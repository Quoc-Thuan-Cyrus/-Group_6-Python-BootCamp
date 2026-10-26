import csv
from datetime import datetime
from pathlib import Path

from Shared.contract import Task


def parse_csv(path: str | Path) -> list[Task]:
    """Parse tasks from a CSV file.

    Expected CSV header: title,importance,effort_h,deadline
    """
    tasks: list[Task] = []
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    with file_path.open(mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_num, row in enumerate(reader, start=2):
            if not row or not any(row.values()):
                continue
            try:
                title = row["title"].strip()
                importance = int(row["importance"].strip())
                effort_h = float(row["effort_h"].strip())
                deadline = datetime.strptime(row["deadline"].strip(), "%Y-%m-%d").date()
                tasks.append(
                    Task(
                        title=title,
                        importance=importance,
                        effort_h=effort_h,
                        deadline=deadline,
                    )
                )
            except (KeyError, ValueError) as e:
                raise ValueError(f"Invalid row on line {line_num}: {e}") from e

    return tasks
