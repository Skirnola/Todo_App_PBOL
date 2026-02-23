class TodoService:
    def __init__(self, repository):
        self.repository = repository

    def add_task(self, task):
        if not task.strip():
            print("Task tidak boleh kosong!")
            return
        self.repository.add(task)
        print(f"Added: {task}")

    def get_all_tasks(self):
        return self.repository.get_all()