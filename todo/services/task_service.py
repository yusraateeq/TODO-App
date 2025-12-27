"""Task service for the Todo application.

This module contains the business logic for managing tasks.
"""

from datetime import datetime
from typing import Self

from todo.models.task import Task, TaskStatus
from todo.exceptions import TaskNotFoundError


class TaskService:
    """Service class for managing tasks in memory.

    Provides CRUD operations for tasks with auto-incrementing IDs.
    All data is stored in memory and lost when the application exits.
    """

    def __init__(self) -> None:
        """Initialize the task service with empty storage."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, content: str) -> Task:
        """Create a new task with auto-generated ID.

        Args:
            content: The task description (will be stripped of whitespace).

        Returns:
            The newly created Task.

        Raises:
            ValueError: If content is empty or too long.
        """
        # Validate content before creating task
        stripped_content = content.strip()
        if not stripped_content:
            raise ValueError("Task content cannot be empty")
        if len(stripped_content) > 500:
            raise ValueError("Task content cannot exceed 500 characters")

        task = Task(
            id=self._next_id,
            content=stripped_content,
            status=TaskStatus.INCOMPLETE,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self) -> list[Task]:
        """Return all tasks sorted by ID.

        Returns:
            A list of all tasks, sorted by ID in ascending order.
        """
        return sorted(self._tasks.values(), key=lambda t: t.id)

    def get_task(self, task_id: int) -> Task | None:
        """Return task by ID, or None if not found.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            The Task if found, None otherwise.
        """
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, new_content: str) -> Task:
        """Update task content.

        Args:
            task_id: The ID of the task to update.
            new_content: The new task description.

        Returns:
            The updated Task.

        Raises:
            TaskNotFoundError: If task_id is not found.
            ValueError: If new_content is empty or too long.
        """
        task = self._tasks.get(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        # Validate new content
        stripped_content = new_content.strip()
        if not stripped_content:
            raise ValueError("Task content cannot be empty")
        if len(stripped_content) > 500:
            raise ValueError("Task content cannot exceed 500 characters")

        task.update_content(stripped_content)
        return task

    def delete_task(self, task_id: int) -> None:
        """Delete task by ID.

        Args:
            task_id: The ID of the task to delete.

        Raises:
            TaskNotFoundError: If task_id is not found.
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)
        del self._tasks[task_id]

    def mark_complete(self, task_id: int) -> Task:
        """Mark task as complete. Idempotent operation.

        Args:
            task_id: The ID of the task to mark complete.

        Returns:
            The updated Task.

        Raises:
            TaskNotFoundError: If task_id is not found.
        """
        task = self._tasks.get(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        task.mark_complete()
        return task

    def mark_incomplete(self, task_id: int) -> Task:
        """Mark task as incomplete. Idempotent operation.

        Args:
            task_id: The ID of the task to mark incomplete.

        Returns:
            The updated Task.

        Raises:
            TaskNotFoundError: If task_id is not found.
        """
        task = self._tasks.get(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        task.mark_incomplete()
        return task

    def get_task_count(self) -> int:
        """Return the number of tasks in storage.

        Returns:
            The total number of tasks.
        """
        return len(self._tasks)

    def clear_all_tasks(self) -> None:
        """Remove all tasks from storage.

        Used primarily for testing purposes.
        """
        self._tasks.clear()
        self._next_id = 1

    def __enter__(self) -> Self:
        """Support context manager protocol."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Support context manager protocol."""
        pass
