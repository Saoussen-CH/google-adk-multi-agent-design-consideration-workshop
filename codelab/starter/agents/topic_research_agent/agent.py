import os
from google.adk.agents import Agent
from google.adk.tools import google_search
from common.callbacks import inject_current_date
from common.retry import GENERATE_CONTENT_CONFIG
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

topic_research_agent = Agent(
    name="topic_research_agent",
    model=MODEL_NAME,
    instruction="""
    Today's date is {current_date}. Anchor "trending", "recent", and "this year" to this date.

    You are a topic research expert. Based on the user's request,
    use search to find trending angles and select the SINGLE BEST specific blog post title.
    Output format: Just the title, nothing else.

    Example: "10 AI Tools That Save Small Businesses 20 Hours Per Week"
    """,
    tools=[google_search],
    before_agent_callback=inject_current_date,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    output_key="blog_topic",  # Saves the agent's final response to session state["blog_topic"]
)

root_agent = topic_research_agent
