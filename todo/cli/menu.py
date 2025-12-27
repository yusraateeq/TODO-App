"""Menu display and user interaction for the Todo application."""

from typing import Optional

from todo.models.task import Task, TaskStatus


class Menu:
    """Menu class for displaying options and task lists."""

    WIDTH_ID = 3
    WIDTH_STATUS = 14
    WIDTH_CONTENT = 50

    def display_menu(self) -> None:
        """Print the main menu options."""
        print()
        print("=== Todo Application ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        print()

    def display_tasks(
        self, tasks: list[Task], empty_message: Optional[str] = None
    ) -> None:
        """Format and display a list of tasks.

        Args:
            tasks: List of Task objects to display.
            empty_message: Optional message to show when list is empty.
        """
        if not tasks:
            if empty_message is None:
                empty_message = "No tasks found. Add a task to get started!"
            print(empty_message)
            return

        # Calculate column widths based on content
        max_content_width = max((len(t.content) for t in tasks), default=50)
        content_width = min(max_content_width, self.WIDTH_CONTENT)

        # Print header
        header_id = "ID".center(self.WIDTH_ID)
        header_status = "Status".center(self.WIDTH_STATUS)
        header_content = "Task".center(content_width)
        print(f"{header_id} | {header_status} | {header_content}")
        print("-" * (self.WIDTH_ID + 2 + self.WIDTH_STATUS + 2 + content_width))

        # Print each task
        for task in tasks:
            status_icon = "[x]" if task.status == TaskStatus.COMPLETE else "[ ]"
            status_text = "Complete" if task.status == TaskStatus.COMPLETE else "Incomplete"

            # Truncate content if too long
            display_content = task.content
            if len(display_content) > content_width:
                display_content = display_content[: content_width - 3] + "..."

            task_id_str = str(task.id).center(self.WIDTH_ID)
            status_str = f"{status_icon} {status_text}".center(self.WIDTH_STATUS)
            content_str = display_content

            print(f"{task_id_str} | {status_str} | {content_str}")

    def display_message(self, message: str) -> None:
        """Print an informational message.

        Args:
            message: The message to display.
        """
        print(message)

    def display_error(self, error: Exception) -> None:
        """Print an error message.

        Args:
            error: The exception to display.
        """
        print(f"Error: {error}")

    def display_success(self, message: str) -> None:
        """Print a success message.

        Args:
            message: The success message to display.
        """
        print(f"Success: {message}")

    def display_welcome(self) -> None:
        """Display the welcome message."""
        print("=" * 50)
        print("       Welcome to Todo Application")
        print("=" * 50)
        print("A simple in-memory task manager")
        print()

    def display_goodbye(self) -> None:
        """Display the goodbye message."""
        print()
        print("=" * 50)
        print("     Thank you for using Todo Application")
        print("                  Goodbye!")
        print("=" * 50)

    def display_task_added(self, task: Task) -> None:
        """Display confirmation of a task being added.

        Args:
            task: The newly added task.
        """
        print(f"Task added successfully! (ID: {task.id})")

    def display_task_updated(self, task: Task) -> None:
        """Display confirmation of a task being updated.

        Args:
            task: The updated task.
        """
        print(f"Task {task.id} updated successfully.")

    def display_task_deleted(self, task_id: int) -> None:
        """Display confirmation of a task being deleted.

        Args:
            task_id: The ID of the deleted task.
        """
        print(f"Task {task_id} deleted successfully.")

    def display_task_status_changed(self, task: Task, action: str) -> None:
        """Display confirmation of task status change.

        Args:
            task: The task whose status changed.
            action: Description of the action (e.g., "marked complete").
        """
        print(f"Task {task.id} {action}.")
