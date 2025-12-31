from typing import List, Optional
from datetime import date
from .models import Task

def search_tasks(tasks: List[Task], keyword: str) -> List[Task]:
    """Search tasks by keyword in content or tags."""
    k = keyword.lower()
    return [
        t for t in tasks
        if k in t.content.lower() or any(k in tag.lower() for tag in t.tags)
    ]

def filter_tasks(tasks: List[Task], status: Optional[str] = None,
                 priority: Optional[str] = None, tag: Optional[str] = None,
                 due_date: Optional[date] = None) -> List[Task]:
    """Filter tasks by multiple criteria."""
    result = tasks
    if status:
        result = [t for t in result if t.status == status]
    if priority:
        result = [t for t in result if t.priority == priority]
    if tag:
        tag_lower = tag.lower()
        result = [t for t in result if any(tag_lower == t_tag.lower() for t_tag in t.tags)]
    if due_date:
        result = [t for t in result if t.due_date == due_date]
    return result

def sort_tasks(tasks: List[Task], sort_by: str) -> List[Task]:
    """Sort tasks by due_date, priority, creation_time, or title."""
    priority_map = {"high": 0, "medium": 1, "low": 2}

    if sort_by == "due_date":
        # None dates go to the end
        return sorted(tasks, key=lambda t: (t.due_date is None, t.due_date, t.created_at))
    elif sort_by == "priority":
        return sorted(tasks, key=lambda t: (priority_map.get(t.priority, 1), t.created_at))
    elif sort_by == "title":
        return sorted(tasks, key=lambda t: (t.content.lower(), t.created_at))
    elif sort_by == "creation_time":
        return sorted(tasks, key=lambda t: t.created_at)

    return tasks
