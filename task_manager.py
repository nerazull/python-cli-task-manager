from task import Task
from storage import save_tasks, load_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self):
        title = input("Enter task title: ")
        task = Task(title)
        self.tasks.append(task)
        save_tasks(self.tasks)
        print("Task added.")

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
        
    def mark_task_done(self):
        if not self.tasks:
            print("No tasks to mark.")
            return
        
        self.list_tasks()

        index = self.get_task_index("Enter task number to mark as done: ")
        if index is None:
            return
            
        self.tasks[index].done = True
        save_tasks(self.tasks)
        print("Task marked as done.")

    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete.")
            return
        
        self.list_tasks()

        index = self.get_task_index("Enter task number to mark as done: ")
        if index is None:
            return

        deleted_task = self.tasks.pop(index)
        save_tasks(self.tasks)
        print(f"Deleted task: {deleted_task.title}")