import sys
from datetime import datetime
from core.manager import TaskManager
from core.engine import search_tasks, filter_tasks, sort_tasks
from utils.validators import validate_date, validate_priority

class TodoApp:
    def __init__(self):
        self.manager = TaskManager()

    def display_menu(self):
        print("\n=== Evolution of Todo (Intermediate Phase I) ===")
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Toggle Task Status")
        print("6. Search Tasks")
        print("7. Filter Tasks")
        print("8. Sort Tasks")
        print("9. Exit")
        print("================================================")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-9): ").strip()

            if choice == '1':
                self.ui_add_task()
            elif choice == '2':
                self.ui_list_tasks(self.manager.get_all_tasks())
            elif choice == '3':
                self.ui_update_task()
            elif choice == '4':
                self.ui_delete_task()
            elif choice == '5':
                self.ui_toggle_status()
            elif choice == '6':
                self.ui_search_tasks()
            elif choice == '7':
                self.ui_filter_tasks()
            elif choice == '8':
                self.ui_sort_tasks()
            elif choice == '9':
                print("Exiting. Data will be lost.")
                sys.exit(0)
            else:
                print("Invalid choice. Please enter 1-9.")

    def ui_add_task(self):
        content = input("Enter task description: ").strip()
        if not content:
            print("Error: Task description cannot be empty.")
            return

        due_date_str = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
        try:
            due_date = validate_date(due_date_str)
        except ValueError as e:
            print(f"Error: {e}")
            return

        priority = input("Enter priority (high/medium/low) [medium]: ").strip() or "medium"
        try:
            priority = validate_priority(priority)
        except ValueError as e:
            print(f"Error: {e}")
            return

        tags_str = input("Enter tags (comma-separated): ").strip()
        tags = self.manager.parse_tags(tags_str)

        self.manager.add_task(content, due_date, priority, tags)
        print("Task added successfully.")

    def ui_list_tasks(self, tasks):
        if not tasks:
            print("\nNo tasks to display.")
            return

        print(f"\n{'ID':<4} | {'Status':<12} | {'Priority':<8} | {'Due Date':<12} | {'Content':<30} | {'Tags'}")
        print("-" * 100)
        for t in tasks:
            due_date = str(t.due_date) if t.due_date else "None"
            tags = ", ".join(t.tags) if t.tags else "None"
            status = f"[{'X' if t.status == 'complete' else ' '}] {t.status}"
            print(f"{t.id:<4} | {status:<12} | {t.priority:<8} | {due_date:<12} | {t.content:<30} | {tags}")

    def ui_update_task(self):
        try:
            task_id = int(input("Enter task ID to update: ").strip())
        except ValueError:
            print("Error: Invalid ID.")
            return

        task = self.manager.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return

        print(f"Updating Task {task_id}. Leave blank to keep current value.")

        new_content = input(f"Content [{task.content}]: ").strip()
        if new_content:
            task.content = new_content

        new_date_str = input(f"Due Date [{task.due_date}]: ").strip()
        if new_date_str:
            try:
                task.due_date = validate_date(new_date_str)
            except ValueError as e:
                print(f"Error: {e}")
                return

        new_priority = input(f"Priority [{task.priority}]: ").strip()
        if new_priority:
            try:
                task.priority = validate_priority(new_priority)
            except ValueError as e:
                print(f"Error: {e}")
                return

        new_tags_str = input(f"Tags [{', '.join(task.tags)}]: ").strip()
        if new_tags_str:
            task.tags = self.manager.parse_tags(new_tags_str)

        task.updated_at = datetime.now()
        print("Task updated successfully.")

    def ui_delete_task(self):
        try:
            task_id = int(input("Enter task ID to delete: ").strip())
        except ValueError:
            print("Error: Invalid ID.")
            return

        if self.manager.delete_task(task_id):
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Error: Task {task_id} not found.")

    def ui_toggle_status(self):
        try:
            task_id = int(input("Enter task ID to toggle status: ").strip())
        except ValueError:
            print("Error: Invalid ID.")
            return

        task = self.manager.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task {task_id} not found.")
            return

        task.status = "complete" if task.status == "incomplete" else "incomplete"
        task.updated_at = datetime.now()
        print(f"Task {task_id} is now {task.status}.")

    def ui_search_tasks(self):
        keyword = input("Enter keyword to search (in content or tags): ").strip()
        if not keyword:
            print("Error: Search keyword cannot be empty.")
            return

        results = search_tasks(self.manager.get_all_tasks(), keyword)
        self.ui_list_tasks(results)

    def ui_filter_tasks(self):
        print("\nFilter by:")
        print("1. Status (complete/incomplete)")
        print("2. Priority (high/medium/low)")
        print("3. Tag")
        print("4. Due Date (YYYY-MM-DD)")
        print("5. Cancel")

        choice = input("Choice: ").strip()

        tasks = self.manager.get_all_tasks()
        if choice == '1':
            status = input("Enter status: ").strip().lower()
            results = filter_tasks(tasks, status=status)
        elif choice == '2':
            priority = input("Enter priority: ").strip().lower()
            results = filter_tasks(tasks, priority=priority)
        elif choice == '3':
            tag = input("Enter tag: ").strip().lower()
            results = filter_tasks(tasks, tag=tag)
        elif choice == '4':
            date_str = input("Enter date (YYYY-MM-DD): ").strip()
            try:
                d = validate_date(date_str)
                results = filter_tasks(tasks, due_date=d)
            except ValueError as e:
                print(f"Error: {e}")
                return
        elif choice == '5':
            return
        else:
            print("Invalid choice.")
            return

        self.ui_list_tasks(results)

    def ui_sort_tasks(self):
        print("\nSort by:")
        print("1. Due Date")
        print("2. Priority")
        print("3. Title (Alphabetical)")
        print("4. Creation Time")
        print("5. Cancel")

        choice = input("Choice: ").strip()

        tasks = self.manager.get_all_tasks()
        if choice == '1':
            results = sort_tasks(tasks, "due_date")
        elif choice == '2':
            results = sort_tasks(tasks, "priority")
        elif choice == '3':
            results = sort_tasks(tasks, "title")
        elif choice == '4':
            results = sort_tasks(tasks, "creation_time")
        elif choice == '5':
            return
        else:
            print("Invalid choice.")
            return

        self.ui_list_tasks(results)

if __name__ == "__main__":
    app = TodoApp()
    app.run()
