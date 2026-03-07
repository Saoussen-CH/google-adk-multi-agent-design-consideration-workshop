from google.adk.agents import Agent
from content_creation_studio.config import MODEL_NAME

blog_post_writer_agent = Agent(
    name="blog_post_writer_agent",
    model=MODEL_NAME,
    instruction="""
    You are a professional blog writer. Create the final polished blog post from: {{current_content}}

    Enhance it to be publication-ready:
    - Ensure 800-1200 words
    - Add engaging subheadings
    - Include actionable tips
    - Strong call-to-action

    Output only the final blog post in markdown.
    """,
    tools=[],
    output_key="final_blog_post"
)
