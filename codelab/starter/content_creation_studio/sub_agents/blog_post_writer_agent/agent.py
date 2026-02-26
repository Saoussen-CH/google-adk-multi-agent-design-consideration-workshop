from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from content_creation_studio.config import MODEL_NAME, RETRY_CONFIG

blog_post_writer_agent = Agent(
    name="blog_post_writer_agent",
    model=Gemini(model=MODEL_NAME, retry_options=RETRY_CONFIG),
    instruction="""
    TODO: #REPLACE-blog-post-writer-instruction
    Write an instruction that:
    1. Reads {{current_content}} from session state
    2. Transforms it into a publication-ready blog post with:
       - 800-1200 words
       - Engaging subheadings
       - Actionable tips
       - A strong call-to-action at the end
    3. Outputs ONLY the final blog post in markdown format
    """,
    tools=[],
    output_key="final_blog_post",  # Saves to session state["final_blog_post"]
)
