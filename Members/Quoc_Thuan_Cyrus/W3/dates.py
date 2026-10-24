from datetime import date, timedelta
import re

def parse_due(text: str, today: date) -> date:
    text = text.strip()
    text_lower = text.lower()

    # 1. Exact date format (e.g., "2026-10-30")
    try:
        return date.fromisoformat(text)
    except ValueError:
        pass

    # 2. "tomorrow"
    if text_lower == "tomorrow":
        return today + timedelta(days=1)

    # 3. "in X days"
    match = re.match(r"^in\s+(\d+)\s+days$", text_lower)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    # 4. Next occurrence of a weekday (e.g., "Fri")
    weekdays = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6}
    if text_lower in weekdays:
        target_weekday = weekdays[text_lower]
        current_weekday = today.weekday()
        
        days_ahead = target_weekday - current_weekday
        if days_ahead <= 0:  # Ensures it gets the *next* occurrence 
            days_ahead += 7
            
        return today + timedelta(days=days_ahead)

    # 5. Unknown text
    raise ValueError(f"Unknown text format: '{text}'")