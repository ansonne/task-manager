# tests/test_manager.py
import pytest
from pathlib import Path
from datetime import date

from task_manager.manager import TaskManager
from task_manager.utils import Task


@pytest.fixture
def task_manager(tmp_path: Path) -> TaskManager:
    storage = tmp_path / "tasks.json"
    return TaskManager(str(storage))


def test_add_and_list_tasks(task_manager: TaskManager) -> None:
    t1 = Task(title="Task 1", priority=3)
    task_manager.add_task(t1)
    tasks = task_manager.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Task 1"


def test_complete_task(task_manager: TaskManager) -> None:
    t1 = Task(title="Complete Me")
    task_manager.add_task(t1)
    result = task_manager.complete_task("Complete Me")
    assert result is True
    completed = task_manager.list_tasks(completed=True)
    assert len(completed) == 1
    assert completed[0].completed is True


def test_list_filtered_sorted(task_manager: TaskManager) -> None:
    t1 = Task(title="Task 1", completed=True, priority=2)
    t2 = Task(title="Task 2", priority=5)
    t3 = Task(title="Task 3", due_date=date.today())
    for t in [t1, t2, t3]:
        task_manager.add_task(t)

    # Filter completed
    completed = task_manager.list_tasks(completed=True)
    assert completed[0].title == "Task 1"

    # Sort by priority
    sorted_tasks = task_manager.list_tasks(sort_by_priority=True)
    assert sorted_tasks[0].priority == 5

    # Sort by due date
    sorted_by_due = task_manager.list_tasks(sort_by_due_date=True)
    assert sorted_by_due[0].due_date == date.today()
