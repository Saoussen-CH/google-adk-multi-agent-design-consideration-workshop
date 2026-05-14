import os
from google.adk.agents import Agent
from common.callbacks import inject_current_date
from common.retry import GENERATE_CONTENT_CONFIG
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

content_drafter_agent = Agent(
    name="content_drafter_agent",
    model=MODEL_NAME,
    instruction="""
    Today's date is {current_date}. Anchor any references to "now", "current", or "this year" to this date.

    You are a content writer. Write a blog post: {blog_topic}

    Create a draft (400-600 words) with:
    - Engaging introduction
    - At least 2 H2 headings
    - A conclusion section

    Output only the blog post in markdown format.
    """,
    tools=[],
    before_agent_callback=inject_current_date,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    output_key="current_content",  # Saves to session state["current_content"]
)

root_agent = content_drafter_agent
