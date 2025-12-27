"""Tests for the Task data model."""

import pytest
from datetime import datetime

from todo.models.task import Task, TaskStatus


class TestTaskStatus:
    """Tests for TaskStatus enum."""

    def test_status_values(self):
        """Test that status enum has correct values."""
        assert TaskStatus.INCOMPLETE.value == "incomplete"
        assert TaskStatus.COMPLETE.value == "complete"

    def test_status_comparison(self):
        """Test that status can be compared to strings."""
        assert TaskStatus.INCOMPLETE == "incomplete"
        assert TaskStatus.COMPLETE == "complete"


class TestTaskCreation:
    """Tests for Task instantiation."""

    def test_create_task_with_required_fields(self):
        """Test creating a task with only required fields."""
        task = Task(id=1, content="Test task")
        assert task.id == 1
        assert task.content == "Test task"
        assert task.status == TaskStatus.INCOMPLETE
        assert isinstance(task.created_at, datetime)
        assert isinstance(task.updated_at, datetime)

    def test_create_task_with_all_fields(self):
        """Test creating a task with all fields specified."""
        now = datetime.now()
        task = Task(
            id=1,
            content="Test task",
            status=TaskStatus.COMPLETE,
            created_at=now,
            updated_at=now,
        )
        assert task.status == TaskStatus.COMPLETE
        assert task.created_at == now
        assert task.updated_at == now

    def test_default_status_is_incomplete(self):
        """Test that default status is INCOMPLETE."""
        task = Task(id=1, content="Test task")
        assert task.status == TaskStatus.INCOMPLETE

    def test_content_is_preserved(self):
        """Test that content is stored correctly."""
        content = "Buy groceries"
        task = Task(id=1, content=content)
        assert task.content == content


class TestTaskValidation:
    """Tests for Task field validation."""

    def test_empty_content_raises_error(self):
        """Test that empty content raises ValueError."""
        with pytest.raises(ValueError, match="Task content cannot be empty"):
            Task(id=1, content="")

    def test_whitespace_only_content_raises_error(self):
        """Test that whitespace-only content raises ValueError."""
        with pytest.raises(ValueError, match="Task content cannot be empty"):
            Task(id=1, content="   ")

    def test_content_too_long_raises_error(self):
        """Test that content over 500 chars raises ValueError."""
        long_content = "x" * 501
        with pytest.raises(ValueError, match="Task content cannot exceed 500 characters"):
            Task(id=1, content=long_content)

    def test_max_length_content_is_valid(self):
        """Test that content with exactly 500 chars is valid."""
        content = "x" * 500
        task = Task(id=1, content=content)
        assert len(task.content) == 500

    def test_negative_id_raises_error(self):
        """Test that negative ID raises ValueError."""
        with pytest.raises(ValueError, match="Task ID must be positive"):
            Task(id=-1, content="Test task")

    def test_zero_id_raises_error(self):
        """Test that zero ID raises ValueError."""
        with pytest.raises(ValueError, match="Task ID must be positive"):
            Task(id=0, content="Test task")


class TestTaskMethods:
    """Tests for Task methods."""

    def test_mark_complete(self):
        """Test marking task as complete."""
        task = Task(id=1, content="Test task")
        assert task.status == TaskStatus.INCOMPLETE

        task.mark_complete()

        assert task.status == TaskStatus.COMPLETE
        assert isinstance(task.updated_at, datetime)

    def test_mark_incomplete(self):
        """Test marking task as incomplete."""
        task = Task(id=1, content="Test task", status=TaskStatus.COMPLETE)
        assert task.status == TaskStatus.COMPLETE

        task.mark_incomplete()

        assert task.status == TaskStatus.INCOMPLETE
        assert isinstance(task.updated_at, datetime)

    def test_update_content(self):
        """Test updating task content."""
        task = Task(id=1, content="Original content")

        task.update_content("New content")

        assert task.content == "New content"
        assert isinstance(task.updated_at, datetime)

    def test_update_content_strips_whitespace(self):
        """Test that update_content strips whitespace."""
        task = Task(id=1, content="Original")

        task.update_content("  New content  ")

        assert task.content == "New content"

    def test_str_representation_incomplete(self):
        """Test string representation for incomplete task."""
        task = Task(id=1, content="Buy groceries")
        result = str(task)
        assert "1" in result
        assert "[ ]" in result
        assert "Incomplete" in result
        assert "Buy groceries" in result

    def test_str_representation_complete(self):
        """Test string representation for complete task."""
        task = Task(id=2, content="Call dentist", status=TaskStatus.COMPLETE)
        result = str(task)
        assert "2" in result
        assert "[x]" in result
        assert "Complete" in result
        assert "Call dentist" in result


class TestTaskEquality:
    """Tests for Task equality."""

    def test_tasks_with_same_values_are_equal(self):
        """Test that tasks with same values are equal."""
        now = datetime.now()
        task1 = Task(id=1, content="Test", created_at=now, updated_at=now)
        task2 = Task(id=1, content="Test", created_at=now, updated_at=now)
        assert task1 == task2

    def test_tasks_with_different_ids_are_not_equal(self):
        """Test that tasks with different IDs are not equal."""
        now = datetime.now()
        task1 = Task(id=1, content="Test", created_at=now, updated_at=now)
        task2 = Task(id=2, content="Test", created_at=now, updated_at=now)
        assert task1 != task2
