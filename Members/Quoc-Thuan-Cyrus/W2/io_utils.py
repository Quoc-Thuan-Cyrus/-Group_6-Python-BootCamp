import csv
import json
from datetime import datetime
from models import Task # Assuming Task is saved in models.py from the previous step

def load_tasks(path: str) -> list[Task]:
    tasks = []
    with open(path, mode='r', encoding='utf-8') as f:
        # Using DictReader automatically handles the expected header 
        # title,importance,effort_h,deadline
        reader = csv.DictReader(f)
        
        # start=2 because line 1 is the header
        for line_num, row in enumerate(reader, start=2):
            try:
                title = row['title']
                importance = int(row['importance'])
                effort_h = float(row['effort_h'])
                deadline = datetime.strptime(row['deadline'], "%Y-%m-%d").date()
                
                # The Task dataclass __post_init__ will also raise a ValueError 
                # if importance is not between 1-5
                task = Task(title, importance, effort_h, deadline)
                tasks.append(task)
            except (ValueError, KeyError) as e:
                # Raise ValueError with the line number for any invalid rows
                raise ValueError(f"Invalid row at line {line_num}: {e}")
                
    return tasks

def save_json(tasks: list[Task], path: str):
    tasks_data = []
    for task in tasks:
        tasks_data.append({
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat() # Convert date to string for JSON
        })
        
    with open(path, mode='w', encoding='utf-8') as f:
        json.dump(tasks_data, f, indent=4)