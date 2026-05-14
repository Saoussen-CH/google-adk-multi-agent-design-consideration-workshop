import os
from google.adk.agents import Agent
from common.callbacks import inject_current_date
from common.retry import GENERATE_CONTENT_CONFIG
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

social_media_creator_agent = Agent(
    name="social_media_creator_agent",
    model=MODEL_NAME,
    instruction="""
    Today's date is {current_date}. Anchor any time-sensitive references (trends, hashtags, "this year") to this date.

    You are a social media specialist. Create posts from: {current_content}

    Create:
    1. LinkedIn Post (150-200 words, professional)
    2. Twitter Thread (3 tweets, 280 chars each)
    3. Instagram Caption (100-150 words, with emojis and hashtags)

    Format with clear headers for each platform.
    """,
    tools=[],
    before_agent_callback=inject_current_date,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    output_key="social_media_posts",  # Saves to session state["social_media_posts"]
)

root_agent = social_media_creator_agent
