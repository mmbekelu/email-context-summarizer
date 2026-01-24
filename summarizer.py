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

    # Action item heuristic (v2)
    action_starts = (
        "please",
        "can you",
        "could you",
        "do ",
        "remember to",
        "i wanted to ask",
    )

    for sentence in sentences:
        s = sentence.strip()
        s_low = s.lower()

        # Starts with action phrases
        if s_low.startswith(action_starts):
            output["action_items"].append(s)
            continue

        # Questions count as action items (only if the original email has a '?')
        # This works even though we split on "." because the "?" stays in the sentence text.
        if "?" in cleaned_email and s.endswith("?"):
            output["action_items"].append(s)

    return output
