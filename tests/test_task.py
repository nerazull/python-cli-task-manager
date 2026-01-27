from task_manager.task import Task


def test_task_initial_state():
    task = Task("Test task")

    assert task.title == "Test task"
    assert task.done is False