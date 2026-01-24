# cleaner.py
"""
Cleans raw email text before summarization.
Removes signatures, reply chains, and normalizes spacing.
"""

def clean_email(email_text: str) -> tuple[str, list[str]]:
    warnings = []
    lines = email_text.splitlines()

    cleaned_lines = []

    for line in lines:
        lower = line.lower().strip()

        # Remove reply chains
        if lower.startswith("on ") and "wrote:" in lower:
            warnings.append("Reply chain removed")
            break

        # Remove common signature indicators
        if lower.startswith(("thanks", "best regards", "sincerely")):
            warnings.append("Signature removed")
            break

        if line.strip():
            cleaned_lines.append(line.strip())

    cleaned_text = " ".join(cleaned_lines)

    return cleaned_text, warnings
