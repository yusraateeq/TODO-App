---

description: "Task list for Intermediate Level feature implementation in Phase I"

---

# Tasks: Todo Intermediate Features (Phase I)

**Input**: Design documents from `/specs/005-todo-intermediate/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md

**Organization**: Tasks are grouped by foundational infrastructure and then by prioritized user stories to ensure incremental delivery and independent testability.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (US1, US2, US3, US4)

---

## Phase 1: Setup & Foundational

**Purpose**: Modularize the project and define the core Task model and validation logic.

**⚠️ CRITICAL**: This foundation must be complete before any user story work begins.

- [X] T001 [P] Create directory structure: `src/core/`, `src/utils/`
- [X] T002 Implement `Task` dataclass in `src/core/models.py` with `due_date`, `priority`, and `tags` (per `data-model.md`)
- [X] T003 Implement date and priority validators in `src/utils/validators.py` (per `plan.md`)
- [X] T004 Create `TaskManager` in `src/core/manager.py` to handle the in-memory collection and unique ID generation
- [X] T005 [P] Setup basic unit tests for model and validators in `tests/unit/`

**Checkpoint**: Foundation ready - task enrichment and retrieval logic can now be implemented.

---

## Phase 2: User Story 1 - Task Enrichment (Due Dates & Priority) (Priority: P1) 🎯 MVP

**Goal**: Allow users to add and update tasks with due dates and priority levels.

**Independent Test**: Create a task with a specific date and priority and verify it displays correctly in the list.

- [X] T006 [US1] Update `add_task` flow in `src/app.py` to prompt for due date and priority
- [X] T007 [US1] Update `update_task` flow in `src/app.py` to allow modifying due date and priority
- [X] T008 [US1] Integrate `validators.py` into the CLI task creation/update loops
- [X] T009 [US1] Enhance task listing display in `src/app.py` to show Due Date and Priority columns

**Checkpoint**: Users can now manage tasks with dates and priority levels.

---

## Phase 3: User Story 2 - Task Categorization (Tags) (Priority: P1)

**Goal**: Support multiple tags per task.

**Independent Test**: Assign "work, urgent" to a task and verify they appear as a list.

- [X] T010 [US2] Update `add_task` and `update_task` in `src/app.py` to accept comma-separated tags
- [X] T011 [US2] Implement tag parsing logic (whitespace stripping, uniqueness) in `src/core/manager.py`
- [X] T012 [US2] Update task display to include tags in the output

**Checkpoint**: Tasks now support flexible categorization via tags.

---

## Phase 4: User Story 3 - Search & Filter (Priority: P2)

**Goal**: Find tasks by keyword or filter by attributes.

**Independent Test**: Search for a keyword found only in tags and verify matching tasks are returned.

- [X] T013 [US3] Implement search logic (keyword matching across title, desc, tags) in `src/core/engine.py`
- [X] T014 [US3] Implement filter logic (by priority, status, tag, or date) in `src/core/engine.py`
- [X] T015 [US3] Add "Search" and "Filter" options to the main CLI menu in `src/app.py`
- [X] T016 [US3] Handle "No matching tasks found" gracefully with a user message

**Checkpoint**: Retrieval functionality is fully operational.

---

## Phase 5: User Story 4 - Sorting (Priority: P2)

**Goal**: Reorder tasks based on due date, priority, or title.

**Independent Test**: Sort a list with mixed priorities and verify "High" tasks are at the top.

- [X] T017 [US4] Implement priority-weighted sorting logic in `src/core/engine.py`
- [X] T018 [US4] Implement due date and title sorting logic in `src/core/engine.py`
- [X] T019 [US4] Add "Sort" option to the CLI menu and implement sort stability (fallback to creation time)

**Checkpoint**: All Intermediate Level features are complete and integrated.

---

## Phase 6: Polish & Final Validation

- [X] T020 Run full integration test of all flows via the CLI
- [X] T021 Validate `quickstart.md` examples against the final implementation
- [X] T022 Final code cleanup and documentation update

---

## Dependencies & Execution Order

1. **Phase 1 (Foundational)**: MUST be completed first.
2. **Phase 2-3 (Enrichment)**: Can be done in parallel once foundation is set.
3. **Phase 4-5 (Retrieval)**: Depend on enrichment metadata being present in the Task model.
4. **Phase 6 (Polish)**: Final step once all stories are complete.
