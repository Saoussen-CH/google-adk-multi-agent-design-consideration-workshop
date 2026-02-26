from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from content_creation_studio.config import MODEL_NAME, RETRY_CONFIG

seo_metadata_agent = Agent(
    name="seo_metadata_agent",
    model=Gemini(model=MODEL_NAME, retry_options=RETRY_CONFIG),
    instruction="""
    TODO: #REPLACE-seo-metadata-instruction
    Write an instruction that generates SEO metadata from {{current_content}}:
    1. Meta Title: 50-60 characters
    2. Meta Description: 150-160 characters
    3. URL Slug: lowercase, hyphenated
    4. Focus Keyword: the single primary keyword
    5. 5 Related Keywords

    Format as readable markdown with bold labels (not JSON).
    """,
    tools=[],
    output_key="seo_metadata",  # Saves to session state["seo_metadata"]
)
