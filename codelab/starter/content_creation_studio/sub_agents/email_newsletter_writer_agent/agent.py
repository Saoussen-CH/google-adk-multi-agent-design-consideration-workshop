from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from content_creation_studio.config import MODEL_NAME, RETRY_CONFIG

email_newsletter_writer_agent = Agent(
    name="email_newsletter_writer_agent",
    model=Gemini(model=MODEL_NAME, retry_options=RETRY_CONFIG),
    instruction="""
    TODO: #REPLACE-email-newsletter-instruction
    Write an instruction that:
    1. Reads {{current_content}} from session state
    2. Creates a complete email newsletter with:
       - Subject Line: compelling, 50-60 characters
       - Preview Text: 40-50 characters
       - Body: 300-400 words with a clear call-to-action (CTA)
    3. Formats the output with clear section labels for each part
    """,
    tools=[],
    output_key="email_newsletter",  # Saves to session state["email_newsletter"]
)
