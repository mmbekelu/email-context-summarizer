# cleaner.py
"""
Cleans raw email text before summarization.
Removes signatures and reply chains.
"""

def clean_email(email_text: str) -> tuple[str, list[str]]:
    warnings = []
    lines = email_text.splitlines()

    cleaned_lines = []
    for line in lines:
        lower = line.lower()

        # Remove common signature indicators
        if lower.startswith("thanks") or lower.startswith("best regards"):
            warnings.append("Signature removed")
            break

        # Remove reply chains
        if lower.startswith("on ") and "wrote:" in lower:
            warnings.append("Reply chain removed")
            break

        cleaned_lines.append(line)

    cleaned_text = "\n".join(cleaned_lines).strip()
    return cleaned_text, warnings
