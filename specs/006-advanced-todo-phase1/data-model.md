# Data Model: Advanced Todo Phase I

## Entities

### Task
Represents a single todo item.

| Attribute | Type | Description |
|-----------|------|-------------|
| id | int | Unique identifier |
| title | str | Name of the task |
| description | str | Detailed info |
| priority | enum | Low, Medium, High |
| status | enum | Incomplete, Done |
| recurrence_type | enum/str | None, Daily, Weekly, Monthly |
| due_datetime | datetime | Full deadline (YYYY-MM-DD HH:MM) |
| created_at | datetime | Timestamp of creation |

## State Transitions

### Mark Complete
1. If `recurrence_type` is `None`:
    - Set `status` to `Done`.
2. If `recurrence_type` is NOT `None`:
    - Set `status` to `Done`.
    - Create a NEW `Task` instance.
    - Title/Desc/Priority/Recurrence inherited from parent.
    - `due_datetime` = `parent.due_datetime` + recurrence interval.
    - Add to memory list.

## Validation Rules
- **Datetime**: Must match `%Y-%m-%d %H:%M`. Must not be in the past for *new* tasks (optional/soft warning).
- **Recurrence**: Must be one of `['none', 'daily', 'weekly', 'monthly']`.
