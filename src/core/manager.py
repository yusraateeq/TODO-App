from typing import List, Optional
from datetime import date
from .models import Task

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, content: str, due_date: Optional[date] = None,
                 priority: str = "medium", tags: List[str] = None) -> Task:
        task = Task(
            id=self._next_id,
            content=content,
            due_date=due_date,
            priority=priority,
            tags=tags or []
        )
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def parse_tags(self, tags_str: str) -> List[str]:
        """Parses comma-separated tags into a unique, stripped list."""
        if not tags_str:
            return []
        tags = [t.strip().lower() for t in tags_str.split(",") if t.strip()]
        return list(dict.fromkeys(tags)) # Maintain order, ensure uniqueness
