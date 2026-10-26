from pathlib import Path
from .io_utils import load_tasks

if __name__ == "__main__":
    csv_path = Path(__file__).parent / "tasks.csv"
    for task in load_tasks(csv_path):
        print(task)
