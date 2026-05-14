"""FastAPI server to expose the content creation agent via Gemini Enterprise Agent Runtime."""

import os
import asyncio
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import json
from pathlib import Path

# Load environment variables
load_dotenv()

from vertexai import agent_engines

# Get Agent Runtime resource name from environment
# Allow it to be missing at startup for health checks, but required for actual API calls
AGENT_RESOURCE_NAME = os.environ.get("AGENT_RESOURCE_NAME") or os.environ.get("AGENT_ENGINE_RESOURCE_NAME")

# Agent name for session management
AGENT_NAME = "orchestrator_agent"

# Map sub-agent names to frontend channel names.
# With sub_agents, inner events propagate and include the author field.
CHANNEL_MAP = {
    "blog_post_writer_agent": "blog_post",
    "social_media_creator_agent": "social_media",
    "email_newsletter_writer_agent": "email_newsletter",
    "seo_metadata_agent": "seo_metadata",
}

# Get remote agent instance if configured
remote_agent = None
if AGENT_RESOURCE_NAME:
    try:
        remote_agent = agent_engines.get(AGENT_RESOURCE_NAME)
    except Exception as e:
        print(f"Warning: Failed to connect to Agent Runtime: {e}")
        print(f"The server will start but API calls will fail.")


# Initialize FastAPI app
app = FastAPI(title="Content Creation Studio API")

# Configure CORS - allow frontend URL from environment or defaults
allowed_origins = ["http://localhost:3000", "http://localhost:5173"]
if os.environ.get("FRONTEND_URL"):
    allowed_origins.append(os.environ.get("FRONTEND_URL"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check if static files directory exists (for production deployment)
STATIC_DIR = Path(__file__).parent / "static"
if STATIC_DIR.exists():
    # Mount static files for production (when frontend is built into the backend)
    app.mount("/assets", StaticFiles(directory=str(STATIC_DIR / "assets")), name="assets")

# Note: We don't need a session service for remote agents
# The remote agent manages sessions internally


class ContentRequest(BaseModel):
    """Request model for content creation."""
    topic: str
    target_audience: str
    tone: str
    keywords: str
    session_id: Optional[str] = None


class AnalyzeRequest(BaseModel):
    """Request model for text analysis."""
    text: str


@app.get("/health")
async def health():
    """Health check endpoint for monitoring."""
    return {
        "status": "ok",
        "message": "Content Creation Studio API is running",
        "agent": AGENT_NAME,
        "agent_resource": AGENT_RESOURCE_NAME if AGENT_RESOURCE_NAME else "Not configured",
        "agent_connected": remote_agent is not None
    }


@app.get("/")
async def serve_frontend():
    """Serve the React frontend if static files exist, otherwise return API info."""
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return FileResponse(str(index_file))
    else:
        # Fallback to API info if no static files (development mode)
        return {
            "status": "ok",
            "message": "Content Creation Studio API is running",
            "agent": AGENT_NAME,
            "agent_resource": AGENT_RESOURCE_NAME if AGENT_RESOURCE_NAME else "Not configured",
            "agent_connected": remote_agent is not None,
            "mode": "development - frontend not bundled"
        }


@app.post("/api/create-content")
async def create_content(request: ContentRequest):
    """
    Create a complete content package.
    Returns streaming response with real-time updates.
    """
    # Check if agent is configured
    if not remote_agent:
        raise HTTPException(
            status_code=503,
            detail="Agent Runtime not configured. Set AGENT_RESOURCE_NAME environment variable."
        )

    try:
        # Create session with remote agent
        user_id = "web_user_001"

        # Create or get session
        if request.session_id:
            # Try to use existing session
            session_id = request.session_id
        else:
            # Create new session
            session = await remote_agent.async_create_session(user_id=user_id)
            session_id = session['id']

        # Build the query
        query = f"""Create a complete content package for:
- Topic: {request.topic}
- Target Audience: {request.target_audience}
- Tone: {request.tone}
- Keywords: {request.keywords}
"""

        async def generate():
            """Stream events from the workflow. With sub_agents, inner events
            propagate and include the author field for per-channel mapping."""
            try:
                yield f"data: {json.dumps({'type': 'status', 'message': 'Starting content creation workflow...', 'session_id': session_id})}\n\n"

                event_count = 0
                channels_received = set()

                async for event in remote_agent.async_stream_query(
                    user_id=user_id,
                    session_id=session_id,
                    message=query
                ):
                    event_count += 1

                    if not isinstance(event, dict):
                        continue

                    # Extract author and text from the event
                    author = event.get("author", "")
                    channel = CHANNEL_MAP.get(author)

                    text = ""
                    content = event.get("content", {})
                    if isinstance(content, dict):
                        for part in content.get("parts", []):
                            if isinstance(part, dict) and part.get("text"):
                                text += part["text"]
                    if "text" in event:
                        text += event["text"]

                    if channel and text:
                        channels_received.add(channel)
                        yield f"data: {json.dumps({'type': 'content_piece', 'channel': channel, 'content': text})}\n\n"
                    elif text:
                        # Progress update for non-channel events
                        yield f"data: {json.dumps({'type': 'event', 'event_id': event_count, 'author': author})}\n\n"

                if channels_received:
                    yield f"data: {json.dumps({'type': 'complete', 'session_id': session_id})}\n\n"
                else:
                    yield f"data: {json.dumps({'type': 'error', 'message': 'No content received from agents', 'retryable': True})}\n\n"

            except Exception as e:
                error_message = str(e)
                if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
                    friendly = "The AI service is temporarily busy (quota exhausted). Please wait a moment and try again."
                    retryable = True
                elif "TaskGroup" in error_message:
                    friendly = "Some content channels had issues during generation. Please try again."
                    retryable = True
                elif "500" in error_message or "503" in error_message or "UNAVAILABLE" in error_message:
                    friendly = "The AI service experienced a temporary issue. Please try again."
                    retryable = True
                elif "DEADLINE_EXCEEDED" in error_message or "timeout" in error_message.lower():
                    friendly = "The workflow took too long to complete. Please try again."
                    retryable = True
                else:
                    friendly = "An unexpected error occurred. Please try again."
                    retryable = False
                print(f"Error detail: {error_message}")
                yield f"data: {json.dumps({'type': 'error', 'message': friendly, 'retryable': retryable})}\n\n"

        return StreamingResponse(
            generate(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "X-Accel-Buffering": "no"
            }
        )

    except Exception as e:
        error_message = str(e)
        print(f"Error detail: {error_message}")
        if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
            raise HTTPException(status_code=429, detail="The AI service is temporarily busy (quota exhausted). Please try again later.")
        raise HTTPException(status_code=500, detail="An error occurred starting the workflow. Please try again.")


@app.post("/api/analyze-text")
async def analyze_text(request: AnalyzeRequest):
    """Analyze text snippet."""
    # Check if agent is configured
    if not remote_agent:
        raise HTTPException(
            status_code=503,
            detail="Agent Runtime not configured. Set AGENT_RESOURCE_NAME environment variable."
        )

    try:
        user_id = "web_user_001"

        # Create session
        session = await remote_agent.async_create_session(user_id=user_id)
        session_id = session['id']

        query = f"Can you analyze this text snippet:\n\n{request.text}"

        # Stream query to remote agent and collect response
        response_text = ""

        async for event in remote_agent.async_stream_query(
            user_id=user_id,
            session_id=session_id,
            message=query
        ):
            # Extract text from event
            if isinstance(event, dict):
                content = event.get("content", event.get("parts", {}))

                if isinstance(content, dict):
                    parts = content.get("parts", [])
                    for part in parts:
                        if isinstance(part, dict) and part.get("text"):
                            response_text += part["text"]

                # Also check for direct text field
                if "text" in event:
                    response_text += event["text"]

        return {
            "status": "success",
            "analysis": response_text if response_text else "No analysis received"
        }

    except Exception as e:
        error_message = str(e)
        print(f"Error detail: {error_message}")
        if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
            raise HTTPException(status_code=429, detail="The AI service is temporarily busy (quota exhausted). Please try again later.")
        raise HTTPException(status_code=500, detail="An error occurred during analysis. Please try again.")


if __name__ == "__main__":
    import uvicorn

    # Warn if agent not configured, but still start server
    if not AGENT_RESOURCE_NAME:
        print("⚠️  WARNING: AGENT_RESOURCE_NAME not found in environment variables!")
        print("   The server will start, but API calls will fail until configured.")
        print("   Deploy your agent to Agent Runtime first and set this variable.")
    else:
        print(f"🤖 Connected to Agent: {AGENT_RESOURCE_NAME}")

    print("✅ Starting Content Creation Studio API Server")
    print("📡 Server will be available at: http://localhost:8000")
    print("📚 API Docs at: http://localhost:8000/docs")

    uvicorn.run(app, host="0.0.0.0", port=8000)
