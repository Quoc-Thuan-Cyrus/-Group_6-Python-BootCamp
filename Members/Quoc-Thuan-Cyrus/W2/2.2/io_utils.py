import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path
from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    tasks: list[Task] = []
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for line_num, row in enumerate(reader, start=2):
            try:
                title = row["title"].strip()
                if not title:
                    raise ValueError("Empty title")
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"].strip())
                tasks.append(Task(title, importance, effort_h, deadline))
            except (ValueError, TypeError, KeyError) as e:
                raise ValueError(f"Invalid row at line {line_num}: {e}") from e
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    data = []
    for task in tasks:
        item = asdict(task)
        item["deadline"] = task.deadline.isoformat()
        data.append(item)
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
