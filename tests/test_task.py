from task_manager.task import Task


def test_task_initial_state():
    task = Task("Test task")

    assert task.title == "Test task"
    assert task.done is False


def test_task_default_priority():
    task = Task("Test")
    assert task.priority == "medium"


def test_task_custom_priority():
    task = Task("Test", priority="high")
    assert task.priority == "high"


def test_task_default_due_date():
    task = Task("Test")
    assert task.due_date is None


def test_task_with_due_date():
    task = Task("Test", due_date="2026-02-20")
    assert task.due_date == "2026-02-20"