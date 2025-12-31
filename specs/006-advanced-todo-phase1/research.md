# Research: Advanced Todo Phase I

**Feature**: Advanced Todo Phase I
**Date**: 2025-12-31

## Decision: Datetime Handling
- **Choice**: Use Python's `datetime` module for all time-related operations.
- **Rationale**: Standard library requirement, lightweight, and perfectly suited for in-memory operations.
- **Alternatives considered**: `time` module (too low level), `dateutil` (external dependency, prohibited).

## Decision: Recurrence Logic
- **Choice**: Handled in the `TaskService` during the `mark_complete` operation.
- **Rationale**: Centralizes business logic. If a task has a recurrence type, the service will instantiate a new task with an offset `due_datetime`.
- **Logic**:
    - `daily`: `due_datetime + timedelta(days=1)`
    - `weekly`: `due_datetime + timedelta(weeks=1)`
    - `monthly`: Use a custom helper to add exactly one month (handling variance in days/month).

## Decision: Reminder Simulation
- **Choice**: Passive check during the main menu refresh cycle.
- **Rationale**: Meets the requirement of "console simulation" without needing background threads or async loops which are out of scope for Phase I.
- **Implementation**: The `CLI` controller will call a `get_reminders()` method in `TaskService` every time the main menu is printed.

## Decision: Internal Data Structure
- **Choice**: Update the `Task` model class to include `recurrence_type` (String) and `due_datetime` (datetime).
- **Rationale**: Minimal change to existing architecture while providing all necessary fields.
- **Persistence**: Strictly in-memory `List` in `TaskService`.
