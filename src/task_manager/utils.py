# src/task_manager/utils.py
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Task:
    """Represents a task with optional due date and completion status."""

    title: str
    priority: int = 1  # 1 (low) - 5 (high)
    due_date: Optional[date] = None
    completed: bool = False
