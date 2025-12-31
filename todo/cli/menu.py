"""Menu display and user interaction for the Todo application."""

from typing import Optional, List

from todo.models.task import Task, TaskStatus


class Menu:
    """Menu class for displaying options and task lists."""

    WIDTH_ID = 3
    WIDTH_STATUS = 12
    WIDTH_PRIORITY = 8
    WIDTH_DUE = 20
    WIDTH_CONTENT = 40
    WIDTH_TAGS = 20

    def display_menu(self) -> None:
        """Print the main menu options."""
        print("\n=== Todo Application (Advanced Level) ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task Content")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Set Due Date/Time")
        print("8. Set Priority")
        print("9. Manage Tags")
        print("10. Search Tasks")
        print("11. Filter Tasks")
        print("12. Sort Tasks")
        print("13. View Reminders (Overdue)")
        print("14. Set Recurrence")
        print("15. Exit")
        print("===========================================")

    def display_tasks(self, tasks: List[Task], title: str = "Tasks") -> None:
        """Format and display tasks as a table."""
        if not tasks:
            print(f"\nNo tasks found for: {title}")
            return

        print(f"\n--- {title} ---")
        header = (
            f"{'ID':<{self.WIDTH_ID}} | {'Status':<{self.WIDTH_STATUS}} | "
            f"{'Priority':<{self.WIDTH_PRIORITY}} | {'Due Date/Time':<{self.WIDTH_DUE}} | "
            f"{'Task':<{self.WIDTH_CONTENT}} | {'Tags'}"
        )
        print(header)
        print("-" * (len(header) + self.WIDTH_TAGS))

        for task in tasks:
            status_icon = "[x]" if task.status == TaskStatus.COMPLETE else "[ ]"
            status_text = "Complete" if task.status == TaskStatus.COMPLETE else "Incomplete"

            # Format due date with recurrence
            due_val = task.due_date.strftime("%Y-%m-%d %H:%M") if task.due_date else "None"
            if task.recurrence != "none":
                due_val += f" ({task.recurrence.value[0]})" # Show first letter (d/w/m)

            # Truncate content
            display_content = task.content
            if len(display_content) > self.WIDTH_CONTENT:
                display_content = display_content[:self.WIDTH_CONTENT-3] + "..."

            # Format row
            row = (
                f"{task.id:<{self.WIDTH_ID}} | {status_icon} {status_text:<{self.WIDTH_STATUS-4}} | "
                f"{task.priority.upper():<{self.WIDTH_PRIORITY}} | "
                f"{due_val:<{self.WIDTH_DUE}} | "
                f"{display_content:<{self.WIDTH_CONTENT}} | "
                f"{', '.join(task.tags) if task.tags else 'None'}"
            )
            print(row)

    def display_reminders(self, overdue_tasks: List[Task]) -> None:
        """Display a summary of overdue tasks as a reminder."""
        if not overdue_tasks:
            return

        print("\n" + "!" * 43)
        print(f"!!! REMINDER: YOU HAVE {len(overdue_tasks)} OVERDUE TASKS !!!")
        print("!" * 43)
        for t in overdue_tasks:
            due = t.due_date.strftime("%Y-%m-%d %H:%M") if t.due_date else "N/A"
            print(f"- [ID: {t.id}] {t.content} (Due: {due})")
        print("!" * 43)

    def display_message(self, message: str) -> None:
        print(message)

    def display_error(self, error: Exception) -> None:
        print(f"Error: {error}")

    def display_success(self, message: str) -> None:
        print(f"Success: {message}")

    def display_welcome(self) -> None:
        print("=" * 50)
        print("       Welcome to Todo Application")
        print("=" * 50)
        print("Advanced features enabled: Recurring Tasks, Datetime Recurrence, Overdue Reminders.")

    def display_goodbye(self) -> None:
        print("\nExiting. Data lost on exit. Goodbye!")

    def display_task_added(self, task: Task) -> None:
        print(f"Task added successfully! (ID: {task.id})")

    def display_task_updated(self, task: Task) -> None:
        print(f"Task {task.id} updated successfully.")

    def display_task_deleted(self, task_id: int) -> None:
        print(f"Task {task_id} deleted successfully.")

    def display_task_status_changed(self, task: Task, action: str) -> None:
        print(f"Task {task.id} {action}.")
