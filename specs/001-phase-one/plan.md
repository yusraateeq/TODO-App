# Implementation Plan: Phase I - Todo Console Application

**Branch**: `001-phase-one` | **Date**: 2025-12-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/001-phase-one/spec.md`

## Summary

Phase I implements a simple in-memory Python console application for task management. The application provides a menu-driven CLI interface for adding, viewing, updating, deleting, and marking tasks complete/incomplete. All data is stored in memory and lost when the application exits.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: Standard library only (no external dependencies)
**Storage**: In-memory Python data structures (list/dict)
**Testing**: pytest (unit tests for models and services)
**Target Platform**: Terminal/Console (Linux, macOS, Windows)
**Project Type**: Single console application
**Performance Goals**: Immediate response (<1 second for all operations)
**Constraints**: No persistence, single user, no network
**Scale/Scope**: Single user session, <1000 tasks per session

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Spec-Driven Development | PASS | Plan derived strictly from approved spec |
| II. Agent Behavior Rules | PASS | No new features introduced |
| III. Phase Governance | PASS | No future-phase concepts included |
| IV. Technology Stack | PASS | Using Python standard library only |
| V. Quality Principles | PASS | Clean architecture with separation of concerns |

## Project Structure

### Documentation (this feature)

```text
specs/001-phase-one/
├── plan.md              # This file (/sp.plan command output)
├── spec.md              # Feature specification
├── research.md          # Technical decisions and research
├── data-model.md        # Entity and data structure design
└── tasks.md             # Implementation tasks (/sp.tasks command)
```

### Source Code (repository root)

```text
todo.py                 # Main application entry point
todo/
├── __init__.py
├── models/
│   └── task.py         # Task data class
├── services/
│   └── task_service.py # Business logic for task operations
└── cli/
    ├── __init__.py
    ├── menu.py         # Menu display and navigation
    └── inputs.py       # User input handling and validation
```

**Structure Decision**: Using a package-based structure (`todo/`) with clear separation between models (data), services (logic), and CLI (presentation). This adheres to clean architecture principles while keeping the application simple.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |

## Research Decisions

### Application Structure

**Decision**: Package-based structure with separate modules for models, services, and CLI.

**Rationale**:
- Clean separation of concerns (data, logic, presentation)
- Follows constitution quality principle V: Clean architecture
- Single responsibility per module
- Testable code with dependency injection

**Alternatives Considered**:
- Single file (todo.py): Rejected - violates separation of concerns, hard to test
- Multiple files without package: Rejected - less organized, potential namespace conflicts

### In-Memory Storage

**Decision**: Use a Python dictionary (`dict[int, Task]`) for task storage, keyed by task ID.

**Rationale**:
- O(1) lookup time for all operations
- Simple to implement and understand
- Natural fit for the ID-based access pattern
- Easy to iterate for list display

**Alternatives Considered**:
- List: Rejected - O(n) lookup for updates/deletes, less intuitive API
- Set: Rejected - cannot store task content alongside ID

### Task Identification

**Decision**: Auto-incrementing integer IDs starting from 1.

**Rationale**:
- Simple and predictable for users
- Matches spec assumptions
- Easy to implement with a counter variable
- Familiar mental model (1-based indexing)

**Alternatives Considered**:
- UUID: Rejected - too complex for in-memory only, harder for users to type
- Timestamp-based: Rejected - ugly IDs, potential collisions
- Skip IDs on delete: Rejected - spec says IDs remain consistent

### CLI Control Flow

**Decision**: While loop with numbered menu options, input() for user interaction.

**Rationale**:
- Simple and familiar console interaction pattern
- Easy for users to understand and navigate
- No external dependencies required
- Clear exit path (option 7)

**Alternatives Considered**:
- argparse: Rejected - command-line flags don't fit "menu-based" requirement
- click/typer: Rejected - external dependency, overkill for simple menu
- curses: Rejected - platform-specific, too complex

### Separation of Responsibilities

**Decision**: Three-layer architecture:
- Models: Pure data (Task dataclass)
- Services: Business logic (TaskService class)
- CLI: Presentation (Menu class, input functions)

**Rationale**:
- Each layer has single responsibility
- Easy to test models and services without CLI
- Changes to one layer don't affect others
- Follows SOLID principles

### Error Handling Strategy

**Decision**: Custom exception classes with try/except blocks and user-friendly messages.

**Rationale**:
- Clear error taxonomy (TaskNotFoundError, InvalidInputError)
- User-friendly messages that explain how to fix issues
- Separates error detection from error presentation
- Testable error cases

**Error Categories**:
- InvalidInputError: Malformed or empty task content
- TaskNotFoundError: Reference to non-existent task ID
- InvalidMenuChoiceError: Non-numeric or out-of-range menu selection

## Data Model

### Task Entity

```python
@dataclass
class Task:
    id: int
    content: str
    status: str  # "complete" or "incomplete"
    created_at: datetime
    updated_at: datetime
```

### Validation Rules

- content: 1-500 characters, required, non-empty after strip
- status: must be "complete" or "incomplete"
- id: positive integer, unique within session

### State Transitions

- `incomplete` → `complete` (mark complete)
- `complete` → `incomplete` (mark incomplete)
- Both transitions are idempotent

## Implementation Notes

### TaskService API

```python
class TaskService:
    def add_task(content: str) -> Task
    def get_all_tasks() -> List[Task]
    def update_task(task_id: int, new_content: str) -> Task
    def delete_task(task_id: int) -> None
    def mark_complete(task_id: int) -> Task
    def mark_incomplete(task_id: int) -> Task
    def get_task(task_id: int) -> Task | None
```

### Menu Options

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit

### File Locations

| Component | Path |
|-----------|------|
| Entry point | `todo.py` |
| Task model | `todo/models/task.py` |
| Task service | `todo/services/task_service.py` |
| CLI menu | `todo/cli/menu.py` |
| Input handling | `todo/cli/inputs.py` |
| Tests | `tests/` |
