from datetime import date
from shared.contract import Task

def prioritise(tasks: list[Task], today: date) -> list[Task]:
    """
    Sắp xếp danh sách Task giảm dần theo công thức: importance / days_left
    """
    def calculate_priority(task: Task) -> float:
        days_left = (task.deadline - today).days
        # Nếu deadline hôm nay hoặc đã qua hạn, lấy days_left = 1 để không bị chia cho 0
        if days_left <= 0:
            days_left = 1
        return task.importance / days_left

    # Sắp xếp giảm dần theo điểm ưu tiên
    return sorted(tasks, key=calculate_priority, reverse=True)