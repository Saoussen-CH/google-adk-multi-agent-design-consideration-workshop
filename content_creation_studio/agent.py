import os
from dotenv import load_dotenv

# Ensure environment variables are loaded (especially GOOGLE_API_KEY)
load_dotenv()

from google.adk.agents import SequentialAgent, LoopAgent, ParallelAgent, Agent
from google.adk.tools import preload_memory_tool
from content_creation_studio.config import MODEL_NAME, MAX_IMPROVEMENT_ITERATIONS
from content_creation_studio.callbacks import (
    before_agent_callback,
    after_agent_callback,
    before_model_callback,
    after_model_callback,
)
from content_creation_studio.sub_agents.topic_research_agent.agent import topic_research_agent
from content_creation_studio.sub_agents.content_drafter_agent.agent import content_drafter_agent
from content_creation_studio.sub_agents.quality_checker_agent.agent import quality_checker_agent
from content_creation_studio.sub_agents.content_improver_agent.agent import content_improver_agent
from content_creation_studio.sub_agents.blog_post_writer_agent.agent import blog_post_writer_agent
from content_creation_studio.sub_agents.social_media_creator_agent.agent import social_media_creator_agent
from content_creation_studio.sub_agents.email_newsletter_writer_agent.agent import email_newsletter_writer_agent
from content_creation_studio.sub_agents.seo_metadata_agent.agent import seo_metadata_agent
from content_creation_studio.sub_agents.content_analyzer_agent.agent import content_analyzer_agent

# --- Sequential: Research and Draft ---
research_and_draft_workflow = SequentialAgent(
    name="research_and_draft_workflow",
    sub_agents=[topic_research_agent, content_drafter_agent]
)

# --- Loop: Quality Improvement ---
quality_improvement_loop = LoopAgent(
    name="quality_improvement_loop",
    sub_agents=[quality_checker_agent, content_improver_agent],
    max_iterations=MAX_IMPROVEMENT_ITERATIONS
)

# --- Parallel: Multi-Channel Content Creation ---
parallel_content_creation = ParallelAgent(
    name="parallel_content_creation",
    sub_agents=[
        blog_post_writer_agent,
        social_media_creator_agent,
        email_newsletter_writer_agent,
        seo_metadata_agent
    ]
)

# --- Full Content Workflow ---
# The user's request is passed as conversation context through AgentTool.
# Sub-agents read it from the conversation, not from state.
full_content_workflow = SequentialAgent(
    name="full_content_workflow",
    sub_agents=[
        research_and_draft_workflow,
        quality_improvement_loop,
        parallel_content_creation,
    ]
)

# --- Root Agent ---
# Uses sub_agents for event visibility (inner events propagate to the Runner).
# The LLM transfers control to the appropriate sub-agent based on user intent.
master_orchestrator_agent = Agent(
    name="master_orchestrator_agent",
    model=MODEL_NAME,
    instruction="""
    You are the Master Content Creation Studio orchestrator. Delegate tasks to specialists.

    Past conversations from long-term memory are automatically loaded before each turn.
    Use this context to provide continuity across sessions.

    - For FULL content creation (topic research -> draft -> improve -> multi-channel content),
      transfer to `full_content_workflow`. Pass the complete user request with topic, audience, tone, and keywords.

    - For ANALYZING existing text (readability, word count, hashtags),
      transfer to `content_analyzer_agent`.

    Always delegate to the appropriate agent.
    """,
    sub_agents=[full_content_workflow, content_analyzer_agent],
    tools=[preload_memory_tool.PreloadMemoryTool()],
    before_agent_callback=before_agent_callback,
    after_agent_callback=after_agent_callback,
    before_model_callback=before_model_callback,
    after_model_callback=after_model_callback,
)

# root_agent is used by `adk web` and `run_agent.py`
root_agent = master_orchestrator_agent
