"""W3-1: Date parsing module supporting ISO, relative, and weekday formats."""

import re
from datetime import date, timedelta

WEEKDAYS: dict[str, int] = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse a human-friendly date string into a datetime.date object.

    Supported formats:
        - ISO format: "2026-10-30"
        - Relative keyword: "tomorrow"
        - Relative offset: "in 3 days", "in 1 day"
        - Weekday name (next occurrence): "Fri", "Friday", "Mon", etc.

    Args:
        text: The date representation string.
        today: Reference base date for relative calculations.

    Returns:
        The resolved target date.

    Raises:
        ValueError: If text cannot be parsed as any supported format.
    """
    clean_text = text.strip()
    clean_lower = clean_text.lower()

    # 1. Try ISO date format (e.g. "2026-10-30")
    try:
        return date.fromisoformat(clean_text)
    except ValueError:
        pass

    # 2. "tomorrow"
    if clean_lower == "tomorrow":
        return today + timedelta(days=1)

    # 3. "in X days" / "in X day"
    match = re.match(r"^in\s+(\d+)\s+days?$", clean_lower)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    # 4. Weekday name (next occurrence)
    if clean_lower in WEEKDAYS:
        target_weekday = WEEKDAYS[clean_lower]
        days_ahead = target_weekday - today.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return today + timedelta(days=days_ahead)

    # 5. Unsupported format
    raise ValueError(f"Unknown or unsupported date format: '{text}'")
