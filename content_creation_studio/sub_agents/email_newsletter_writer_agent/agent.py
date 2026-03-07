from google.adk.agents import Agent
from content_creation_studio.config import MODEL_NAME

email_newsletter_writer_agent = Agent(
    name="email_newsletter_writer_agent",
    model=MODEL_NAME,
    instruction="""
    You are an email marketing specialist. Create a newsletter from: {{current_content}}

    Include:
    - Subject Line (compelling, 50-60 chars)
    - Preview Text (40-50 chars)
    - Body (300-400 words with CTA)

    Format with clear sections.
    """,
    tools=[],
    output_key="email_newsletter"
)
