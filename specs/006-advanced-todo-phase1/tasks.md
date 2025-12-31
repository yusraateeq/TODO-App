# Implementation Tasks: Advanced Todo Phase I

## Overview
This document breaks down the Advanced Level features into atomic, testable tasks. All implementation remains strictly in-memory and follows Phase I constraints.

---

### ADV-01: Update Task Model Data Structure
- [x] **Description**: Add `recurrence_type` Enum/Attribute and migrate `due_date` from `str` to `datetime` objects.
- **Preconditions**: Base Task model exists.
- **Expected Outcome**: Task model supports full datetime precision and recurrence metadata.
- **Files/Functions**:
    - `todo/models/task.py`: Update `Task` dataclass. Add `RecurrenceType` Enum. Change `due_date` type.
- **Reference**: Spec section "Key Entities"

### ADV-02: Implement Datetime Parsing and Validation
- [x] **Description**: Add utility for converting `YYYY-MM-DD HH:MM` strings to `datetime` objects with validation.
- **Preconditions**: ADV-01 complete.
- **Expected Outcome**: Robust parsing for full datetime inputs.
- **Files/Functions**:
    - `todo/services/task_service.py`: Add internal datetime validation/parsing logic.
- **Reference**: Spec section "Validation Rules"

### ADV-03: Extend TaskService for Recurrence and Datetime
- [x] **Description**: Update `add_task` and `update_task_metadata` to accept and store recurrence types and `datetime` objects.
- **Preconditions**: ADV-01, ADV-02 complete.
- **Expected Outcome**: Service layer correctly handles new advanced fields.
- **Files/Functions**:
    - `todo/services/task_service.py`: `add_task`, `update_task_metadata`.
- **Reference**: FR-001, FR-003

### ADV-04: Implement Auto-Reschedule Logic
- [x] **Description**: Modify `mark_complete` in `TaskService` to detect recurring tasks and create the next occurrence.
- **Preconditions**: ADV-03 complete.
- **Expected Outcome**: Marking a daily/weekly/monthly task complete automatically adds a new instance.
- **Files/Functions**:
    - `todo/services/task_service.py`: `mark_complete`.
- **Reference**: FR-002, User Story 1

### ADV-05: Implement Overdue Detection and Reminder Logic
- [x] **Description**: Create a method in `TaskService` to retrieve tasks where `due_datetime < datetime.now()`.
- **Preconditions**: ADV-03 complete.
- **Expected Outcome**: Capability to isolate overdue tasks for reporting.
- **Files/Functions**:
    - `todo/services/task_service.py`: New `get_overdue_tasks()` method.
- **Reference**: FR-004

### ADV-06: Enhance CLI input for Advanced Features
- [x] **Description**: Update CLI prompts to ask for recurrence and full datetime (with example format).
- **Preconditions**: ADV-03 complete.
- **Expected Outcome**: User can interactively set recurrence and time.
- **Files/Functions**:
    - `todo.py`: Update task entry flow.
- **Reference**: User Story 2

### ADV-07: Implement CLI Reminders Section
- [x] **Description**: Update main menu logic to display the Overdue Reminders section before the options list.
- **Preconditions**: ADV-05 complete.
- **Expected Outcome**: High-visibility overdue tasks on menu load.
- **Files/Functions**:
    - `todo.py`: Menu rendering logic.
- **Reference**: FR-004, User Story 2

### ADV-08: Update Search and Filter for Datetime
- [x] **Description**: Refactor `filter_tasks` and `search_tasks` to handle datetime matches and ranges.
- **Preconditions**: ADV-03 complete.
- **Expected Outcome**: Filters work correctly with new object types.
- **Files/Functions**:
    - `todo/services/task_service.py`: `filter_tasks`, `search_tasks`.
- **Reference**: FR-005

### ADV-09: Update Sort Logic for Datetime Objects
- [x] **Description**: Refactor `sort_tasks` to correctly compare `datetime` objects instead of strings.
- **Preconditions**: ADV-03 complete.
- **Expected Outcome**: Sorting by due date is accurate down to the minute.
- **Files/Functions**:
    - `todo/services/task_service.py`: `sort_tasks`.
- **Reference**: FR-005

### ADV-10: Update Task Listing Display
- [x] **Description**: Enhance the string representation of tasks to show "Recurrence" and full "Due Datetime".
- **Preconditions**: ADV-01 complete.
- **Expected Outcome**: `list` command shows all metadata clearly.
- **Files/Functions**:
    - `todo/models/task.py`: `__str__`.
- **Reference**: User Story 2, Requirements
