class Task:
    VALID_PRIORITIES = {"low", "medium", "high"}

    def __init__(self, title, *, priority="medium", done=False, due_date=None):
        if priority not in self.VALID_PRIORITIES:
            raise ValueError(f"Invalid priority: {priority}")
        
        self.title = title
        self.done = done
        self.priority = priority
        self.due_date = due_date