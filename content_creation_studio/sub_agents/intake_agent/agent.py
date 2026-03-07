from google.adk.agents import Agent
from content_creation_studio.config import MODEL_NAME

intake_agent = Agent(
    name="intake_agent",
    model=MODEL_NAME,
    instruction="""
    You are a content brief analyzer. From the user's request, identify:
    - Main topic
    - Target audience
    - Desired tone
    - Key SEO keywords (comma-separated)

    Output a structured brief in this exact format:
    Topic: <topic>
    Audience: <audience>
    Tone: <tone>
    Keywords: <keywords>
    """,
    output_key="content_brief"
)
