import os
from dotenv import load_dotenv

# Ensure environment variables are loaded (especially GOOGLE_API_KEY)
load_dotenv()

from google.adk.agents import SequentialAgent, LoopAgent, ParallelAgent, Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import preload_memory_tool
from content_creation_studio.config import MODEL_NAME, RETRY_CONFIG, MAX_IMPROVEMENT_ITERATIONS
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


# --- Step 8: Sequential — Research and Draft ---
# TODO: #REPLACE-research-and-draft-workflow
# Create a SequentialAgent named "research_and_draft_workflow"
# with sub_agents=[topic_research_agent, content_drafter_agent]
research_and_draft_workflow = None  # Replace this line


# --- Step 10: Loop — Quality Improvement ---
# TODO: #REPLACE-quality-improvement-loop
# Create a LoopAgent named "quality_improvement_loop"
# with sub_agents=[quality_checker_agent, content_improver_agent]
# and max_iterations=MAX_IMPROVEMENT_ITERATIONS
quality_improvement_loop = None  # Replace this line


# --- Step 11: Parallel — Multi-Channel Content Creation ---
# TODO: #REPLACE-parallel-content-creation
# Create a ParallelAgent named "parallel_content_creation"
# with sub_agents=[blog_post_writer_agent, social_media_creator_agent,
#                  email_newsletter_writer_agent, seo_metadata_agent]
parallel_content_creation = None  # Replace this line


# --- Step 12: Full Content Workflow ---
# TODO: #REPLACE-full-content-workflow
# Create a SequentialAgent named "full_content_workflow"
# with sub_agents=[research_and_draft_workflow, quality_improvement_loop,
#                  parallel_content_creation]
full_content_workflow = None  # Replace this line


# --- Step 13: Root Agent (Master Orchestrator) ---
# TODO: #REPLACE-master-orchestrator
# Create an Agent named "master_orchestrator_agent" with:
#   - model=Gemini(model=MODEL_NAME, retry_options=RETRY_CONFIG)
#   - instruction: routes to full_content_workflow for content creation
#                  OR content_analyzer_agent for text analysis
#                  (mention that past memory is loaded before each turn)
#   - sub_agents=[full_content_workflow, content_analyzer_agent]
#   - tools=[preload_memory_tool.PreloadMemoryTool()]
#   - before_agent_callback=before_agent_callback
#   - after_agent_callback=after_agent_callback
#   - before_model_callback=before_model_callback
#   - after_model_callback=after_model_callback
master_orchestrator_agent = None  # Replace this line


# root_agent is used by `adk web` and the Runner
root_agent = master_orchestrator_agent
