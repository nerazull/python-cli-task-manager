from task_manager.task import Task
from task_manager.storage import save_tasks, load_tasks

class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = tasks if tasks is not None else load_tasks()

    def add_task_from_cli(self, title):
        task = Task(title)
        self.tasks.append(task)
        save_tasks(self.tasks)
        print("✓ Task added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        
        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task.done else " "
            print(f"{index}. [{status}] {task.title}")  

    def get_task_index(self, prompt):
        try:
            task_number = int(input(prompt))
            index = task_number - 1

            if index < 0 or index >= len(self.tasks):
                print("Invalid task number.")
                return None
            
            return index
        
        except ValueError:
            print("Please enter a valid number.")
            return None
        
    def mark_task_done_from_cli(self, task_number):
        index = task_number - 1

        if index < 0 or index >= len(self.tasks):
            print("Invalid task number.")
            return
        
        self.tasks[index].done = True
        save_tasks(self.tasks)
        print("✓ Task marked as done.")

    def delete_task_from_cli(self, task_number):
        index = task_number - 1

        if index < 0 or index >= len(self.tasks):
            print("Invalid task number.")
            return
        
        deleted = self.tasks.pop(index)
        save_tasks(self.tasks)
        print(f"✓ Deleted task: {deleted.title}")