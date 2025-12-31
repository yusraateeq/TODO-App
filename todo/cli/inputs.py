"""User input handling and validation utilities."""

from datetime import datetime
from typing import List, Optional

from todo.models.task import Priority, RecurrenceType


def get_task_content(prompt: Optional[str] = None) -> str:
    """Prompt for and validate task content."""
    if prompt is None:
        prompt = "Enter task description: "

    while True:
        content = input(prompt).strip()
        if not content:
            print("Error: Task content cannot be empty.")
            continue
        if len(content) > 500:
            print(f"Error: Task content is too long. Max 500 chars.")
            continue
        return content


def get_task_id(prompt: Optional[str] = None) -> int:
    """Prompt for and validate a task ID."""
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
                print("Error: Task ID must be a positive integer.")
                continue
            return task_id
        except ValueError:
            print("Error: Invalid input. Please enter a numeric task ID.")


def get_menu_choice(valid_range: tuple[int, int] = (1, 15), prompt: Optional[str] = None) -> int:
    """Prompt for and validate a menu selection."""
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
                print(f"Error: Please enter a number between {min_choice} and {max_choice}.")
                continue
            return choice
        except ValueError:
            print("Error: Invalid input. Please enter a numeric choice.")


def get_due_date(prompt: str = "Enter due date/time (YYYY-MM-DD HH:MM) or leave blank: ") -> Optional[datetime]:
    """Prompt for and validate a datetime string."""
    while True:
        date_str = input(prompt).strip()
        if not date_str:
            return None
        try:
            return datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Error: Invalid format. Please use YYYY-MM-DD HH:MM.")


def get_recurrence(prompt: str = "Enter recurrence (none/daily/weekly/monthly) [none]: ") -> RecurrenceType:
    """Prompt for and validate recurrence type."""
    while True:
        r_input = input(prompt).strip().lower()
        if not r_input:
            return RecurrenceType.NONE
        try:
            return RecurrenceType(r_input)
        except ValueError:
            print("Error: Invalid recurrence. Choose none, daily, weekly, or monthly.")


def get_priority(prompt: str = "Enter priority (high/medium/low) [medium]: ") -> Priority:
    """Prompt for and validate priority."""
    while True:
        p_input = input(prompt).strip().lower()
        if not p_input:
            return Priority.MEDIUM
        try:
            return Priority(p_input)
        except ValueError:
            print("Error: Invalid priority. Choose high, medium, or low.")


def get_tags(prompt: str = "Enter tags (comma-separated): ") -> List[str]:
    """Prompt for comma-separated tags."""
    tags_str = input(prompt).strip()
    if not tags_str:
        return []
    return list(dict.fromkeys([t.strip().lower() for t in tags_str.split(",") if t.strip()]))


def confirm_action(prompt: str = "Are you sure? (y/n): ") -> bool:
    """Prompt for confirmation."""
    while True:
        ui = input(prompt).strip().lower()
        if ui in ("y", "yes"):
            return True
        if ui in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")
