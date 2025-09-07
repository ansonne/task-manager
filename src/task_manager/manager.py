# src/task_manager/manager.py
from __future__ import annotations
from typing import List, Optional, Dict
from pathlib import Path
from datetime import date
import json

from .utils import Task


class TaskManager:
    """Manages tasks with optimized lookup and JSON persistence."""

    def __init__(self, storage_file: str = "tasks.json") -> None:
        self.storage_file: Path = Path(storage_file)
        self.tasks: Dict[str, Task] = {}  # optimized lookup by title
        self.load()

    def add_task(self, task: Task) -> None:
        """Add or overwrite a task by title."""
        self.tasks[task.title] = task
        self.save()

    def list_tasks(
        self,
        completed: Optional[bool] = None,
        sort_by_priority: bool = False,
        sort_by_due_date: bool = False,
    ) -> List[Task]:
        """Return tasks optionally filtered and sorted."""
        tasks = list(self.tasks.values())
        if completed is not None:
            tasks = [t for t in tasks if t.completed == completed]
        if sort_by_priority:
            tasks.sort(key=lambda t: t.priority, reverse=True)
        if sort_by_due_date:
            tasks.sort(key=lambda t: t.due_date or date.max)
        return tasks

    def complete_task(self, title: str) -> bool:
        """Mark a task as completed. Returns True if task exists."""
        task = self.tasks.get(title)
        if task:
            task.completed = True
            self.save()
            return True
        return False

    def save(self) -> None:
        """Persist tasks to JSON file."""
        data = [
            {
                "title": t.title,
                "priority": t.priority,
                "due_date": t.due_date.isoformat() if t.due_date else None,
                "completed": t.completed,
            }
            for t in self.tasks.values()
        ]
        try:
            self.storage_file.write_text(json.dumps(data, indent=4))
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def load(self) -> None:
        """Load tasks from JSON file safely."""
        if self.storage_file.exists():
            try:
                data = json.loads(self.storage_file.read_text())
                self.tasks = {
                    t["title"]: Task(
                        title=t["title"],
                        priority=int(t.get("priority", 1)),
                        due_date=(
                            date.fromisoformat(t["due_date"])
                            if t.get("due_date")
                            else None
                        ),
                        completed=bool(t.get("completed", False)),
                    )
                    for t in data
                }
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading tasks, starting empty: {e}")
                self.tasks = {}
