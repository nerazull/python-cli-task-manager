from task_manager import TaskManager


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


def main():
    task_manager = TaskManager()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.list_tasks()
        elif choice == "3":
            task_manager.mark_task_done()
        elif choice == "4":
            task_manager.delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()