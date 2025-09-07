# Task Manager

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Task Manager** is a Python library to manage tasks with priorities and due dates.

---

## Features

- Add, list, and complete tasks
- Persist tasks in JSON
- Optimized lookup by title
- Optional sorting by priority or due date
- Fully typed and tested
- Linting and formatting with Flake8 & Black
- CI/CD ready

---

## Installation

```powershell
git clone https://github.com/your-username/task-manager.git
cd task-manager
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
pip install pytest black flake8 mypy
```

---

## Usage

```powershell
from task_manager import TaskManager, Task
from datetime import date

manager = TaskManager()
task = Task(title="Finish project", priority=5, due_date=date.today())
manager.add_task(task)

tasks = manager.list_tasks(sort_by_priority=True)
for t in tasks:
    print(t)
```

---

## Testing

```powershell
pytest -v
python -m mypy src
black --check src tests
flake8 src tests
```

---

## License

MIT License © 2025 André Luiz. See the LICENSE file for details.