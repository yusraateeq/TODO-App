#!/usr/bin/env python3
"""Main entry point for the Todo Application.

This module provides a menu-driven CLI interface for managing tasks.
Run this file directly to start the application:
    python todo.py
"""

from todo.cli.menu import Menu
from todo.cli.inputs import get_task_content, get_task_id, get_menu_choice, confirm_action
from todo.services.task_service import TaskService


def main() -> None:
    """Run the Todo application."""
    # Initialize components
    task_service = TaskService()
    menu = Menu()

    # Display welcome message
    menu.display_welcome()

    # Main menu loop
    while True:
        # Display menu and get user choice
        menu.display_menu()
        choice = get_menu_choice()

        # Handle user selection
        if choice == 1:
            handle_add_task(task_service, menu)
        elif choice == 2:
            handle_view_tasks(task_service, menu)
        elif choice == 3:
            handle_update_task(task_service, menu)
        elif choice == 4:
            handle_delete_task(task_service, menu)
        elif choice == 5:
            handle_mark_complete(task_service, menu)
        elif choice == 6:
            handle_mark_incomplete(task_service, menu)
        elif choice == 7:
            break

    # Display goodbye message
    menu.display_goodbye()


def handle_add_task(task_service: TaskService, menu: Menu) -> None:
    """Handle the Add Task menu option.

    Args:
        task_service: The task service instance.
        menu: The menu instance.
    """
    try:
        content = get_task_content()
        task = task_service.add_task(content)
        menu.display_task_added(task)
    except ValueError as e:
        menu.display_error(e)


def handle_view_tasks(task_service: TaskService, menu: Menu) -> None:
    """Handle the View Tasks menu option.

    Args:
        task_service: The task service instance.
        menu: The menu instance.
    """
    tasks = task_service.get_all_tasks()
    menu.display_tasks(tasks)


def handle_update_task(task_service: TaskService, menu: Menu) -> None:
    """Handle the Update Task menu option.

    Args:
        task_service: The task service instance.
        menu: The menu instance.
    """
    if task_service.get_task_count() == 0:
        menu.display_error(Exception("No tasks to update. Add a task first."))
        return

    try:
        task_id = get_task_id("Enter ID of task to update: ")
        content = get_task_content("Enter new task description: ")
        task = task_service.update_task(task_id, content)
        menu.display_task_updated(task)
    except Exception as e:
        menu.display_error(e)


def handle_delete_task(task_service: TaskService, menu: Menu) -> None:
    """Handle the Delete Task menu option.

    Args:
        task_service: The task service instance.
        menu: The menu instance.
    """
    if task_service.get_task_count() == 0:
        menu.display_error(Exception("No tasks to delete. Add a task first."))
        return

    try:
        task_id = get_task_id("Enter ID of task to delete: ")
        if confirm_action(f"Are you sure you want to delete task {task_id}? (y/n): "):
            task_service.delete_task(task_id)
            menu.display_task_deleted(task_id)
        else:
            menu.display_message("Delete cancelled.")
    except Exception as e:
        menu.display_error(e)


def handle_mark_complete(task_service: TaskService, menu: Menu) -> None:
    """Handle the Mark Task Complete menu option.

    Args:
        task_service: The task service instance.
        menu: The menu instance.
    """
    if task_service.get_task_count() == 0:
        menu.display_error(Exception("No tasks available. Add a task first."))
        return

    try:
        task_id = get_task_id("Enter ID of task to mark complete: ")
        task = task_service.mark_complete(task_id)
        menu.display_task_status_changed(task, "marked complete")
    except Exception as e:
        menu.display_error(e)


def handle_mark_incomplete(task_service: TaskService, menu: Menu) -> None:
    """Handle the Mark Task Incomplete menu option.

    Args:
        task_service: The task service instance.
        menu: The menu instance.
    """
    if task_service.get_task_count() == 0:
        menu.display_error(Exception("No tasks available. Add a task first."))
        return

    try:
        task_id = get_task_id("Enter ID of task to mark incomplete: ")
        task = task_service.mark_incomplete(task_id)
        menu.display_task_status_changed(task, "marked incomplete")
    except Exception as e:
        menu.display_error(e)


if __name__ == "__main__":
    main()
