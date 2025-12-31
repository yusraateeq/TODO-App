"""Service for managing tasks in-memory."""

from datetime import datetime, timedelta
from typing import List, Optional

from todo.models.task import Task, TaskStatus, Priority, RecurrenceType


class TaskService:
    """Service class for task operations."""

    def __init__(self) -> None:
        """Initialize with an empty list and ID counter."""
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, content: str, due_date: Optional[datetime] = None,
                 priority: Priority = Priority.MEDIUM, tags: List[str] = None,
                 recurrence: RecurrenceType = RecurrenceType.NONE) -> Task:
        """Add a new task.

        Args:
            content: The task description.
            due_date: Optional due datetime.
            priority: Priority level.
            tags: List of tags.
            recurrence: Recurrence type.

        Returns:
            The newly created Task.
        """
        task = Task(
            id=self._next_id,
            content=content,
            due_date=due_date,
            priority=priority,
            tags=tags or [],
            recurrence=recurrence
        )
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks."""
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Find a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, content: str) -> Task:
        """Update a task's content."""
        task = self._get_or_raise(task_id)
        task.update_content(content)
        return task

    def update_task_metadata(self, task_id: int, due_date: Optional[datetime] = None,
                             priority: Optional[Priority] = None, tags: Optional[List[str]] = None,
                             recurrence: Optional[RecurrenceType] = None) -> Task:
        """Update a task's extra metadata."""
        task = self._get_or_raise(task_id)
        task.update_metadata(due_date=due_date, priority=priority, tags=tags, recurrence=recurrence)
        return task

    def delete_task(self, task_id: int) -> None:
        """Remove a task."""
        task = self._get_or_raise(task_id)
        self.tasks.remove(task)

    def mark_complete(self, task_id: int) -> Task:
        """Mark task as complete and handle recurrence."""
        task = self._get_or_raise(task_id)
        task.mark_complete()

        # Handle recurrence logic
        if task.recurrence != RecurrenceType.NONE and task.due_date:
            next_due = self._calculate_next_due(task.due_date, task.recurrence)
            if next_due:
                # Create a new instance of the task
                self.add_task(
                    content=task.content,
                    due_date=next_due,
                    priority=task.priority,
                    tags=task.tags,
                    recurrence=task.recurrence
                )

        return task

    def mark_incomplete(self, task_id: int) -> Task:
        """Mark task as incomplete."""
        task = self._get_or_raise(task_id)
        task.mark_incomplete()
        return task

    def get_task_count(self) -> int:
        """Return total number of tasks."""
        return len(self.tasks)

    def search_tasks(self, keyword: str) -> List[Task]:
        """Find tasks by keyword in content or tags."""
        k = keyword.lower()
        return [
            t for t in self.tasks
            if k in t.content.lower() or any(k in tag.lower() for tag in t.tags)
        ]

    def filter_tasks(self, status: Optional[TaskStatus] = None, priority: Optional[Priority] = None,
                     tag: Optional[str] = None, due_date: Optional[datetime] = None) -> List[Task]:
        """Filter tasks by multiple criteria."""
        results = self.tasks
        if status:
            results = [t for t in results if t.status == status]
        if priority:
            results = [t for t in results if t.priority == priority]
        if tag:
            tag_lower = tag.lower()
            results = [t for t in results if any(tag_lower == tt.lower() for tt in t.tags)]
        if due_date:
            # Filter by matching date (ignore time for exact day filtering if needed, but here we match exactly)
            results = [t for t in results if t.due_date == due_date]
        return results

    def sort_tasks(self, sort_by: str) -> List[Task]:
        """Sort tasks by due_date, priority, creation_time, or title."""
        priority_map = {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}

        if sort_by == "due_date":
            # None due_dates go to the end
            return sorted(self.tasks, key=lambda t: (t.due_date is None, t.due_date if t.due_date else datetime.max, t.created_at))
        elif sort_by == "priority":
            return sorted(self.tasks, key=lambda t: (priority_map.get(t.priority, 1), t.created_at))
        elif sort_by == "title":
            return sorted(self.tasks, key=lambda t: (t.content.lower(), t.created_at))
        elif sort_by == "creation_time":
            return sorted(self.tasks, key=lambda t: t.created_at)

        return self.tasks

    def get_overdue_tasks(self) -> List[Task]:
        """Return tasks that are incomplete and overdue."""
        now = datetime.now()
        return [
            t for t in self.tasks
            if t.status == TaskStatus.INCOMPLETE and t.due_date and t.due_date < now
        ]

    def _get_or_raise(self, task_id: int) -> Task:
        """Internal helper to get task or raise error."""
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        return task

    def _calculate_next_due(self, current_due: datetime, recurrence: RecurrenceType) -> Optional[datetime]:
        """Calculate the next due date based on recurrence type."""
        if recurrence == RecurrenceType.DAILY:
            return current_due + timedelta(days=1)
        elif recurrence == RecurrenceType.WEEKLY:
            return current_due + timedelta(weeks=1)
        elif recurrence == RecurrenceType.MONTHLY:
            # Approx month jump (30 days) - or handle properly if exactness is required
            # Simple approach: add 30 days
            new_month = current_due.month + 1
            new_year = current_due.year
            if new_month > 12:
                new_month = 1
                new_year += 1

            # Handle day overflow (e.g., Jan 31 -> Feb 28/29)
            try:
                return current_due.replace(year=new_year, month=new_month)
            except ValueError:
                # If day 31 doesn't exist in next month, use last day of next month
                if new_month == 2:
                    is_leap = (new_year % 4 == 0 and new_year % 100 != 0) or (new_year % 400 == 0)
                    day = 29 if is_leap else 28
                elif new_month in [4, 6, 9, 11]:
                    day = 30
                else:
                    day = 31
                return current_due.replace(year=new_year, month=new_month, day=day)

        return None
