from task_manager.task_manager import TaskManager
import argparse


def main():
    parser = argparse.ArgumentParser(description="Simple CLI Task Manager")

    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.add_argument("--priority", choices=["low", "medium", "high"], default="medium", help="Task priority")
    add_parser.add_argument("--due", help="Due date in format YYYY-MM-DD")

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--priority", choices=["low", "medium", "high"], help="Filter by priority")

    # Done command
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("index", type=int, help="Task number")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("index", type=int, help="Task number")
    delete_parser.add_argument("--force", action="store_true", help="Delete without confirmation")

    # Clear command
    clear_parser = subparsers.add_parser("clear", help="Clear all tasks")
    clear_parser.add_argument("--force", action="store_true", help="Clear all tasks without confirmation")

    args = parser.parse_args()

    task_manager = TaskManager()

    if args.command == "add":
        task_manager.add_task_from_cli(args.title, args.priority, due_date=args.due)
    elif args.command == "list":
        task_manager.list_tasks(priority_filter=args.priority)
    elif args.command == "done":
        task_manager.mark_task_done_from_cli(args.index)
    elif args.command == "delete":
        task_manager.delete_task_from_cli(args.index, force=args.force)
    elif args.command == "clear":
        task_manager.clear_tasks(force=args.force)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()