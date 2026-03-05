from task_manager.task import Task
from task_manager.storage import save_tasks, load_tasks
from datetime import date


PRIORITY_ORDER = {"high": 3, "medium": 2, "low": 1}


class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = tasks if tasks is not None else load_tasks()

    def add_task_from_cli(self, title, priority, due_date=None):
        task = Task(title=title, priority=priority, due_date=due_date)
        self.tasks.append(task)
        save_tasks(self.tasks)
        print(f"✓ Task added with priority '{priority}'.")

    def get_sorted_tasks(self):
        return sorted(self.tasks, key=lambda task: PRIORITY_ORDER.get(task.priority, 2), reverse=True)

    def list_tasks(self, priority_filter=None):
        visible_tasks = self.get_visible_tasks(priority_filter)
        
        if not visible_tasks:
            print("No tasks found.")
            return
        
        for index, task in enumerate(visible_tasks, start=1):
            status = "✓" if task.done else " "
            due_info = f" - Due: {task.due_date}" if task.due_date else ""
            print(f"{index}. [{status}] {task.title} ({task.priority}){due_info}")

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
        
    def mark_task_done_from_cli(self, index):
        visible_tasks = self.get_visible_tasks()

        try:
            task = visible_tasks[index - 1]
            task.done = True
            save_tasks(self.tasks)
            print("Task marked as done.")
        except IndexError:
            print("Invalid task index.")

    def delete_task_from_cli(self, index, force=False):
        visible_tasks = self.get_visible_tasks()
        
        try:
            task_to_delete = visible_tasks[index - 1]

            if not force:
                if not self._confirm_action(f" Delete task '{task_to_delete.title}'?"):
                    print("Deletion cancelled.")
                    return
                
            self.tasks.remove(task_to_delete)
            save_tasks(self.tasks)
            print("Task deleted successfully.")

        except IndexError:
            print("Invalid task index.")

    def clear_tasks(self, force=False):
        if not self.tasks:
            print("No tasks to clear.")
            return
        
        if not force:
            if not self._confirm_action("Clear ALL tasks?"):
                print("Clear cancelled.")
                return
        
        self.tasks.clear()
        save_tasks(self.tasks)
        print("All tasks cleared.")

    def _confirm_action(self, message):
        response = input(f"{message} (y/N): ").strip().lower()
        return response == "y"
    
    def get_visible_tasks(self, priority_filter=None):
        filtered_tasks = self.tasks

        if priority_filter:
            filtered_tasks = [task for task in self.tasks if task.priority == priority_filter]

        return sorted(filtered_tasks, key=lambda task: PRIORITY_ORDER.get(task.priority, 2), reverse=True)
        
    def show_stats(self):
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.done)
        pending = total - completed

        high = sum(1 for task in self.tasks if task.priority == "high")
        medium = sum(1 for task in self.tasks if task.priority == "medium")
        low = sum(1 for task in self.tasks if task.priority == "low")

        today = date.today().isoformat()
        overdue = sum(1 for task in self.tasks if task.due_date and task.due_date < today and not task.done)

        print(f"Total tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")
        print(f"High priority: {high}")
        print(f"Medium priority: {medium}")
        print(f"Low priority: {low}")
        print(f"Overdue: {overdue}")
