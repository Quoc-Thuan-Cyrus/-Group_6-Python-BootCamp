"""W2-3: Custom exception and feasibility check."""

from .models import Task


class InfeasiblePlan(Exception):
    """Raised when the total effort of tasks exceeds available hours.

    Attributes:
        needed_h: Total effort hours required by all tasks.
        available_h: Total hours available.
    """

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Plan is infeasible: need {self.needed_h:.1f} h "
            f"but only {self.available_h:.1f} h available "
            f"(short by {self.needed_h - self.available_h:.1f} h)."
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Check whether the total effort of tasks fits within available_h.

    Args:
        tasks: List of Task objects.
        available_h: Total hours available.

    Raises:
        InfeasiblePlan: If the sum of effort_h exceeds available_h.
    """
    needed_h = sum(t.effort_h for t in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)


if __name__ == "__main__":
    from datetime import date
    from .models import Task

    tasks = [Task("DS exam", 5, 6.0, date(2026, 10, 30)),
             Task("Assignment", 4, 1.5, date(2026, 10, 27))]
    try:
        check_feasible(tasks, 5.0)
    except InfeasiblePlan as e:
        print(e)
