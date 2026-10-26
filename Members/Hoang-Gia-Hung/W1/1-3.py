def can_register_thesis(credits: int, gpa: float) -> bool:
    """W1-3: Return True if credits >= 120 and gpa >= 2.0."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """W1-3: Return human-readable reasons if not eligible for thesis registration."""
    reasons = []
    if credits < 120:
        needed_credits = 120 - credits
        reasons.append(f"need {needed_credits} more credits")
    if gpa < 2.0:
        reasons.append("GPA must be at least 2.0")
    return reasons


if __name__ == "__main__":
    print(can_register_thesis(118, 2.5))  # False
    print(missing(118, 2.5))  # ['need 2 more credits']
    print(can_register_thesis(125, 3.2))  # True
    print(missing(125, 3.2))  # []
