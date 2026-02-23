class TodoCLI:
    def __init__(self, service):
        self.service = service

    def run(self):
        print("To-Do List App")
        while True:
            command = input("> ")
            if command == "add":
                task = input("Task: ")
                self.service.add_task(task)
            elif command == "list":
                tasks = self.service.get_all_tasks()
                if not tasks:
                    print("Belum ada task.")
                else:
                    for i, task in enumerate(tasks):
                        print(f"{i+1}. {task}")
            elif command == "exit":
                break
            else:
                print("Command tidak dikenal. Gunakan: add, list, exit")