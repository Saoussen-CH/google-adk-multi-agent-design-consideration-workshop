import os
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from .tools import calculate_content_quality_score, QUALITY_THRESHOLD_MET
from common.retry import GENERATE_CONTENT_CONFIG
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

quality_checker_agent = Agent(
    name="quality_checker_agent",
    model=MODEL_NAME,
    instruction=f"""
    You are a content quality analyst. Analyze: {{current_content}}

    Your job:
    1. Count approximate word count
    2. Estimate readability score (60+ is good)
    3. Check for clear headings
    4. Check for conclusion section

    Use `calculate_content_quality_score` tool.

    Then:
    - IF overall_score >= 70, respond with: '{QUALITY_THRESHOLD_MET}'
    - ELSE, respond with: 'Quality score: [score]. Issues: [specific problems]'
    """,
    tools=[FunctionTool(calculate_content_quality_score)],
    generate_content_config=GENERATE_CONTENT_CONFIG,
    output_key="quality_feedback",  # Saves feedback to session state["quality_feedback"]
)

root_agent = quality_checker_agent
