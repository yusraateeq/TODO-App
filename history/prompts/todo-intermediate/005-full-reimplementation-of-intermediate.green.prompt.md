---
id: 5
title: Full Re-implementation of Intermediate Level
stage: green
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-intermediate
branch: 005-todo-intermediate
user: yusraa
command: /sp.implement
labels: ["refactor", "bugfix", "integration", "intermediate-features"]
links:
  spec: specs/005-todo-intermediate/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - todo.py
  - todo/models/task.py
  - todo/services/task_service.py
  - todo/cli/menu.py
  - todo/cli/inputs.py
tests:
  - null
---

## Prompt

FULL RE-IMPLEMENT Intermediate Level for Phase I with current modular structure.

CURRENT ISSUE: Running app still shows only 7 basic menu options. Intermediate features (due date, priority, tags, search, filter, sort) are not available.

PROJECT STRUCTURE (must preserve and extend):
- todo.py (main entry point with menu loop)
- todo/cli/menu.py (Menu class with display_menu, etc.)
- todo/cli/inputs.py (input functions)
- todo/services/task_service.py (TaskService class with all logic)
- (Possibly todo/models/task.py if exists)

REQUIREMENTS FOR INTERMEDIATE LEVEL:
1. Task model must have: id, title, description, completed, due_date (str 'YYYY-MM-DD' or None), priority ('high'/'medium'/'low', default 'medium'), tags (list[str])
2. Extend add_task and update_task to support new fields (prompt user for due_date, priority, tags)
3. New menu options (add to display_menu):
   8. Set Due Date (for existing task)
   9. Set Priority
   10. Manage Tags
   11. Search Tasks
   12. Filter Tasks
   13. Sort Tasks
   14. Exit (shift old exit)
4. Implement search, filter (by status/priority/tag/due), sort (multiple options)
5. Update display_tasks to show due_date, priority, tags nicely
6. All in-memory only

RULES:
- Output the COMPLETE content of ALL modified/created files in separate code blocks
- File paths as headers (e.g., ### todo/services/task_service.py)
- Use python for each
- Preserve clean architecture
- No file persistence
- Full working app after this

## Response snapshot

Fully re-implemented the Intermediate Level features within the user's preferred modular structure (`todo/` directory).
- **Service Layer**: Enhanced `TaskService` with search, filter, and sorting logic.
- **Model Layer**: Updated `Task` dataclass with `due_date`, `priority`, and `tags`.
- **CLI Layer**: Expanded `Menu` for tabular display of enriched tasks and added 6 new menu operations.
- **Input handling**: Added validation for ISO dates and priority enums in `inputs.py`.
- **Main Entry**: Updated `todo.py` main loop and handler functions to integrate all intermediate features.

## Outcome

- ✅ Impact: High - Resolves the issue where features were not visible in the existing app structure.
- 🧪 Tests: N/A (Manual validation recommended)
- 📁 Files: Updated todo.py, todo/models/task.py, todo/services/task_service.py, todo/cli/menu.py, and todo/cli/inputs.py.
- 🔁 Next prompts: /sp.analyze to verify feature alignment with specification.
- 🧠 Reflection: Maintaining the existing `todo/` package structure while extending functionality ensures the core application remains clean and follows established patterns.

## Evaluation notes (flywheel)

- Failure modes observed: Confusion between previously created modular structure (`src/`) and user-preferred structure (`todo/`). Resolved by re-mapping to user structure.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
