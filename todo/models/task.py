"""Task data model for the Todo application."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional


class TaskStatus(str, Enum):
    """Enumeration of possible task statuses."""
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"


class Priority(str, Enum):
    """Enumeration of possible task priorities."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RecurrenceType(str, Enum):
    """Enumeration of possible recurrence types."""
    NONE = "none"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


@dataclass
class Task:
    """Represents a single task in the todo list.

    Attributes:
        id: Unique identifier for the task (auto-generated).
        content: The task description (1-500 characters).
        status: Current completion status.
        due_date: Optional due datetime.
        priority: Priority level (high, medium, low).
        recurrence: Recurrence type (none, daily, weekly, monthly).
        tags: List of categorization tags.
        created_at: Timestamp when the task was created.
        updated_at: Timestamp when the task was last modified.
    """

    id: int
    content: str
    status: TaskStatus = TaskStatus.INCOMPLETE
    due_date: Optional[datetime] = None
    priority: Priority = Priority.MEDIUM
    recurrence: RecurrenceType = RecurrenceType.NONE
    tags: List[str] = field(default_factory=list)
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
        """Update the task content."""
        self.content = new_content.strip()
        self.updated_at = datetime.now()

    def update_metadata(self, due_date: Optional[datetime] = None, priority: Optional[Priority] = None,
                        tags: Optional[List[str]] = None, recurrence: Optional[RecurrenceType] = None) -> None:
        """Update task metadata."""
        if due_date is not None:
            self.due_date = due_date
        if priority is not None:
            self.priority = priority
        if tags is not None:
            self.tags = tags
        if recurrence is not None:
            self.recurrence = recurrence
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Return a human-readable string representation."""
        status_icon = "[x]" if self.status == TaskStatus.COMPLETE else "[ ]"
        due_str = self.due_date.strftime("%Y-%m-%d %H:%M") if self.due_date else "None"
        recur_str = f" ({self.recurrence.value})" if self.recurrence != RecurrenceType.NONE else ""
        prio = f" [{self.priority.upper()}]"
        tag_str = f" Tags: {', '.join(self.tags)}" if self.tags else ""
        return f"{self.id:3} | {status_icon}{prio:<10} | {self.content} | Due: {due_str}{recur_str}{tag_str}"
