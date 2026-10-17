"""W2-1: Task dataclass with deadline and days_left method."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represents a single task with priority, effort, and a deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def days_left(self, today: date) -> int:
        """Return the number of days remaining until the deadline.

        Never returns below 0 (returns 0 if the deadline has passed).
        """
        delta = (self.deadline - today).days
        return max(0, delta)


if __name__ == "__main__":
    from datetime import date

    task = Task("DS exam", 5, 6.0, date(2026, 10, 30))
    today = date(2026, 10, 17)
    print(task)
    print(f"Days left: {task.days_left(today)}")  # 13
