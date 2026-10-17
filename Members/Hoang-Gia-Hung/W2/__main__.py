"""W2-5: Entry point — python -m Members.Hoang-Gia-Hung.W2

Loads the sample CSV and prints all tasks with days_left.
"""

from datetime import date
from pathlib import Path

from . import load_tasks, check_feasible, InfeasiblePlan

CSV_PATH = Path(__file__).parent / "sample_tasks.csv"
AVAILABLE_H = 10.0


def main() -> None:
    tasks = load_tasks(CSV_PATH)
    today = date.today()

    print(f"{'Title':<20} {'Importance':>10} {'Effort (h)':>10} {'Deadline':>12} {'Days left':>10}")
    print("-" * 66)
    for task in tasks:
        print(
            f"{task.title:<20} {task.importance:>10} {task.effort_h:>10.1f} "
            f"{task.deadline.isoformat():>12} {task.days_left(today):>10}"
        )

    print()
    try:
        check_feasible(tasks, AVAILABLE_H)
        print(f"Plan is feasible within {AVAILABLE_H} h available.")
    except InfeasiblePlan as e:
        print(e)


if __name__ == "__main__":
    main()
