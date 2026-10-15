try:
    from .models import Task
except ImportError:
    from models import Task


class InfeasiblePlan(Exception):
    """Ngoại lệ ném ra khi tổng thời gian cần thiết vượt quá thời gian khả dụng."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        super().__init__()
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self) -> str:
        return (
            f"Kế hoạch bất khả thi: cần {self.needed_h:.1f} giờ, "
            f"nhưng chỉ có sẵn {self.available_h:.1f} giờ."
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Kiểm tra tính khả thi của kế hoạch.

    Ném InfeasiblePlan nếu needed_h > available_h.
    """
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)


if __name__ == "__main__":
    from datetime import date

    sample_tasks = [
        Task(title="Ôn tập OS", importance=5, effort_h=8.0, deadline=date(2026, 10, 30)),
        Task(title="Làm bài tập Git", importance=4, effort_h=3.0, deadline=date(2026, 10, 27)),
    ]

    print("Kiểm tra 1 (available_h = 15h - Đủ thời gian):")
    try:
        check_feasible(sample_tasks, available_h=15.0)
        print("-> Kế hoạch hợp lệ, hoàn thành tốt!\n")
    except InfeasiblePlan as err:
        print(f"-> Lỗi: {err}\n")

    print("Kiểm tra 2 (available_h = 5h - Không đủ thời gian):")
    try:
        check_feasible(sample_tasks, available_h=5.0)
        print("-> Kế hoạch hợp lệ!\n")
    except InfeasiblePlan as err:
        print(f"-> Bắt được ngoại lệ thành công: {err}\n")