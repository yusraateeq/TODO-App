# Implementation Plan: Advanced Todo Phase I

**Branch**: `006-advanced-todo-phase1` | **Date**: 2025-12-31 | **Spec**: [specs/006-advanced-todo-phase1/spec.md](spec.md)
**Input**: Feature specification from `/specs/006-advanced-todo-phase1/spec.md`

## Summary

The Advanced Level of Phase I enhances the TODO application with recurring tasks (daily, weekly, monthly), precision due datetimes (YYYY-MM-DD HH:MM), and proactive overdue reminders. The technical approach involves updating the `Task` model to use `datetime` objects, extending the `TaskService` to handle auto-rescheduling logic upon task completion, and modifying the CLI to display a pro-active reminders section.

## Technical Context

**Language/Version**: Python 3.12 (as per environment)
**Primary Dependencies**: standard library `datetime`
**Storage**: In-memory (Python `List` in `TaskService`)
**Testing**: `pytest`
**Target Platform**: CLI / Terminal
**Project Type**: Single project
**Performance Goals**: Instant CLI responses (p95 < 50ms)
**Constraints**: No persistence (data lost on exit), no external packages.
**Scale/Scope**: ~10-100 in-memory tasks.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

1. **SDDW**: Following Constitution → Specs → Plan → Tasks. (Pass)
2. **Phase Scoping**: Strictly Phase I (CLI + In-memory). (Pass)
3. **Tech Stack**: Python (Pass). No SQLModel yet as this is Phase I in-memory only.
4. **Independent Testability**: User stories are split by feature. (Pass)

## Project Structure

### Documentation (this feature)

```text
specs/006-advanced-todo-phase1/
├── plan.md              # This file
├── research.md          # Datetime and recurrence logic research
├── data-model.md        # Updated Task entity and transitions
├── quickstart.md        # Steps to test the new CLI features
├── checklists/          # Validation checklists
└── tasks.md             # (Future) Implementation tasks
```

### Source Code (repository root)

```text
todo/
├── models/
│   └── task.py          # Update Task dataclass with Recurrence and Datetime
├── services/
│   └── task_service.py   # Extend with rescheduling and reminder logic
└── cli.py               # (or equivalent) Add reminder display and new inputs
tests/
├── unit/
│   ├── test_recurrence.py
│   └── test_datetime.py
└── integration/
    └── test_reminder_flow.py
```

**Structure Decision**: Extending the existing domain-driven structure (models/services/cli).

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| In-memory `datetime` objects | Requirement for precision and reminders | `str` is insufficient for arithmetic required for recurrence and overdue checks. |
| Auto-task generation | Requirement for recurring tasks | Manual recreation by user defeats the purpose of "Advanced" level automation. |
