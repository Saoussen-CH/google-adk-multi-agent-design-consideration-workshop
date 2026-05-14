import os
from dotenv import load_dotenv

# Ensure environment variables are loaded
load_dotenv()

from google.adk.agents import SequentialAgent, LoopAgent, ParallelAgent, LlmAgent
from google.adk.tools import preload_memory_tool
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
MAX_IMPROVEMENT_ITERATIONS = int(os.getenv("MAX_IMPROVEMENT_ITERATIONS", "2"))
from common.retry import GENERATE_CONTENT_CONFIG

from .callbacks import (
    before_agent_callback,
    after_agent_callback,
    before_model_callback,
    after_model_callback,
)
from agents.topic_research_agent.agent import topic_research_agent
from agents.content_drafter_agent.agent import content_drafter_agent
from agents.quality_checker_agent.agent import quality_checker_agent
from agents.content_improver_agent.agent import content_improver_agent
from agents.blog_post_writer_agent.agent import blog_post_writer_agent
from agents.social_media_creator_agent.agent import social_media_creator_agent
from agents.email_newsletter_writer_agent.agent import email_newsletter_writer_agent
from agents.seo_metadata_agent.agent import seo_metadata_agent
from agents.content_analyzer_agent.agent import content_analyzer_agent


# --- Section 6: Sequential — Research and Draft ---
# TODO: #REPLACE-research-and-draft-workflow
# Create a SequentialAgent named "research_and_draft_workflow"
# with sub_agents=[topic_research_agent, content_drafter_agent]
research_and_draft_workflow = None  # Replace this line


# --- Section 7: Loop — Quality Improvement ---
# TODO: #REPLACE-quality-improvement-loop
# Create a LoopAgent named "quality_improvement_loop"
# with sub_agents=[quality_checker_agent, content_improver_agent]
# and max_iterations=MAX_IMPROVEMENT_ITERATIONS
quality_improvement_loop = None  # Replace this line


# --- Section 8: Parallel — Multi-Channel Content Creation ---
# TODO: #REPLACE-parallel-content-creation
# Create a ParallelAgent named "parallel_content_creation"
# with sub_agents=[blog_post_writer_agent, social_media_creator_agent,
#                  email_newsletter_writer_agent, seo_metadata_agent]
parallel_content_creation = None  # Replace this line


# --- Section 9: Full Content Workflow ---
# TODO: #REPLACE-full-content-workflow
# Create a SequentialAgent named "full_content_workflow"
# with sub_agents=[research_and_draft_workflow, quality_improvement_loop,
#                  parallel_content_creation]
full_content_workflow = None  # Replace this line


# --- Section 10: Root Agent (Orchestrator) ---
# TODO: #REPLACE-orchestrator
# Create an LlmAgent named "orchestrator_agent" with:
#   - model=MODEL_NAME  (plain string — lets ADK pick the right backend at runtime)
#   - instruction: routes to full_content_workflow for content creation
#                  OR content_analyzer_agent for text analysis
#                  (mention that past memory is loaded before each turn)
#   - sub_agents=[full_content_workflow, content_analyzer_agent]
#   - tools=[preload_memory_tool.PreloadMemoryTool()]
#   - before_agent_callback=before_agent_callback
#   - after_agent_callback=after_agent_callback
#   - before_model_callback=before_model_callback
#   - after_model_callback=after_model_callback
orchestrator_agent = None  # Replace this line


# root_agent is used by `adk web` and the Runner
root_agent = orchestrator_agent
