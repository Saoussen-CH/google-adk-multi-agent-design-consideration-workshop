from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from content_creation_studio.config import MODEL_NAME, RETRY_CONFIG

content_drafter_agent = Agent(
    name="content_drafter_agent",
    model=Gemini(model=MODEL_NAME, retry_options=RETRY_CONFIG),
    instruction="""
    TODO: #REPLACE-content-drafter-instruction
    Write an instruction that:
    1. Tells the agent it is a content writer
    2. References {{blog_topic}} to read the researched title from session state
       (ADK substitutes {{blog_topic}} with the value from session state automatically)
    3. Asks for a draft of 400-600 words with:
       - An engaging introduction
       - At least 2 H2 headings (## Heading)
       - A conclusion section
    4. Instructs the agent to output ONLY the blog post in markdown format
    """,
    tools=[],
    output_key="current_content",  # Saves to session state["current_content"]
)
