# tests/test_utils.py
from datetime import date
from task_manager.utils import Task


def test_task_creation() -> None:
    t = Task(title="My Task", priority=2, due_date=date.today())
    assert t.title == "My Task"
    assert t.priority == 2
    assert t.completed is False
    assert t.due_date == date.today()
