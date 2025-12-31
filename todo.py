#!/usr/bin/env python3
"""Main entry point for the Todo Application (Advanced Level)."""

import sys
from todo.cli.menu import Menu
from todo.cli.inputs import (
    get_task_content, get_task_id, get_menu_choice, confirm_action,
    get_due_date, get_priority, get_tags, get_recurrence
)
from todo.services.task_service import TaskService
from todo.models.task import TaskStatus


def main() -> None:
    """Run the Todo application."""
    task_service = TaskService()
    menu = Menu()

    menu.display_welcome()

    while True:
        # Show reminders at the start of each menu cycle
        overdue = task_service.get_overdue_tasks()
        menu.display_reminders(overdue)

        menu.display_menu()
        choice = get_menu_choice((1, 15))

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
            handle_set_due_date(task_service, menu)
        elif choice == 8:
            handle_set_priority(task_service, menu)
        elif choice == 9:
            handle_manage_tags(task_service, menu)
        elif choice == 10:
            handle_search_tasks(task_service, menu)
        elif choice == 11:
            handle_filter_tasks(task_service, menu)
        elif choice == 12:
            handle_sort_tasks(task_service, menu)
        elif choice == 13:
            handle_view_reminders(task_service, menu)
        elif choice == 14:
            handle_set_recurrence(task_service, menu)
        elif choice == 15:
            break

    menu.display_goodbye()


def handle_add_task(task_service: TaskService, menu: Menu) -> None:
    try:
        content = get_task_content()
        due_date = get_due_date()
        recurrence = get_recurrence()
        priority = get_priority()
        tags = get_tags()
        task = task_service.add_task(content, due_date, priority, tags, recurrence)
        menu.display_task_added(task)
    except Exception as e:
        menu.display_error(e)


def handle_view_tasks(task_service: TaskService, menu: Menu) -> None:
    tasks = task_service.get_all_tasks()
    menu.display_tasks(tasks, "All Tasks")


def handle_update_task(task_service: TaskService, menu: Menu) -> None:
    if task_service.get_task_count() == 0:
        menu.display_error(Exception("No tasks to update."))
        return
    try:
        task_id = get_task_id("Enter ID to update content: ")
        content = get_task_content("Enter new description: ")
        task = task_service.update_task(task_id, content)
        menu.display_task_updated(task)
    except Exception as e:
        menu.display_error(e)


def handle_delete_task(task_service: TaskService, menu: Menu) -> None:
    if task_service.get_task_count() == 0:
        menu.display_error(Exception("No tasks to delete."))
        return
    try:
        task_id = get_task_id("Enter ID to delete: ")
        if confirm_action(f"Delete task {task_id}? (y/n): "):
            task_service.delete_task(task_id)
            menu.display_task_deleted(task_id)
    except Exception as e:
        menu.display_error(e)


def handle_mark_complete(task_service: TaskService, menu: Menu) -> None:
    try:
        task_id = get_task_id("Enter ID to mark complete: ")
        task = task_service.mark_complete(task_id)
        msg = "marked complete"
        if task.recurrence != "none":
            msg += " (new recurring instance created)"
        menu.display_task_status_changed(task, msg)
    except Exception as e:
        menu.display_error(e)


def handle_mark_incomplete(task_service: TaskService, menu: Menu) -> None:
    try:
        task_id = get_task_id("Enter ID to mark incomplete: ")
        task = task_service.mark_incomplete(task_id)
        menu.display_task_status_changed(task, "marked incomplete")
    except Exception as e:
        menu.display_error(e)


def handle_set_due_date(task_service: TaskService, menu: Menu) -> None:
    try:
        task_id = get_task_id("Enter task ID: ")
        due_date = get_due_date()
        task = task_service.update_task_metadata(task_id, due_date=due_date)
        dt_str = due_date.strftime("%Y-%m-%d %H:%M") if due_date else "None"
        menu.display_success(f"Due date for task {task_id} updated to {dt_str}.")
    except Exception as e:
        menu.display_error(e)


def handle_set_priority(task_service: TaskService, menu: Menu) -> None:
    try:
        task_id = get_task_id("Enter task ID: ")
        priority = get_priority()
        task = task_service.update_task_metadata(task_id, priority=priority)
        menu.display_success(f"Priority for task {task_id} updated to {priority.upper()}.")
    except Exception as e:
        menu.display_error(e)


def handle_manage_tags(task_service: TaskService, menu: Menu) -> None:
    try:
        task_id = get_task_id("Enter task ID: ")
        tags = get_tags()
        task = task_service.update_task_metadata(task_id, tags=tags)
        menu.display_success(f"Tags for task {task_id} updated.")
    except Exception as e:
        menu.display_error(e)


def handle_search_tasks(task_service: TaskService, menu: Menu) -> None:
    keyword = input("Enter search keyword: ").strip()
    if not keyword:
        menu.display_error(Exception("Keyword cannot be empty."))
        return
    results = task_service.search_tasks(keyword)
    menu.display_tasks(results, f"Search results for '{keyword}'")


def handle_filter_tasks(task_service: TaskService, menu: Menu) -> None:
    print("\n1. Filter by Status")
    print("2. Filter by Priority")
    print("3. Filter by Tag")
    print("4. Filter by Due Date/Time")
    choice = input("Choice: ").strip()

    tasks = []
    if choice == '1':
        st = input("Enter status (complete/incomplete): ").strip().lower()
        tasks = task_service.filter_tasks(status=TaskStatus(st) if st in ["complete", "incomplete"] else None)
    elif choice == '2':
        pr = get_priority("Enter priority: ")
        tasks = task_service.filter_tasks(priority=pr)
    elif choice == '3':
        tg = input("Enter tag: ").strip().lower()
        tasks = task_service.filter_tasks(tag=tg)
    elif choice == '4':
        dt = get_due_date()
        tasks = task_service.filter_tasks(due_date=dt)

    menu.display_tasks(tasks, "Filtered results")


def handle_sort_tasks(task_service: TaskService, menu: Menu) -> None:
    print("\n1. Sort by Due Date")
    print("2. Sort by Priority")
    print("3. Sort by Title")
    print("4. Sort by Creation Time")
    choice = input("Choice: ").strip()

    sort_map = {'1': "due_date", '2': "priority", '3': "title", '4': "creation_time"}
    if choice in sort_map:
        results = task_service.sort_tasks(sort_map[choice])
        menu.display_tasks(results, f"Sorted by {sort_map[choice]}")
    else:
        menu.display_error(Exception("Invalid sort choice."))


def handle_view_reminders(task_service: TaskService, menu: Menu) -> None:
    overdue = task_service.get_overdue_tasks()
    if overdue:
        menu.display_tasks(overdue, "Overdue Reminders")
    else:
        menu.display_success("No overdue tasks. You're all caught up!")


def handle_set_recurrence(task_service: TaskService, menu: Menu) -> None:
    try:
        task_id = get_task_id("Enter task ID: ")
        recurrence = get_recurrence()
        task = task_service.update_task_metadata(task_id, recurrence=recurrence)
        menu.display_success(f"Recurrence for task {task_id} updated to {recurrence.value}.")
    except Exception as e:
        menu.display_error(e)


if __name__ == "__main__":
    main()
