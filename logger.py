# logger.py
"""
Simple logging for observability.
v1 uses print; can be replaced later.
"""

from datetime import datetime


def log_event(event_type: str, message: str) -> None:
    timestamp = datetime.utcnow().isoformat()
    print(f"[{timestamp}] [{event_type.upper()}] {message}")
