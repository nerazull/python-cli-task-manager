from task_manager.task import Task
from task_manager.task_manager import TaskManager


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

    manager.tasks.pop(0)

    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Task 2"