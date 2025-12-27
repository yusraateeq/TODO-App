"""User input handling and validation utilities."""

from typing import Optional

from todo.exceptions import InvalidInputError, InvalidMenuChoiceError


def get_task_content(prompt: Optional[str] = None) -> str:
    """Prompt for and validate task content.

    Args:
        prompt: Optional custom prompt message.

    Returns:
        The validated task content (stripped of leading/trailing whitespace).

    Raises:
        InvalidInputError: If input is empty or too long.
    """
    if prompt is None:
        prompt = "Enter task description: "

    while True:
        content = input(prompt).strip()

        if not content:
            print("Error: Task content cannot be empty. Please try again.")
            continue

        if len(content) > 500:
            print(
                f"Error: Task content is too long ({len(content)} chars). "
                "Maximum is 500 characters. Please try again."
            )
            continue

        return content


def get_task_id(prompt: Optional[str] = None) -> int:
    """Prompt for and validate a task ID.

    Args:
        prompt: Optional custom prompt message.

    Returns:
        The validated positive integer task ID.

    Raises:
        InvalidInputError: If input is not a valid positive integer.
    """
    if prompt is None:
        prompt = "Enter task ID: "

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("Error: Please enter a task ID.")
            continue

        try:
            task_id = int(user_input)
            if task_id <= 0:
                print("Error: Task ID must be a positive integer. Please try again.")
                continue
            return task_id
        except ValueError:
            print("Error: Invalid input. Please enter a numeric task ID.")


def get_menu_choice(
    valid_range: tuple[int, int] = (1, 7), prompt: Optional[str] = None
) -> int:
    """Prompt for and validate a menu selection.

    Args:
        valid_range: Tuple of (min, max) valid menu choices.
        prompt: Optional custom prompt message.

    Returns:
        The validated menu choice as an integer.

    Raises:
        InvalidMenuChoiceError: If input is not in valid range.
    """
    min_choice, max_choice = valid_range

    if prompt is None:
        prompt = f"Enter your choice ({min_choice}-{max_choice}): "

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print(f"Please enter a number between {min_choice} and {max_choice}.")
            continue

        try:
            choice = int(user_input)
            if choice < min_choice or choice > max_choice:
                print(
                    f"Error: Please enter a number between {min_choice} and {max_choice}."
                )
                continue
            return choice
        except ValueError:
            print("Error: Invalid input. Please enter a numeric choice.")


def confirm_action(prompt: str = "Are you sure? (y/n): ") -> bool:
    """Prompt for confirmation of an action.

    Args:
        prompt: The confirmation prompt to display.

    Returns:
        True if user confirms (y/Y), False otherwise.
    """
    while True:
        user_input = input(prompt).strip().lower()

        if user_input in ("y", "yes"):
            return True
        elif user_input in ("n", "no"):
            return False
        else:
            print("Please enter 'y' or 'n'.")
