---
id: 1
title: Generate intermediate features specification
stage: spec
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-intermediate
branch: 004-todo-intermediate
user: yusraa
command: /sp.specify
labels: [spec, pytest, python]
links:
  spec: specs/004-todo-intermediate/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/004-todo-intermediate/specify.py
 - specs/004-todo-intermediate/spec.md
 - specs/004-todo-intermediate/requirements.md
tests:
 - specs/004-todo-intermediate/specify.py
---

## Prompt

You are an expert Python tester using pytest. We are extending our Todo App from Basic to Intermediate Level.

Current project has todo.py with a main class (likely TodoApp or TaskManager) that already supports: add_task, delete_task, update_task, list_tasks, mark_complete.

Now adding Intermediate features:
- Due dates (stored as string in 'YYYY-MM-DD' format or datetime)
- Priority (high, medium, low)
- Tags/Categories (list of strings, e.g., ["work", "personal"])
- Search by keyword
- Filter by status, priority, tag, due date range
- Sort by due date, priority, creation time, or title alphabetically

Your task: Generate a complete, detailed pytest specification file at specs/specify.py that covers ALL intermediate features with thorough tests.

Requirements:
- Use clear, descriptive test names like test_add_task_with_priority_and_tags_succeeds
- Include positive, negative, edge cases, and error handling
- At least 5-7 tests per major feature
- Test combinations (e.g., filter + sort, search within filtered results)
- Use pytest fixtures (create a fixture called fresh_todo_app that returns a clean instance)
- Assume tasks are stored in memory (list/dict) for now
- Include imports: from todo import TodoApp (or whatever the class name is), import pytest, from datetime import date if needed

Output ONLY the full content of specs/specify.py inside a ```python code block. Do not explain, just the code.

## Response snapshot

Generated a comprehensive pytest suite in `specs/004-todo-intermediate/specify.py` covering Due Dates, Priority, Tags, Search, Filtering, and Sorting. Also provided a behavior-driven `spec.md` and a quality checklist in `requirements.md`.

## Outcome

- ✅ Impact: Established specification and tests for intermediate Todo App features.
- 🧪 Tests: 20+ test cases covering positive, negative, and combination scenarios.
- 📁 Files: Created spec.md, specify.py, and requirements.md.
- 🔁 Next prompts: /sp.clarify or /sp.plan
- 🧠 Reflection: Using specific branch 004-todo-intermediate to manage the multi-step SDD workflow.

## Evaluation notes (flywheel)

- Failure modes observed: Shell script for feature creation was missing/incompatible, handled via manual bash commands.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
