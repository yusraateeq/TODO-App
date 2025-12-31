from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List, Optional

@dataclass
class Task:
    id: int
    content: str
    status: str = "incomplete"  # "complete" or "incomplete"
    due_date: Optional[date] = None
    priority: str = "medium"  # "high", "medium", "low"
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "status": self.status,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "priority": self.priority,
            "tags": self.tags,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
