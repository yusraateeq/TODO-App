"""Tests for the TaskService."""

import pytest

from todo.models.task import Task, TaskStatus
from todo.services.task_service import TaskService
from todo.exceptions import TaskNotFoundError


class TestTaskServiceCreation:
    """Tests for TaskService initialization."""

    def test_service_starts_empty(self):
        """Test that new service has no tasks."""
        service = TaskService()
        assert service.get_task_count() == 0

    def test_first_task_gets_id_1(self):
        """Test that first task gets ID 1."""
        service = TaskService()
        task = service.add_task("First task")
        assert task.id == 1

    def test_ids_increment(self):
        """Test that task IDs increment correctly."""
        service = TaskService()
        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")
        task3 = service.add_task("Task 3")

        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3


class TestAddTask:
    """Tests for add_task method."""

    def test_add_task_creates_task(self):
        """Test that add_task creates a task with correct content."""
        service = TaskService()
        task = service.add_task("Buy groceries")

        assert task.content == "Buy groceries"
        assert task.status == TaskStatus.INCOMPLETE

    def test_add_task_strips_whitespace(self):
        """Test that add_task strips leading/trailing whitespace."""
        service = TaskService()
        task = service.add_task("  Buy groceries  ")

        assert task.content == "Buy groceries"

    def test_add_task_empty_content_raises_error(self):
        """Test that empty content raises ValueError."""
        service = TaskService()

        with pytest.raises(ValueError, match="Task content cannot be empty"):
            service.add_task("")

    def test_add_task_too_long_raises_error(self):
        """Test that content over 500 chars raises ValueError."""
        service = TaskService()
        long_content = "x" * 501

        with pytest.raises(ValueError, match="Task content cannot exceed 500 characters"):
            service.add_task(long_content)

    def test_added_task_can_be_retrieved(self):
        """Test that added task can be retrieved by ID."""
        service = TaskService()
        original = service.add_task("Test task")

        retrieved = service.get_task(original.id)

        assert retrieved is not None
        assert retrieved.id == original.id
        assert retrieved.content == original.content


class TestGetAllTasks:
    """Tests for get_all_tasks method."""

    def test_get_empty_list(self):
        """Test that empty list is returned when no tasks."""
        service = TaskService()
        tasks = service.get_all_tasks()

        assert tasks == []

    def test_get_all_returns_sorted_list(self):
        """Test that tasks are returned sorted by ID."""
        service = TaskService()
        service.add_task("Third")
        service.add_task("First")
        service.add_task("Second")

        tasks = service.get_all_tasks()

        assert len(tasks) == 3
        assert tasks[0].id == 1
        assert tasks[1].id == 2
        assert tasks[2].id == 3
        assert tasks[0].content == "Third"  # Added first
        assert tasks[1].content == "First"  # Added second
        assert tasks[2].content == "Second"  # Added third


class TestGetTask:
    """Tests for get_task method."""

    def test_get_existing_task(self):
        """Test retrieving an existing task."""
        service = TaskService()
        original = service.add_task("Test task")

        task = service.get_task(original.id)

        assert task == original

    def test_get_nonexistent_task_returns_none(self):
        """Test that getting non-existent task returns None."""
        service = TaskService()

        task = service.get_task(999)

        assert task is None


class TestUpdateTask:
    """Tests for update_task method."""

    def test_update_content(self):
        """Test updating task content."""
        service = TaskService()
        original = service.add_task("Original content")

        updated = service.update_task(original.id, "New content")

        assert updated.content == "New content"

    def test_update_nonexistent_task_raises_error(self):
        """Test that updating non-existent task raises TaskNotFoundError."""
        service = TaskService()

        with pytest.raises(TaskNotFoundError):
            service.update_task(999, "New content")

    def test_update_strips_whitespace(self):
        """Test that update strips whitespace."""
        service = TaskService()
        task = service.add_task("Original")

        service.update_task(task.id, "  New content  ")

        assert task.content == "New content"

    def test_update_empty_content_raises_error(self):
        """Test that empty content raises ValueError."""
        service = TaskService()
        task = service.add_task("Test")

        with pytest.raises(ValueError, match="Task content cannot be empty"):
            service.update_task(task.id, "")

    def test_update_updates_timestamp(self):
        """Test that update changes updated_at."""
        service = TaskService()
        task = service.add_task("Test")
        original_updated = task.updated_at

        # Small delay to ensure timestamp difference
        service.update_task(task.id, "New content")

        assert task.updated_at > original_updated


class TestDeleteTask:
    """Tests for delete_task method."""

    def test_delete_removes_task(self):
        """Test that delete removes the task."""
        service = TaskService()
        task = service.add_task("Test task")

        service.delete_task(task.id)

        assert service.get_task_count() == 0
        assert service.get_task(task.id) is None

    def test_delete_nonexistent_task_raises_error(self):
        """Test that deleting non-existent task raises TaskNotFoundError."""
        service = TaskService()

        with pytest.raises(TaskNotFoundError):
            service.delete_task(999)

    def test_delete_one_does_not_affect_others(self):
        """Test that deleting one task doesn't affect others."""
        service = TaskService()
        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")

        service.delete_task(task1.id)

        assert service.get_task(task2.id) is not None
        assert service.get_task_count() == 1


class TestMarkComplete:
    """Tests for mark_complete method."""

    def test_mark_complete_changes_status(self):
        """Test marking task as complete."""
        service = TaskService()
        task = service.add_task("Test task")
        assert task.status == TaskStatus.INCOMPLETE

        result = service.mark_complete(task.id)

        assert result.status == TaskStatus.COMPLETE

    def test_mark_complete_idempotent(self):
        """Test that marking complete twice doesn't cause issues."""
        service = TaskService()
        task = service.add_task("Test task")

        service.mark_complete(task.id)
        service.mark_complete(task.id)

        assert task.status == TaskStatus.COMPLETE

    def test_mark_complete_nonexistent_raises_error(self):
        """Test that marking complete non-existent task raises error."""
        service = TaskService()

        with pytest.raises(TaskNotFoundError):
            service.mark_complete(999)

    def test_mark_complete_updates_timestamp(self):
        """Test that mark_complete updates timestamp."""
        service = TaskService()
        task = service.add_task("Test task")
        original_updated = task.updated_at

        service.mark_complete(task.id)

        assert task.updated_at > original_updated


class TestMarkIncomplete:
    """Tests for mark_incomplete method."""

    def test_mark_incomplete_changes_status(self):
        """Test marking task as incomplete."""
        service = TaskService()
        task = service.add_task("Test task")
        service.mark_complete(task.id)
        assert task.status == TaskStatus.COMPLETE

        result = service.mark_incomplete(task.id)

        assert result.status == TaskStatus.INCOMPLETE

    def test_mark_incomplete_idempotent(self):
        """Test that marking incomplete twice doesn't cause issues."""
        service = TaskService()
        task = service.add_task("Test task")
        service.mark_complete(task.id)

        service.mark_incomplete(task.id)
        service.mark_incomplete(task.id)

        assert task.status == TaskStatus.INCOMPLETE

    def test_mark_incomplete_on_already_incomplete(self):
        """Test marking incomplete on already incomplete task."""
        service = TaskService()
        task = service.add_task("Test task")

        result = service.mark_incomplete(task.id)

        assert result.status == TaskStatus.INCOMPLETE

    def test_mark_incomplete_nonexistent_raises_error(self):
        """Test that marking incomplete non-existent task raises error."""
        service = TaskService()

        with pytest.raises(TaskNotFoundError):
            service.mark_incomplete(999)

    def test_mark_incomplete_updates_timestamp(self):
        """Test that mark_incomplete updates timestamp."""
        service = TaskService()
        task = service.add_task("Test task")
        service.mark_complete(task.id)
        original_updated = task.updated_at

        service.mark_incomplete(task.id)

        assert task.updated_at > original_updated


class TestTaskServiceUtilities:
    """Tests for utility methods."""

    def test_get_task_count(self):
        """Test get_task_count returns correct value."""
        service = TaskService()
        assert service.get_task_count() == 0

        service.add_task("Task 1")
        assert service.get_task_count() == 1

        service.add_task("Task 2")
        assert service.get_task_count() == 2

    def test_clear_all_tasks(self):
        """Test that clear_all_tasks removes all tasks."""
        service = TaskService()
        service.add_task("Task 1")
        service.add_task("Task 2")

        service.clear_all_tasks()

        assert service.get_task_count() == 0
        assert service.get_all_tasks() == []

    def test_clear_all_tasks_resets_id_counter(self):
        """Test that clear_all_tasks resets ID counter."""
        service = TaskService()
        service.add_task("Task 1")
        service.add_task("Task 2")

        service.clear_all_tasks()

        task = service.add_task("New task")
        assert task.id == 1
