---
description: "Task list template for feature implementation"
---

# Tasks: Phase I - Todo Console Application

**Input**: Design documents from `specs/001-phase-one/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md

## Format: `[ID] [P?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

---

## Phase 1: Project Setup

**Purpose**: Initialize project structure and configuration

- [x] T001 Create todo package directory structure `todo/`, `todo/models/`, `todo/services/`, `todo/cli/`
- [x] T002 [P] Create `todo/__init__.py`, `todo/models/__init__.py`, `todo/services/__init__.py`, `todo/cli/__init__.py`
- [x] T003 [P] Create `tests/` directory and `tests/__init__.py`
- [x] T004 [P] Create `requirements.txt` with pytest (for testing)

**Checkpoint**: Project structure ready for implementation

---

## Phase 2: Core Data Model

**Purpose**: Define Task entity and exceptions (prerequisite for all other tasks)

**CRITICAL**: All user story work depends on this phase

- [x] T005 Create `todo/exceptions.py` with TodoError, TaskNotFoundError, InvalidInputError, InvalidMenuChoiceError
- [x] T006 Create `todo/models/task.py` with TaskStatus enum and Task dataclass (see data-model.md)

**Checkpoint**: Core data model complete - user story implementation can begin

---

## Phase 3: Task Service Layer

**Purpose**: Implement business logic and in-memory storage

- [x] T007 Create `todo/services/task_service.py` with TaskService class (see data-model.md for API)

**Checkpoint**: Service layer complete - all operations ready for CLI integration

---

## Phase 4: CLI - Input Validation

**Purpose**: User input handling and validation utilities

- [x] T008 Create `todo/cli/inputs.py` with functions:
  - `get_task_content()` - prompt for and validate task content (1-500 chars)
  - `get_task_id()` - prompt for and validate positive integer
  - `get_menu_choice()` - prompt for and validate menu selection (1-7)

**Checkpoint**: Input validation complete - ready for menu integration

---

## Phase 5: CLI - Menu System

**Purpose**: Menu display and user interaction

- [x] T009 Create `todo/cli/menu.py` with Menu class:
  - `display_menu()` - print menu options (see data-model.md contract)
  - `display_tasks(tasks)` - format and display task list (see data-model.md contract)
  - `display_message(msg)` - print informational messages
  - `display_error(error)` - print error messages

**Checkpoint**: Menu system complete - ready for application integration

---

## Phase 6: Application Entry Point

**Purpose**: Main entry point and menu loop integration

- [x] T010 Create `todo.py` at repository root:
  - Initialize TaskService
  - Display welcome message
  - Run menu loop until exit (option 7)
  - Handle all menu options by calling TaskService methods
  - Display goodbye message on exit

**Checkpoint**: Application core complete - all features integrated

---

## Phase 7: User Story 1 - Add Task

**Goal**: Users can add new tasks (US1 from spec.md)

**Independent Test**: Add a task, view list, verify task appears

- [x] T011 Implement add task flow in `todo.py`:
  - Call `get_task_content()` to get task description
  - Call `task_service.add_task(content)`
  - Display success message with new task ID

**Checkpoint**: Add task feature complete and testable

---

## Phase 8: User Story 2 - View Task List

**Goal**: Users can see all their tasks (US2 from spec.md)

**Independent Test**: Add multiple tasks, view list, verify all appear

- [x] T012 Implement view tasks flow in `todo.py`:
  - Call `task_service.get_all_tasks()`
  - Call `menu.display_tasks(tasks)` or display empty message if no tasks

**Checkpoint**: View tasks feature complete and testable

---

## Phase 9: User Story 3 - Update Task

**Goal**: Users can modify task content (US3 from spec.md)

**Independent Test**: Add task, update it, verify change in list

- [x] T013 Implement update task flow in `todo.py`:
  - Call `get_task_id()` to get target task ID
  - Call `get_task_content()` to get new content
  - Call `task_service.update_task(task_id, content)`
  - Handle TaskNotFoundError and display error

**Checkpoint**: Update task feature complete and testable

---

## Phase 10: User Story 4 - Delete Task

**Goal**: Users can remove tasks (US4 from spec.md)

**Independent Test**: Add task, delete it, verify it no longer appears

- [x] T014 Implement delete task flow in `todo.py`:
  - Call `get_task_id()` to get target task ID
  - Call `task_service.delete_task(task_id)`
  - Handle TaskNotFoundError and display error

**Checkpoint**: Delete task feature complete and testable

---

## Phase 11: User Story 5 - Mark Complete

**Goal**: Users can mark tasks as complete (US5 from spec.md)

**Independent Test**: Add task, mark complete, verify status change

- [x] T015 Implement mark complete flow in `todo.py`:
  - Call `get_task_id()` to get target task ID
  - Call `task_service.mark_complete(task_id)`
  - Handle TaskNotFoundError and display error

**Checkpoint**: Mark complete feature complete and testable

---

## Phase 12: User Story 6 - Mark Incomplete

**Goal**: Users can reopen completed tasks (US6 from spec.md)

**Independent Test**: Add task, mark complete, mark incomplete, verify status change

- [x] T016 Implement mark incomplete flow in `todo.py`:
  - Call `get_task_id()` to get target task ID
  - Call `task_service.mark_incomplete(task_id)`
  - Handle TaskNotFoundError and display error

**Checkpoint**: All user story features complete

---

## Phase 13: Unit Tests

**Purpose**: Verify model, service, and CLI components work correctly

- [x] T017 Create `tests/test_task.py`:
  - Test Task dataclass creation
  - Test TaskStatus enum
  - Test content validation (empty, too long)
- [x] T018 Create `tests/test_task_service.py`:
  - Test add_task creates task with correct ID
  - Test get_all_tasks returns sorted list
  - Test update_task changes content
  - Test delete_task removes task
  - Test mark_complete changes status
  - Test mark_incomplete changes status
  - Test TaskNotFoundError raised for invalid ID
- [x] T019 Create `tests/test_inputs.py`:
  - Test get_task_content validation
  - Test get_task_id validation
  - Test get_menu_choice validation

**Checkpoint**: All unit tests pass

---

## Dependencies & Execution Order

### Phase Dependencies

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Setup (1) | None | Data Model |
| Data Model (2) | Setup | Service |
| Service (3) | Data Model | CLI Input |
| CLI Input (4) | Service | CLI Menu |
| CLI Menu (5) | CLI Input | Entry Point |
| Entry Point (6) | CLI Menu | User Stories |
| User Stories (7-12) | Entry Point | Tests |
| Tests (13) | User Stories | Complete |

### Within Each User Story

- Model → Service → CLI integration → Story complete
- Commit after each task or logical group

### Parallel Opportunities

- Setup tasks (T001-T004) can run in parallel
- Test files (T017-T019) can be written in parallel with implementation
- Different user stories can be tested independently

---

## Implementation Strategy

### Recommended Order

1. Complete Phases 1-6 (infrastructure and core components)
2. Complete Phases 7-12 (all user stories)
3. Complete Phase 13 (tests)

### Validation Checkpoints

After each phase, verify:
- Code compiles without errors
- Tests for completed phases pass
- Manual testing of completed features

---

## References

- **Spec Reference**: `specs/001-phase-one/spec.md`
- **Plan Reference**: `specs/001-phase-one/plan.md`
- **Data Model Reference**: `specs/001-phase-one/data-model.md`
- **Constitution**: `.specify/memory/constitution.md`
