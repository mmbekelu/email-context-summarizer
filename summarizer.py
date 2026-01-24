# summarizer.py
"""
Summarization logic.
v1 uses simple heuristics (no external AI yet).
"""

import re
import config
from schema import empty_output


def summarize_email(cleaned_email: str) -> dict:
    output = empty_output()
    text_lower = cleaned_email.lower()

    # Urgency detection
    for keyword in config.HIGH_URGENCY_KEYWORDS:
        if keyword in text_lower:
            output["urgency"] = "high"
            break

    # Sentence splitting
    sentences = [s.strip() for s in re.split(r"[.!?]", cleaned_email) if s.strip()]

    # 🔥 FIX: read value dynamically from config
    output["summary_bullets"] = sentences[: config.MAX_SUMMARY_BULLETS]

    # Action items
    action_starts = (
        "please",
        "can you",
        "could you",
        "do ",
        "remember to",
        "i wanted to ask",
    )

    for sentence in sentences:
        s_low = sentence.lower()
        if s_low.startswith(action_starts) or "?" in sentence:
            output["action_items"].append(sentence)

    # Deadline extraction (v1)
    deadline_patterns = [
        r"by\s+\w+",              # by Friday
        r"by\s+\w+\s+\d{1,2}",    # by Jan 30
        r"\btomorrow\b",
        r"\beod\b",
    ]

    for pattern in deadline_patterns:
        matches = re.findall(pattern, text_lower)
        output["deadlines"].extend(matches)

    return output

