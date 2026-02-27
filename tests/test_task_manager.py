from task_manager.task import Task
from task_manager.task_manager import TaskManager, PRIORITY_ORDER
from unittest.mock import patch


def test_task_manager_starts_with_tasks():
    tasks = [Task("Task 1"), Task("Task 2")]
    manager = TaskManager(tasks=tasks)

    assert len(manager.tasks) == 2


def test_mark_task_done_sets_done_flag():
    task = Task("Test task")
    manager = TaskManager(tasks=[task])

    manager.tasks[0].done = True

    assert manager.tasks[0].done is True


def test_delete_task_removes_task():
    task1 = Task("Task 1")
    task2 = Task("Task 2")
    manager = TaskManager(tasks=[task1, task2])

    manager.delete_task_from_cli(1, force=True)

    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Task 2"


def test_tasks_are_sorted_by_priority():
    task1 = Task("Low task", priority="low")
    task2 = Task("High task", priority="high")
    task3 = Task("Medium task", priority="medium")

    manager = TaskManager(tasks=[task1, task2, task3])

    sorted_tasks = sorted(manager.tasks, key=lambda task: PRIORITY_ORDER.get(task.priority, 2), reverse=True)

    assert sorted_tasks[0].priority == "high"
    assert sorted_tasks[1].priority == "medium"
    assert sorted_tasks[2].priority == "low"


def test_clear_tasks():
    task1 = Task("Task 1")
    task2 = Task("Task 2")
    manager = TaskManager(tasks=[task1, task2])

    manager.clear_tasks(force=True)

    assert manager.tasks == []


def test_delete_task_with_confirmation():
    task = Task("Test")
    manager = TaskManager(tasks=[task])

    with patch("builtins.input", return_value="y"):
        manager.delete_task_from_cli(1)

    assert manager.tasks == []


def test_filter_tasks_by_priority():
    task1 = Task("Low task", priority="low")
    task2 = Task("High task", priority="high")
    task3 = Task("Another high task", priority="high")

    manager = TaskManager(tasks=[task1, task2, task3])

    filtered = [task for task in manager.tasks if task.priority == "high"]

    assert len(filtered) == 2
    assert all(task.priority == "high" for task in filtered)


def test_delete_uses_sorted_index():
    low = Task("Low", priority="low")
    high = Task("High", priority="high")

    manager = TaskManager(tasks=[low, high])

    # High should appear first when sorted
    manager.delete_task_from_cli(1, force=True)

    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Low"
