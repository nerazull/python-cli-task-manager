# Python CLI Task Manager

## Description

A simple command-line task manager written in Python.  
The project allows users to add, list, complete, and delete tasks, with tasks persisted between runs using a JSON file.

This project is built as a beginner-friendly side project to practice Python fundamentals, clean code, testing, and project structure.

## Features

- Add new tasks
- List existing tasks
- Mark tasks as completed
- Delete tasks
- Persistent storage using JSON
- Simple and clean CLI interface
- Basic unit tests using pytest

## Requirements

- Python 3.10+
- pytest (for running tests)

## How to Run

Clone the repository and run the application from the project root:

```bash python main.py```

Run tests with:

```pytest```

## 🗂 Project Structure

```markdown
task_manager/
├── task.py          # Task model
├── task_manager.py  # Core task logic
├── storage.py       # JSON persistence
tests/
├── test_task.py
├── test_task_manager.py
main.py              # Application entry point
```
## 🧠 What I Learned

- Python basics and OOP concepts
- Separating logic into modules
- Using JSON for simple persistence
- Writing basic unit tests with pytest
- Structuring a Python project
- Handling user input safely
- Using Git with small, meaningful commits

## Possible Improvements

- [x] Add command-line arguments using argparse
- [x] Add task priorities and due dates
- [ ] Improve test coverage
- [x] Add confirmation prompts for destructive actions
- [ ] Package the project for installation
