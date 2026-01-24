# tests/test_basic.py
import os
import sys
import unittest

# Add project root (parent folder) to Python path so imports work when run directly
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, PROJECT_ROOT)

from main import run
from config import MAX_CHARS


class TestEmailSummarizer(unittest.TestCase):

    def test_rejects_non_string_input(self):
        result = run(12345)
        self.assertIn("error", result)

    def test_rejects_too_short_email(self):
        short_email = "Hi"
        result = run(short_email)
        self.assertIn("error", result)

    def test_rejects_too_long_email(self):
        long_email = "a" * (MAX_CHARS + 1)
        result = run(long_email)
        self.assertIn("error", result)

    def test_valid_email_returns_schema(self):
        valid_email = (
            "Please review the document and send feedback by end of day. "
            "This is important for the deadline."
        )

        result = run(valid_email)

        self.assertIn("summary_bullets", result)
        self.assertIn("action_items", result)
        self.assertIn("deadlines", result)
        self.assertIn("urgency", result)
        self.assertIn("warnings", result)

    def test_urgency_detection(self):
        urgent_email = "This is urgent. Please respond ASAP so we can move forward."
        result = run(urgent_email)
        self.assertEqual(result["urgency"], "high")


if __name__ == "__main__":
    unittest.main()
