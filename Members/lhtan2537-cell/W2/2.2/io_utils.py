import csv
import json
from datetime import date

try:
    from .models import Task
except ImportError:
    from models import Task

def load_tasks(path: str) -> list[Task]:
    """Đọc file CSV và trả về danh sách các đối tượng Task.

    Ném ValueError kèm số dòng nếu dữ liệu không hợp lệ.
    """
    tasks = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)

        for line_num, row in enumerate(reader, start=2):
            if not row:
                continue

            if len(row) != 4:
                raise ValueError(
                    f"Invalid column count at line {line_num}: expected 4, got {len(row)}"
                )

            title = row[0].strip()
            try:
                importance = int(row[1].strip())
                effort_h = float(row[2].strip())
                deadline = date.fromisoformat(row[3].strip())

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)
            except Exception as e:
                raise ValueError(f"Invalid data at line {line_num}: {e}") from e

    return tasks


def save_json(tasks: list[Task], path: str) -> None:
    """Lưu danh sách đối tượng Task vào file JSON."""
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)



if __name__ == "__main__":

    sample_csv_content = """title,importance,effort_h,deadline
OS exam,5,8,2026-10-30
Assignment,4,1.5,2026-10-27
"""
    with open("test_tasks.csv", "w", encoding="utf-8") as f:
        f.write(sample_csv_content)

    loaded = load_tasks("test_tasks.csv")
    print(f"Loaded successfully {len(loaded)} tasks:")
    for item in loaded:
        print(f" - {item.title}: {item.effort_h}h (Importance: {item.importance})")

    save_json(loaded, "test_tasks.json")
    print("Saved to test_tasks.json successfully!")
