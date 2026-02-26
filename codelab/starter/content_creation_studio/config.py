"""
Shared configuration for the Content Creation Studio agents.
Centralizes model name and retry settings.
"""

import os
from google.genai import types

# TODO: #REPLACE-model-name
# Set MODEL_NAME from the environment variable "WORKER_MODEL".
# Use "gemini-2.5-flash" as the default if the variable is not set.
MODEL_NAME = None  # Replace this line


# TODO: #REPLACE-retry-config
# Create a RETRY_CONFIG using types.HttpRetryOptions with:
#   - attempts=5
#   - exp_base=7
#   - initial_delay=1
#   - http_status_codes=[429, 500, 503, 504]
RETRY_CONFIG = None  # Replace this line


# TODO: #REPLACE-quality-thresholds
# Set QUALITY_SCORE_THRESHOLD from env var "QUALITY_SCORE_THRESHOLD", default "70" (cast to int)
# Set MAX_IMPROVEMENT_ITERATIONS from env var "MAX_IMPROVEMENT_ITERATIONS", default "2" (cast to int)
QUALITY_SCORE_THRESHOLD = None  # Replace this line
MAX_IMPROVEMENT_ITERATIONS = None  # Replace this line
