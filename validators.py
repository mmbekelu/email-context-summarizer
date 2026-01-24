# validators.py
"""
Validation layer for the Email Summarizer.

Purpose:
- Reject bad inputs BEFORE we do any cleaning or AI summarization.
- Return explainable error messages (product behavior).
"""

from __future__ import annotations

from config import MIN_CHARS, MAX_CHARS


def validate_email(email_text: object) -> tuple[bool, str]:
    """
    Validate raw email text.

    Returns:
        (is_valid, error_message)

    Notes:
    - We accept only strings.
    - We strip whitespace before checking length.
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

    return True, ""
