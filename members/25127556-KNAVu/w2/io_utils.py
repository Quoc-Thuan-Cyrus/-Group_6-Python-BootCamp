import csv
import json
from datetime import date
from typing import List

# Import Task từ file models.py trong cùng thư mục
from .models import Task

def load_tasks(path: str) -> List[Task]:
    tasks = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_num, row in enumerate(reader, start=2):
            try:
                title = row["title"].strip()
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"].strip())
                tasks.append(
                    Task(
                        title=title,
                        importance=importance,
                        effort_h=effort_h,
                        deadline=deadline,
                    )
                )
            except Exception as e:
                raise ValueError(f"Error on line {line_num}: {e}")
    return tasks


def save_json(tasks: List[Task], path: str) -> None:
    data = []
    for t in tasks:
        data.append(
            {
                "title": t.title,
                "importance": t.importance,
                "effort_h": t.effort_h,
                "deadline": t.deadline.isoformat(),
            }
        )

    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)