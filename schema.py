# schema.py
"""
Output schema helpers.
Ensures deterministic structure.
"""

def empty_output() -> dict:
    return {
        "summary_bullets": [],
        "action_items": [],
        "deadlines": [],
        "urgency": "low",
        "warnings": [],
    }
