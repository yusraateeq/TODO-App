"""Custom exceptions for the Todo application."""


class TodoError(Exception):
    """Base exception for all todo application errors."""


class TaskNotFoundError(TodoError):
    """Raised when a task ID is not found in storage."""

    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(f"Task {task_id} not found")


class InvalidInputError(TodoError):
    """Raised when user input fails validation."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class InvalidMenuChoiceError(InvalidInputError):
    """Raised when menu selection is invalid."""

    def __init__(self, choice: str, valid_range: str = "1-7"):
        self.choice = choice
        self.valid_range = valid_range
        super().__init__(
            f"Invalid menu choice: '{choice}'. "
            f"Please enter a number between {valid_range}."
        )
