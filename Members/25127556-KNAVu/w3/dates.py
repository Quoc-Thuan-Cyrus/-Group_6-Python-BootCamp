from datetime import date, timedelta
def parse_due(text: str, today: date) -> date:
    text_lower = text.strip().lower()
    try:
        return date.fromisoformat(text_lower)
    except ValueError:
        pass
    if text_lower == "tomorrow":
        return today + timedelta(days=1)
    if text_lower.startswith("in ") and text_lower.endswith(" days"):
        parts = text_lower.split()
        if len(parts) == 3 and parts[1].isdigit():
            return today + timedelta(days=int(parts[1]))
    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    for idx, day_str in enumerate(weekdays):
        if text_lower.startswith(day_str):
            days_ahead = (idx - today.weekday()) % 7
            if days_ahead == 0:
                days_ahead = 7
            return today + timedelta(days=days_ahead)
    raise ValueError(f"Unknown date format: '{text}'")
