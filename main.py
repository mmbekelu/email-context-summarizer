# main.py
"""
Entry point for the Email Summarizer product.

Pipeline:
input -> validation -> cleaning -> summarization -> logging -> output
"""

from validators import validate_email
from cleaner import clean_email
from summarizer import summarize_email
from logger import log_event


def run(email_text: str) -> dict:
    """
    Runs the full email summarization pipeline.
    Returns a structured summary dict or an error dict.
    """

    # 1. Validate input
    is_valid, error_message = validate_email(email_text)
    if not is_valid:
        log_event("validation_failed", error_message)
        return {
            "error": error_message
        }

    # 2. Clean email text
    cleaned_email, warnings = clean_email(email_text)

    # 3. Summarize
    summary_output = summarize_email(cleaned_email)

    # 4. Attach warnings (from cleaning step)
    summary_output["warnings"] = warnings

    # 5. Log success
    log_event("summarization_success", "Email summarized successfully")

    return summary_output


if
