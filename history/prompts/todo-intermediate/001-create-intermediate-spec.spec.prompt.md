---
id: 1
title: Create Intermediate Level Specification
stage: spec
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-intermediate
branch: 005-todo-intermediate
user: yusraa
command: /sp.specify
labels: ["specification", "todo-app", "intermediate-features"]
links:
  spec: specs/005-todo-intermediate/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/005-todo-intermediate/spec.md
  - specs/005-todo-intermediate/checklists/requirements.md
  - specs/005-todo-intermediate/plan.md
  - specs/005-todo-intermediate/tasks.md
tests:
  - null
---

## Prompt

Create the Intermediate Level specification for Phase I of the "Evolution of Todo" project.

Phase I Scope (remains unchanged):
- In-memory Python console application only
- Single user
- No persistence — data lost on exit
- Menu-driven CLI

Now extending from Basic to Intermediate Level features within the same phase.

Required Intermediate Features (build directly on Basic Level):
1. Due Dates – Assign due date to tasks (format: YYYY-MM-DD, can be None)
2. Priority – high, medium, low (default: medium)
3. Tags/Categories – Multiple tags per task as list of strings (e.g., work, personal, urgent)
4. Search Tasks – Find tasks by keyword in title, description, or tags
5. Filter Tasks – View tasks filtered by status, priority, tag, or due date
6. Sort Tasks – List tasks sorted by due date, priority, creation time, or title

Specification must include:
- Updated Task data model with new fields and constraints
- User stories for each intermediate feature
- CLI menu updates and new command flows
- How list display will show due date, priority, tags
- Acceptance criteria for each feature
- Error handling (invalid date, invalid priority, no tasks match filter, etc.)

Strict Constraints:
- NO file saving/loading
- NO JSON, NO database
- NO web, API, authentication
- NO references to persistence or future phases
- Must fully preserve all Basic Level features
- All data remains in-memory only

This specification defines exactly WHAT the Intermediate Level of Phase I must deliver.
It must comply with the global constitution.

## Response snapshot

Created the Intermediate Level specification for Phase I of the "Evolution of Todo" project.
- **Branch**: `005-todo-intermediate`
- **Spec File**: `specs/005-todo-intermediate/spec.md`
- **Features Defined**: Due Dates, Priorities, Multi-tagging, Search, Filtering, and Sorting.
- **Constraints**: Maintained strict in-memory only operations with no persistence.
- **Validation**: Completed quality checklist; all requirements are testable and unambiguous.

## Outcome

- ✅ Impact: High - Defines the functional scope for the next development level.
- 🧪 Tests: N/A (Specification phase)
- 📁 Files: Created spec.md, plan.md, tasks.md, and quality checklist.
- 🔁 Next prompts: /sp.plan to design the implementation.
- 🧠 Reflection: The user's constraints were very clear, allowing for a focused specification that avoids scope creep into persistence which belongs in later phases.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
