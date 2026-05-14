"""
Callbacks for the Content Creation Studio.

ADK supports 6 callback types that intercept agent execution at key points:
  - before_agent_callback / after_agent_callback
  - before_model_callback / after_model_callback
  - before_tool_callback / after_tool_callback

Return None to proceed normally, or return a specific object to override behavior.
"""

import time
import logging
from typing import Optional
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse, LlmRequest
from google.genai import types

logger = logging.getLogger(__name__)

# Track agent start times for duration logging
_agent_execution_tracker: dict[str, float] = {}

BLOCKED_TOPICS = ["violence", "illegal", "harmful", "hate speech"]


def _extract_session_id(session) -> str:
    """Safely extract session ID from a session object. PROVIDED — do not modify."""
    if session is None:
        return "unknown"
    return getattr(session, 'id', getattr(session, 'session_id', 'unknown'))


# =============================================================================
# AGENT CALLBACKS — Section 11
# =============================================================================

def before_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """Logs when an agent starts execution and tracks start time.

    Returning None means: proceed with normal agent execution.
    Returning a types.Content would skip the agent entirely.
    """
    # TODO: #REPLACE-before-agent-callback
    # 1. Get agent_name from callback_context.agent_name
    # 2. Get session from callback_context._invocation_context.session
    # 3. Get session_id using _extract_session_id(session)
    # 4. Print a start banner:
    #       print(f"\n{'─'*50}")
    #       print(f"▶ AGENT START: {agent_name}")
    #       print(f"{'─'*50}")
    # 5. Store time.time() in _agent_execution_tracker[f"{agent_name}:{session_id}"]
    # 6. Return None to proceed normally
    pass


async def after_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """Logs agent completion and auto-saves session to Memory."""
    # TODO: #REPLACE-after-agent-callback
    # 1. Get memory_service from callback_context._invocation_context.memory_service
    # 2. Get session from callback_context._invocation_context.session
    # 3. Get agent_name from callback_context.agent_name (use getattr with default 'unknown')
    # 4. Get session_id using _extract_session_id(session)
    # 5. Look up execution_key = f"{agent_name}:{session_id}" in _agent_execution_tracker
    #    If found, pop it and compute total_execution_time = time.time() - start_time
    #    Print "■ AGENT DONE: {agent_name} ({total_execution_time:.1f}s)"
    #    If total_execution_time > 20: logger.warning("Slow agent: %s took %.2fs", ...)
    # 6. If memory_service is not None and has 'add_session_to_memory':
    #       await memory_service.add_session_to_memory(session)
    #       Print how many events were saved
    # 7. Return None
    pass


# =============================================================================
# MODEL CALLBACKS — Section 11
# =============================================================================

def before_model_callback(
    callback_context: CallbackContext,
    llm_request: LlmRequest
) -> Optional[LlmResponse]:
    """Content safety guardrail that runs before every LLM call.

    Returning None means: proceed with the normal model call.
    Returning an LlmResponse skips the actual model call entirely.
    """
    # TODO: #REPLACE-before-model-callback
    # 1. Iterate backwards through llm_request.contents to find the last user message:
    #       for content in reversed(llm_request.contents):
    #           if content.role == "user":
    #               ...check parts...
    #               break
    # 2. For each part in that content's parts, get text = part.text or ""
    # 3. Convert text to lowercase and check if any word in BLOCKED_TOPICS is in it
    # 4. If found, print a guardrail message and return:
    #    LlmResponse(content=types.Content(
    #        parts=[types.Part.from_text(
    #            text=f"I cannot generate content about '{topic}'. Please provide a different topic."
    #        )],
    #        role="model"
    #    ))
    # 5. Return None to proceed with the normal model call
    pass


def after_model_callback(
    callback_context: CallbackContext,
    llm_response: LlmResponse
) -> Optional[LlmResponse]:
    """Logs model response metrics after each LLM call.

    Returning None means: use the model's response as-is.
    """
    # TODO: #REPLACE-after-model-callback
    # 1. Get agent_name from callback_context.agent_name
    # 2. If llm_response.content and llm_response.content.parts exist:
    #       text = llm_response.content.parts[0].text or ""
    #       word_count = len(text.split())
    #       print(f"  📊 Model output for {agent_name}: ~{word_count} words")
    # 3. Return None to use the model response as-is
    pass
