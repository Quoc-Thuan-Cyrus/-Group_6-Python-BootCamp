def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    reasons = []
    if credits < 120:
        missing_credits = 120 - credits
        reasons.append(f"need {missing_credits} more credits")
    if gpa < 2.0:
        reasons.append(f"need at least 2.0 gpa (currently {gpa})")
    return reasons