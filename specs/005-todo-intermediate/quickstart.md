# Quickstart: Intermediate Todo Features

## Setup
Since this is an in-memory application, simply run the entry point with Python 3.12+.

```bash
python src/app.py
```

## New Commands
The CLI menu now includes the following:

- **6. Search Tasks**: Input a keyword to find matching tasks across titles and tags.
- **7. Filter Tasks**: Select a criteria (Priority/Status/Tag/Date) to narrow the list.
- **8. Sort Tasks**: Reorder the display by Due Date, Priority, or Title.

## Examples

### Adding a Task with Metadata
```text
Enter task description: Finish report
Enter due date (YYYY-MM-DD) or leave blank: 2025-12-31
Enter priority (high/medium/low) [medium]: high
Enter tags (comma-separated): work, urgent
```

### Filtering by Tag
```text
Enter tag to filter by: work
[1] Finish report | Due: 2025-12-31 | Priority: High | Tags: work, urgent
```
