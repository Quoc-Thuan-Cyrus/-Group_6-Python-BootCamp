def by_day(timetable):
    result = {}
    for course, day in timetable:
        result.setdefault(day, []).append(course)
    
    # Sắp xếp danh sách môn học cho từng ngày
    for day, value in result.items():
        value.sort()
        
    return result


# Kiểm thử theo ví dụ trong đề bài
if __name__ == "__main__":
    data = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]
    print(by_day(data))
    # Output: {'Mon': ['CSC10001', 'CSC10014'], 'Tue': ['MTH00003']}