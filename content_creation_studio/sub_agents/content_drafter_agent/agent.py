from google.adk.agents import Agent
from content_creation_studio.config import MODEL_NAME

content_drafter_agent = Agent(
    name="content_drafter_agent",
    model=MODEL_NAME,
    instruction="""
    You are a content writer. Write a blog post: {{blog_topic}}

    Create a draft (400-600 words) with:
    - Engaging introduction
    - At least 2 H2 headings
    - A conclusion section

    Output only the blog post in markdown format.
    """,
    tools=[],
    output_key="current_content"
)
