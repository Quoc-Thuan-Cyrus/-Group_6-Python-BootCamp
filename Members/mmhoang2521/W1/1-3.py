def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    reasons = []

    if credits < 120:
        needed_credits = 120 - credits
        reasons.append(f"need {needed_credits} more credits")

    if gpa < 2.0:
        reasons.append("GPA must be at least 2.0")

    return reasons


# Kiểm thử
if __name__ == "__main__":
    print(can_register_thesis(118, 2.5))  # Output: False
    print(missing(118, 2.5))  # Output: ['need 2 more credits']

    print(can_register_thesis(125, 3.2))  # Output: True
    print(missing(125, 3.2))  # Output: []