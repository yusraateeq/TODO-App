from datetime import date
from typing import Optional

def validate_date(date_str: str) -> Optional[date]:
    """Validates YYYY-MM-DD format and returns a date object or None."""
    if not date_str or date_str.lower() == "none":
        return None
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def validate_priority(priority: str) -> str:
    """Validates priority level."""
    valid_priorities = ["high", "medium", "low"]
    p = priority.lower().strip()
    if p not in valid_priorities:
        raise ValueError(f"Invalid priority. Must be one of: {', '.join(valid_priorities)}")
    return p
