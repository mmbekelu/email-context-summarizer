
# validators.py
"""
Validation layer for the Email Summarizer.

Purpose:
- Reject bad inputs BEFORE we do any cleaning or AI summarization.
- Return explainable error messages (product behavior).
"""

from __future__ import annotations
import re
import json
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "MIN_CHARS": 30,
            "MAX_CHARS": 5000
        }

CONFIG = load_config()

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

    min_chars = CONFIG.get("MIN_CHARS", 30)
    max_chars = CONFIG.get("MAX_CHARS", 5000)

    if len(text) < min_chars:
        return False, f"Email is too short (min {min_chars} characters)."

    if len(text) > max_chars:
        return False, f"Email is too long (max {max_chars} characters)."

    # --- Anti-gibberish checks (v2) ---

    # Must contain spaces (real language)
    if text.count(" ") < 3:
        return False, "Email does not appear to contain real sentences."

    # Must contain alphabetic words
    words = re.findall(r"[a-zA-Z]{2,}", text)
    if len(words) < 5:
        return False, "Email does not contain enough readable words."

    return True, ""
