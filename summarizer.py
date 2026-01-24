# summarizer.py
"""
Summarization logic.
v1 uses simple heuristics (no external AI yet).
"""

from config import HIGH_URGENCY_KEYWORDS, MAX_SUMMARY_BULLETS
from schema import empty_output


def summarize_email(cleaned_email: str) -> dict:
    output = empty_output()

    text_lower = cleaned_email.lower()

    # Urgency detection
    for keyword in HIGH_URGENCY_KEYWORDS:
        if keyword in text_lower:
            output["urgency"] = "high"
            break

    # Simple sentence-based summary
    sentences = [s.strip() for s in cleaned_email.split(".") if s.strip()]
    output["summary_bullets"] = sentences[:MAX_SUMMARY_BULLETS]

    # Action item heuristic
    for sentence in sentences:
        if sentence.lower().startswith(("please", "can you", "do ", "remember to")):
            output["action_items"].append(sentence)

    return output
