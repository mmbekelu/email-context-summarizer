# validators.py
"""
Validation layer for the Email Summarizer.

Purpose:
- Reject bad inputs BEFORE we do any cleaning or AI summarization.
- Return explainable error messages (product behavior).
"""

from __future__ import annotations
import re

from config import MIN_CHARS, MAX_CHARS


def validate_email(email_text: object) -> tuple[bool, str]:
    """
    Validate raw email text.

    Returns:
        (is_valid, error_message)
    """

    if not isinstance(email_text, str):
        return False, "Input must be a string."

    text = email_text.strip()

    if not text:
        return False, "Email text is empty."

    if len(text) < MIN_CHARS:
        return False, f"Email is too short (min {MIN_CHARS} characters)."

    if len(text) > MAX_CHARS:
        return False, f"Email is too long (max {MAX_CHARS} characters)."

    # --- Anti-gibberish checks (v2) ---

    # Must contain spaces (real language)
    if text.count(" ") < 3:
        return False, "Email does not appear to contain real sentences."

    # Must contain alphabetic words
    words = re.findall(r"[a-zA-Z]{2,}", text)
    if len(words) < 5:
        return False, "Email does not contain enough readable words."

    return True, ""
