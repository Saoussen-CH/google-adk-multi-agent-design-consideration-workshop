import os
from google.adk.agents import Agent
from common.callbacks import inject_current_date
from common.retry import GENERATE_CONTENT_CONFIG
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

email_newsletter_writer_agent = Agent(
    name="email_newsletter_writer_agent",
    model=MODEL_NAME,
    instruction="""
    Today's date is {current_date}. Anchor any time-sensitive references (seasonal hooks, "this month", "this year") to this date.

    You are an email marketing specialist. Create a newsletter from: {current_content}

    Include:
    - Subject Line (compelling, 50-60 chars)
    - Preview Text (40-50 chars)
    - Body (300-400 words with CTA)

    Format with clear sections.
    """,
    tools=[],
    before_agent_callback=inject_current_date,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    output_key="email_newsletter",  # Saves to session state["email_newsletter"]
)

root_agent = email_newsletter_writer_agent
