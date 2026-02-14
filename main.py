from task_manager.task_manager import TaskManager
import argparse


def show_menu():
    print("\n" + "=" * 20)
    print(" Task Manager ")
    print("=" * 20)
    print("1) Add task")
    print("2) List tasks")
    print("3) Mark task as done")
    print("4) Delete task")
    print("5) Exit")


def main():
    parser = argparse.ArgumentParser(description="Simple CLI Task Manager")

    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Done command
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("index", type=int, help="Task number")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("index", type=int, help="Task number")

    args = parser.parse_args()

    task_manager = TaskManager()

    if args.command == "add":
        task_manager.add_task_from_cli(args.title)
    elif args.command == "list":
        task_manager.list_tasks()
    elif args.command == "done":
        task_manager.mark_task_done_from_cli(args.index)
    elif args.command == "delete":
        task_manager.delete_task_from_cli(args.index)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()