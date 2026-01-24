# Email-Summarizer

A rule-based email summarization project built in Python.

This project takes raw email text, validates it, cleans it, extracts useful information
(summary bullets, action items, urgency, deadlines), and returns a structured output.
It is designed like a real product pipeline, not a single script.

---

## What this project does

Given an email, the system:

1. Validates the input (type, length, basic language checks)
2. Cleans the email (removes signatures, reply chains, extra noise)
3. Summarizes the email into bullet points
4. Extracts:
   - action items
   - urgency level
   - deadlines (rule-based)
5. Logs what happened
6. Returns a predictable output structure

---

## Project Structure

Email-Summarizer/
│
├── main.py           # Entry point and pipeline orchestration
├── validators.py     # Input validation rules
├── cleaner.py        # Email cleaning logic
├── summarizer.py     # Rule-based summarization and extraction
├── schema.py         # Output structure contract
├── config.py         # System rules and limits
├── logger.py         # Logging and observability
├── tests/
│   ├── __init__.py
│   └── test_basic.py # Basic unit tests
├── README.md
└── .gitignore

---

## How to run the project

From the project root:

python main.py

Paste an email when prompted and the system will return a structured result.

---

## How to run tests

From the project root:

python -m unittest tests.test_basic

or (if running directly):

python tests/test_basic.py

---

## Example Output

{
  "summary_bullets": [...],
  "action_items": [...],
  "deadlines": [...],
  "urgency": "low | medium | high",
  "warnings": [...]
}

---

## Design Philosophy

- Rule-based before AI
- Validation before processing
- Deterministic, explainable behavior
- Product-like file separation
- Easy to extend with real AI later

---

## Notes

This is a learning project focused on:
- Python fundamentals
- system design
- validation and constraints
- testable code
- context-engineering mindset

---

## Future Improvements

- Replace rule-based summarizer with an LLM
- Better deadline parsing
- Improved email language detection
- Web or API interface

---

Built as a learning project.
