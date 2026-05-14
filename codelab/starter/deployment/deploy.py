"""
Deployment Script for Content Creation Multi-Agent System
==========================================================
This script handles:
1. Deployment to Gemini Enterprise Agent Runtime
2. Testing the deployed agent
3. Cleanup

Prerequisites:
- Google Cloud Project with Vertex AI API enabled
- Authenticated via `gcloud auth application-default login`
- A GCS bucket for staging

Usage:
    python deployment/deploy.py --action [deploy|test_remote|cleanup]

"""

import argparse
import asyncio
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import vertexai
from vertexai import agent_engines
from google.adk.plugins.logging_plugin import LoggingPlugin

# Add project root to Python path so the `agents` package is importable
# (matches the qualified imports inside agents/orchestrator_agent/agent.py
# and the runtime layout produced by extra_packages=["agents", ...]).
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from agents.orchestrator_agent.agent import root_agent

# Load environment variables from .env file
load_dotenv()

# =============================================================================
# CONFIGURATION - Loaded from environment variables
# =============================================================================

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
STAGING_BUCKET = os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET")
DISPLAY_NAME = "content-creation-multiagentsystem"

if not PROJECT_ID:
    raise EnvironmentError("GOOGLE_CLOUD_PROJECT is not set. Copy .env.example to .env and fill in your project ID.")
if not STAGING_BUCKET:
    raise EnvironmentError("GOOGLE_CLOUD_STORAGE_BUCKET is not set. Copy .env.example to .env and set your staging bucket.")

# For Express Mode (no GCP project required):
# API_KEY = "your-express-mode-api-key"


# =============================================================================
# HELPERS
# =============================================================================

def update_env_file(key: str, value: str):
    """Write or update a key=value pair in the .env file in the project root."""
    env_path = project_root / ".env"
    if not env_path.exists():
        env_path.write_text(f"{key}={value}\n")
        print(f"  Created .env with {key}")
        return

    lines = env_path.read_text().splitlines(keepends=True)
    updated = False
    for i, line in enumerate(lines):
        if line.startswith(f"{key}=") or line.startswith(f"{key} ="):
            lines[i] = f"{key}={value}\n"
            updated = True
            break
    if not updated:
        lines.append(f"{key}={value}\n")

    env_path.write_text("".join(lines))
    print(f"  .env updated: {key}={value}")


# =============================================================================
# INITIALIZATION
# =============================================================================

def init_vertex_ai():
    """Initialize Vertex AI SDK with project settings."""
    vertexai.init(
        project=PROJECT_ID,
        location=LOCATION,
        staging_bucket=STAGING_BUCKET,
    )
    print(f"✓ Initialized Vertex AI")
    print(f"  Project: {PROJECT_ID}")
    print(f"  Location: {LOCATION}")
    print(f"  Staging: {STAGING_BUCKET}")


# For Express Mode initialization:
# def init_vertex_ai_express():
#     """Initialize Vertex AI in Express Mode (no GCP project needed)."""
#     vertexai.init(key=API_KEY)
#     print("✓ Initialized Vertex AI in Express Mode")



# =============================================================================
# DEPLOYMENT
# =============================================================================

def deploy_to_agent_engine():
    """Deploy the agent to Gemini Enterprise Agent Runtime."""
    print("\n" + "=" * 60)
    print("DEPLOYING TO GEMINI ENTERPRISE AGENT RUNTIME")
    print("=" * 60)

    init_vertex_ai()

    adk_app = agent_engines.AdkApp(
        agent=root_agent,
        app_name="content_creation",  # CRITICAL: Required for Memory Bank scope
        plugins=[LoggingPlugin()],  # Enable comprehensive observability logging
    )

    print("\n⏳ Deploying agent (this may take several minutes)...")

    # Change to project root so extra_packages paths are relative in the tarball
    os.chdir(project_root)

    agent_engine_resource = agent_engines.create(
        agent_engine=adk_app,
        display_name=DISPLAY_NAME,
        requirements=[
            "google-cloud-aiplatform[agent_engines]>=1.148.1,<2.0.0",
            "google-adk==1.31.1",
            "google-genai>=1.72.0,<2.0.0",
            "python-dotenv>=1.0.0",
            "cloudpickle>=3.0.0",
        ],
        extra_packages=["agents", "common"],
        env_vars={
            "GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY": "true",
            "OTEL_SEMCONV_STABILITY_OPT_IN": "gen_ai_latest_experimental",
            "OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT": "true",
            # Capture prompt/response as span events so they appear in the
            # Cloud Trace UI's span detail panel.
            "ADK_CAPTURE_MESSAGE_CONTENT_IN_SPANS": "true",
            "GOOGLE_GENAI_USE_VERTEXAI": "1",

        },
    )

    # Store resource name before updates (it may change after update calls)
    resource_name = agent_engine_resource.resource_name
    agent_engine_id = resource_name.split("/")[-1]


    print("\n" + "=" * 60)
    print("✓ DEPLOYMENT SUCCESSFUL!")
    print("=" * 60)
    print(f"\nResource Name: {resource_name}")
    print(f"Agent Runtime ID: {agent_engine_id}")
  

    update_env_file("AGENT_ENGINE_RESOURCE_NAME", resource_name)

    print(f"\nView in Cloud Console:")
    print(f"https://console.cloud.google.com/vertex-ai/agents/agent-engines?project={PROJECT_ID}")

    return agent_engine_resource


# =============================================================================
# TEST DEPLOYED AGENT
# =============================================================================

async def test_remote_agent(resource_name: str):
    """Test the deployed agent on Gemini Enterprise Agent Runtime."""
    print("\n" + "=" * 60)
    print("TESTING DEPLOYED AGENT")
    print("=" * 60)
    
    init_vertex_ai()
    
    # Connect to deployed agent
    agent_engine_resource = agent_engines.get(resource_name)
    print(f"✓ Connected to: {resource_name}")
    
    # Create remote session
    remote_session = await agent_engine_resource.async_create_session(user_id="remote_test_user")
    print(f"✓ Created remote session: {remote_session['id']}")
    
    # Test query
   
    test_query = """
    Create a complete content package for:
    - Topic: Productivity hacks using AI for remote workers
    - Target Audience: Remote professionals and digital nomads
    - Tone: Conversational and helpful
    - Keywords: AI productivity, remote work, automation tools
    """
    print(f"\n{'─' * 40}")
    print(f"USER: {test_query}")
    print(f"{'─' * 40}")
    
    async for event in agent_engine_resource.async_stream_query(
        user_id="remote_test_user",
        session_id=remote_session["id"],
        message=test_query,
    ):
        # Handle both object-style and dict-style events
        if hasattr(event, "content"):
            content = event.content
            if content and hasattr(content, "parts"):
                for part in content.parts:
                    if getattr(part, "text", None):
                        print(f"\nAGENT: {part.text}")
        elif isinstance(event, dict):
            content = event.get("content") or {}
            if isinstance(content, dict):
                for part in content.get("parts", []):
                    if isinstance(part, dict) and part.get("text"):
                        print(f"\nAGENT: {part['text']}")
    
    print("\n✓ Remote testing complete!")


# =============================================================================
# CLEANUP
# =============================================================================

def cleanup_deployment(resource_name: str):
    """Delete the deployed agent to avoid charges."""
    print("\n" + "=" * 60)
    print("CLEANING UP DEPLOYMENT")
    print("=" * 60)
    
    init_vertex_ai()
    
    agent_engine_resource = agent_engines.get(resource_name)
    agent_engine_resource.delete(force=True)  # force=True also deletes sessions
    
    print(f"✓ Deleted: {resource_name}")
    print("✓ Cleanup complete!")


# =============================================================================
# CLI INTERFACE
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Deploy Content Creation Multi-Agent System to Gemini Enterprise Agent Runtime"
    )
    parser.add_argument(
        "--action",
        choices=["deploy", "test_remote", "cleanup"],
        required=True,
        help="Action to perform"
    )
    parser.add_argument(
        "--resource_name",
        type=str,
        help="Resource name for test_remote or cleanup actions"
    )
    
    args = parser.parse_args()
    
    
    if args.action == "deploy":
        deploy_to_agent_engine()
    
    elif args.action == "test_remote":
        resource_name = args.resource_name or os.getenv("AGENT_ENGINE_RESOURCE_NAME")
        if not resource_name:
            print("ERROR: --resource_name required or set AGENT_ENGINE_RESOURCE_NAME in .env")
            return
        asyncio.run(test_remote_agent(resource_name))

    elif args.action == "cleanup":
        resource_name = args.resource_name or os.getenv("AGENT_ENGINE_RESOURCE_NAME")
        if not resource_name:
            print("ERROR: --resource_name required or set AGENT_ENGINE_RESOURCE_NAME in .env")
            return
        cleanup_deployment(resource_name)


if __name__ == "__main__":
    main()