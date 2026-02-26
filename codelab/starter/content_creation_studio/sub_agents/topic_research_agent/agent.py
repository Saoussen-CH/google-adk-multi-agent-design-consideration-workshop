from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from content_creation_studio.config import MODEL_NAME, RETRY_CONFIG

topic_research_agent = Agent(
    name="topic_research_agent",
    model=Gemini(model=MODEL_NAME, retry_options=RETRY_CONFIG),
    instruction="""
    TODO: #REPLACE-topic-research-instruction
    Write an instruction that tells the agent to:
    1. Use google_search to find trending angles for the user's topic
    2. Select the SINGLE BEST specific blog post title
    3. Output ONLY the title, nothing else

    Example output: "10 AI Tools That Save Small Businesses 20 Hours Per Week"
    """,
    tools=[google_search],
    output_key="blog_topic",  # Saves the agent's final response to session state["blog_topic"]
)
