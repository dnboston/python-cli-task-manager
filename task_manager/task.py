class Task:
    VALID_PRIORITIES = {"low", "medium", "high"}

    def __init__(self, title, priority="medium"):
        if priority not in self.VALID_PRIORITIES:
            raise ValueError(f"Invalid priority: {priority}")
        
        self.title = title
        self.done = False
        self.priority = priority