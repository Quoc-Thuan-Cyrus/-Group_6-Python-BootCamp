import os
from .io_utils import load_tasks


def main():
    csv_path = os.path.join(os.path.dirname(__file__), "sample.csv")
    tasks = load_tasks(csv_path)
    print(f"Loaded {len(tasks)} tasks:")
    for task in tasks:
        print(
            f" - {task.title} (Importance: {task.importance}, Effort: {task.effort_h}h, Deadline: {task.deadline})"
        )


if __name__ == "__main__":
    main()