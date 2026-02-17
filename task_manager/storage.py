import json
import os
from task_manager.task import Task


DATA_DIR = "data"
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")


def save_tasks(tasks):
    os.makedirs(DATA_DIR, exist_ok=True)

    data = []
    for task in tasks:
        data.append({
            "title": task.title,
            "done": task.done,
            "priority": task.priority,
            "due_date": task.due_date
        })

    with open(TASKS_FILE, "w") as file:
        json.dump(data, file, indent=2)


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    
    try:
        with open(TASKS_FILE, "r") as file:
            data = json.load(file)

        tasks = []
        for item in data:
            priority = item.get("priority", "medium")
            due_date = item.get("due_date")

            task = Task(title=item["title"], priority=priority, done=item.get("done", False), due_date=due_date)
            tasks.append(task)

        return tasks
    
    except (json.JSONDecodeError, KeyError):
        print("Warning: tasks file is corrupted. Starting fresh.")
        return []