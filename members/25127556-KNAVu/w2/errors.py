from typing import List
from .models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Infeasible plan: needed {needed_h}h, but only {available_h}h available."
        )

    def __str__(self) -> str:
        return f"InfeasiblePlan: Required {self.needed_h}h, available {self.available_h}h."


def check_feasible(tasks: List[Task], available_h: float) -> None:
    total_needed = sum(t.effort_h for t in tasks)
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)