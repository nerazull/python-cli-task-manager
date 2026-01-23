def show_menu():
        menu = [
            "Task Manager",
            "1. Add task",
            "2. List tasks",
            "3. Mark task as done",
            "4. Delete task",
            "5. Exit"
        ]

        print("\n".join(menu))  


def add_task(tasks):
    title = input("Enter task title: ")
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    print("Task added.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{index}. [{status}] {task["title"]}")  


def get_task_index(prompt, tasks):
    try:
        task_number = int(input(prompt))
        index = task_number - 1

        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            return None
        
        return index
    
    except ValueError:
        print("Please enter a valid number.")
        return None


def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark.")
        return
    
    list_tasks(tasks)

    index = get_task_index("Enter task number to mark as done: ")
    if index is None:
        return
        
    tasks[index]["done"] = True
    print("Task marked as done.")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    
    list_tasks(tasks)

    index = get_task_index("Enter task number to mark as done: ")
    if index is None:
        return

    deleted_task = tasks.pop(index)
    print(f"Deleted task: {deleted_task["title"]}")


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()