import pytest
from datetime import date
from src.core.manager import TaskManager
from src.core.engine import search_tasks, filter_tasks, sort_tasks

def test_add_and_enrich_task():
    manager = TaskManager()
    t = manager.add_task("Test task", due_date=date(2025, 12, 31), priority="high", tags=["work", "test"])
    assert t.content == "Test task"
    assert t.due_date == date(2025, 12, 31)
    assert t.priority == "high"
    assert "work" in t.tags
    assert len(t.tags) == 2

def test_search_tasks():
    manager = TaskManager()
    manager.add_task("Buy milk", tags=["grocery"])
    manager.add_task("Call boss", tags=["work"])

    tasks = manager.get_all_tasks()
    results = search_tasks(tasks, "milk")
    assert len(results) == 1
    assert results[0].content == "Buy milk"

    results = search_tasks(tasks, "work")
    assert len(results) == 1
    assert results[0].content == "Call boss"

def test_filter_tasks():
    manager = TaskManager()
    manager.add_task("T1", priority="high", status="incomplete")
    manager.add_task("T2", priority="low", status="complete")

    tasks = manager.get_all_tasks()
    results = filter_tasks(tasks, priority="high")
    assert len(results) == 1
    assert results[0].content == "T1"

    results = filter_tasks(tasks, status="complete")
    assert len(results) == 1
    assert results[0].content == "T2"

def test_sort_tasks():
    manager = TaskManager()
    manager.add_task("Later", due_date=date(2026, 1, 1))
    manager.add_task("Sooner", due_date=date(2025, 1, 1))
    manager.add_task("No date", due_date=None)

    tasks = manager.get_all_tasks()
    results = sort_tasks(tasks, "due_date")
    assert results[0].content == "Sooner"
    assert results[1].content == "Later"
    assert results[2].content == "No date"
