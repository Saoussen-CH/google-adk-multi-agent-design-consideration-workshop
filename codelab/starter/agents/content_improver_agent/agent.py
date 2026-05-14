import os
from google.adk.agents import Agent
from .tools import exit_loop, QUALITY_THRESHOLD_MET
from common.callbacks import inject_current_date
from common.retry import GENERATE_CONTENT_CONFIG
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

content_improver_agent = Agent(
    name="content_improver_agent",
    model=MODEL_NAME,
    instruction=f"""
    Today's date is {{current_date}}. Keep any time-sensitive references aligned with this date.

    Current content: {{current_content}}
    Feedback: {{quality_feedback}}

    - IF feedback is '{QUALITY_THRESHOLD_MET}':
      1. Call the `exit_loop` tool to terminate the loop
      2. Respond with the COMPLETE current content in markdown (do NOT add status messages).

    - ELSE: improve based on issues:
      * Expand if short (add examples, details, explanations)
      * Simplify if complex (shorter sentences, simpler words)
      * Add clear H2 headings if missing
      * Add a strong conclusion if missing

      Output the COMPLETE improved content in markdown.
    """,
    tools=[exit_loop],  # exit_loop sets tool_context.actions.escalate = True to break the loop
    before_agent_callback=inject_current_date,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    output_key="current_content",  # Overwrites the previous draft in session state
)

root_agent = content_improver_agent
