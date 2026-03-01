
# summarizer.py
"""
Summarization logic.
v1 uses simple heuristics (no external AI yet).
"""

import re
import json
import os
from schema import empty_output

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "HIGH_URGENCY_KEYWORDS": ["urgent", "asap", "emergency", "immediately", "critical"],
            "MAX_SUMMARY_BULLETS": 3,
            "ACTION_ITEM_STARTS": ["please", "can you", "could you", "do ", "remember to", "i wanted to ask"],
            "DEADLINE_PATTERNS": ["by\\s+\\w+", "by\\s+\\w+\\s+\\d{1,2}", "\\btomorrow\\b", "\\beod\\b"]
        }

CONFIG = load_config()

def summarize_email(cleaned_email: str) -> dict:
    output = empty_output()
    text_lower = cleaned_email.lower()

    # Urgency detection
    for keyword in CONFIG.get("HIGH_URGENCY_KEYWORDS", []):
        if keyword in text_lower:
            output["urgency"] = "high"
            break

    # Sentence splitting
    sentences = [s.strip() for s in re.split(r"[.!?]", cleaned_email) if s.strip()]

    # Summary bullets
    max_bullets = CONFIG.get("MAX_SUMMARY_BULLETS", 3)
    output["summary_bullets"] = sentences[:max_bullets]

    # Action items
    action_starts = tuple(CONFIG.get("ACTION_ITEM_STARTS", []))

    for sentence in sentences:
        s_low = sentence.lower()
        if s_low.startswith(action_starts) or "?" in sentence:
            output["action_items"].append(sentence)

    # Deadline extraction (v1)
    deadline_patterns = CONFIG.get("DEADLINE_PATTERNS", [])

    for pattern in deadline_patterns:
        matches = re.findall(pattern, text_lower)
        output["deadlines"].extend(matches)

    return output
