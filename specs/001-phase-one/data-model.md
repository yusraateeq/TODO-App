# Data Model: Phase I - Todo Console Application

## Task Entity

### Overview

The Task entity is the core data structure representing a single todo item in the in-memory storage.

### Attributes

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | int | > 0, unique | Auto-incremented identifier |
| `content` | str | 1-500 chars, required | Task description text |
| `status` | str | "complete" or "incomplete" | Current completion state |
| `created_at` | datetime | auto-set | Timestamp when task was created |
| `updated_at` | datetime | auto-update | Timestamp when task was last modified |

### Python Implementation

```python
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"

@dataclass
class Task:
    id: int
    content: str
    status: TaskStatus = TaskStatus.INCOMPLETE
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if not self.content or len(self.content.strip()) == 0:
            raise ValueError("Task content cannot be empty")
        if len(self.content) > 500:
            raise ValueError("Task content cannot exceed 500 characters")
        if self.id <= 0:
            raise ValueError("Task ID must be positive")
```

### State Machine

```
[incomplete] --mark_complete()--> [complete]
      ^                              |
      |                              v
      +--------mark_incomplete()----+
```

Both transitions are **idempotent** - calling mark_complete() on a complete task has no effect.

### Validation Rules

1. **Content Validation**:
   - Cannot be None
   - Cannot be empty after stripping whitespace
   - Maximum 500 characters
   - Leading/trailing whitespace preserved

2. **Status Validation**:
   - Must be a valid TaskStatus enum value
   - Default is INCOMPLETE

3. **ID Validation**:
   - Must be positive integer
   - Must be unique within the session

## Storage Structure

### In-Memory Storage

**Type**: Dictionary mapping task ID to Task object

```python
tasks: dict[int, Task] = {}
```

### ID Generation

**Strategy**: Auto-incrementing counter

```python
next_task_id: int = 1

def generate_id() -> int:
    nonlocal next_task_id
    current_id = next_task_id
    next_task_id += 1
    return current_id
```

### Access Patterns

| Operation | Method | Time Complexity |
|-----------|--------|-----------------|
| Add task | `tasks[id] = task` | O(1) |
| Get task | `tasks[id]` | O(1) |
| Delete task | `del tasks[id]` | O(1) |
| List all | `list(tasks.values())` | O(n) |
| Update task | `tasks[id] = task` | O(1) |

## Service Layer API

### TaskService Class

```python
class TaskService:
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, content: str) -> Task:
        """Create a new task with auto-generated ID."""
        task = Task(
            id=self._next_id,
            content=content.strip(),
            status=TaskStatus.INCOMPLETE
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self) -> list[Task]:
        """Return all tasks sorted by ID."""
        return sorted(self._tasks.values(), key=lambda t: t.id)

    def get_task(self, task_id: int) -> Task | None:
        """Return task by ID, or None if not found."""
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, new_content: str) -> Task:
        """Update task content. Raises TaskNotFoundError if not found."""
        task = self._tasks.get(task_id)
        if task is None:
            raise TaskNotFoundError(f"Task {task_id} not found")
        task.content = new_content.strip()
        task.updated_at = datetime.now()
        return task

    def delete_task(self, task_id: int) -> None:
        """Delete task by ID. Raises TaskNotFoundError if not found."""
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"Task {task_id} not found")
        del self._tasks[task_id]

    def mark_complete(self, task_id: int) -> Task:
        """Mark task as complete. Idempotent operation."""
        task = self._tasks.get(task_id)
        if task is None:
            raise TaskNotFoundError(f"Task {task_id} not found")
        task.status = TaskStatus.COMPLETE
        task.updated_at = datetime.now()
        return task

    def mark_incomplete(self, task_id: int) -> Task:
        """Mark task as incomplete. Idempotent operation."""
        task = self._tasks.get(task_id)
        if task is None:
            raise TaskNotFoundError(f"Task {task_id} not found")
        task.status = TaskStatus.INCOMPLETE
        task.updated_at = datetime.now()
        return task
```

## Exceptions

### Custom Exception Hierarchy

```python
class TodoError(Exception):
    """Base exception for all todo application errors."""

class TaskNotFoundError(TodoError):
    """Raised when a task ID is not found in storage."""

class InvalidInputError(TodoError):
    """Raised when user input fails validation."""

class InvalidMenuChoiceError(InvalidInputError):
    """Raised when menu selection is invalid."""
```

## CLI Contracts

### Menu Display Contract

```
=== Todo Application ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit

Enter your choice (1-7):
```

### Task List Display Format

```
ID  | Status       | Task
--- | ------------ | ------------------
1   | [ ] Incomplete | Buy groceries
2   | [x] Complete   | Call dentist
```

Legend:
- `[ ]` = Incomplete
- `[x]` = Complete
