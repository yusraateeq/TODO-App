"""Task data model for the Todo application."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    """Enumeration of possible task statuses."""

    INCOMPLETE = "incomplete"
    COMPLETE = "complete"


@dataclass
class Task:
    """Represents a single task in the todo list.

    Attributes:
        id: Unique identifier for the task (auto-generated).
        content: The task description (1-500 characters).
        status: Current completion status.
        created_at: Timestamp when the task was created.
        updated_at: Timestamp when the task was last modified.
    """

    id: int
    content: str
    status: TaskStatus = TaskStatus.INCOMPLETE
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        """Validate task data after initialization."""
        # Validate content is not empty after stripping whitespace
        if not self.content or len(self.content.strip()) == 0:
            raise ValueError("Task content cannot be empty")

        # Validate content length
        if len(self.content) > 500:
            raise ValueError("Task content cannot exceed 500 characters")

        # Validate ID is positive
        if self.id <= 0:
            raise ValueError("Task ID must be positive")

    def mark_complete(self) -> None:
        """Mark the task as complete."""
        self.status = TaskStatus.COMPLETE
        self.updated_at = datetime.now()

    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.status = TaskStatus.INCOMPLETE
        self.updated_at = datetime.now()

    def update_content(self, new_content: str) -> None:
        """Update the task content.

        Args:
            new_content: The new task description.
        """
        self.content = new_content.strip()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Return a human-readable string representation."""
        status_icon = "[x]" if self.status == TaskStatus.COMPLETE else "[ ]"
        status_text = "Complete" if self.status == TaskStatus.COMPLETE else "Incomplete"
        return f"{self.id:3} | {status_icon} {status_text:<10} | {self.content}"
