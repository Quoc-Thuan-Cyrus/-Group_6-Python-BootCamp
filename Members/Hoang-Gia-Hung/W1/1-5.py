def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    """W1-5: Given a list of (course, day) tuples, return a dict from day to a sorted list of courses."""
    result = {}
    for course, day in schedule:
        result.setdefault(day, []).append(course)

    for day in result:
        result[day].sort()

    return result


if __name__ == "__main__":
    timetable = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]
    print(by_day(timetable))
    # Expected: {'Mon': ['CSC10001', 'CSC10014'], 'Tue': ['MTH00003']}
