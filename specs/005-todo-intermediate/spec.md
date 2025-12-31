# Feature Specification: Evolution of Todo - Intermediate Level (Phase I)

**Feature Branch**: `005-todo-intermediate`
**Created**: 2025-12-31
**Status**: Draft
**Input**: User description: "Create the Intermediate Level specification for Phase I of the "Evolution of Todo" project. Required Intermediate Features (build directly on Basic Level): Due Dates, Priority, Tags/Categories, Search Tasks, Filter Tasks, Sort Tasks. Constraints: In-memory only, no persistence, no database, no web, etc."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Task Enrichment (Due Dates & Priority) (Priority: P1)

As a user, I want to add metadata like due dates and priorities to my tasks so that I can better organize my work and understand what is most important.

**Why this priority**: Core organization requires more than just a title; dates and priority are the foundation of effective task management.

**Independent Test**: Can be fully tested by creating a task with a due date and priority and verifying they are stored and displayed correctly in the session.

**Acceptance Scenarios**:

1. **Given** the user is adding a task, **When** the user provides a due date "2025-12-31" and priority "high", **Then** the task list shows the task with that date and priority.
2. **Given** the user is adding a task, **When** the user provides "None" or leaves the date blank, **Then** the task has no due date assigned.
3. **Given** the user provides an invalid date format, **When** the user enters "31-12-2025", **Then** the system displays a formatting error and asks for re-entry.

---

### User Story 2 - Task Categorization (Tags) (Priority: P1)

As a user, I want to assign multiple tags to my tasks so that I can group related items across different categories.

**Why this priority**: Tags allow for flexible grouping (e.g., "work" and "urgent") which complements linear priority.

**Independent Test**: Can be fully tested by adding multiple tags to a task and verifying they appear as a list when viewing task details.

**Acceptance Scenarios**:

1. **Given** the user is adding or editing a task, **When** the user provides tags "work, personal, urgent", **Then** the task is associated with all three tags as a list.
2. **Given** a task with tags, **When** the user views the task list, **Then** the tags are displayed clearly alongside the task description.

---

### User Story 3 - Search & Filter (Priority: P2)

As a user, I want to find specific tasks using keywords and filter the list based on attributes like status or priority.

**Why this priority**: As lists grow, finding specific items becomes difficult without search and filter capabilities.

**Independent Test**: Can be fully tested by creating a set of varied tasks and performing keyword searches or applying filters for "high" priority or "complete" status.

**Acceptance Scenarios**:

1. **Given** multiple tasks exist with different tags and descriptions, **When** the user searches for "groceries", **Then** only tasks containing that word in the title, description, or tags are shown.
2. **Given** a mixed list of tasks, **When** the user filters by priority "high", **Then** only high-priority tasks are displayed.
3. **Given** no tasks match a filter/search, **When** the user executes the query, **Then** the system displays a "No matching tasks found" message.

---

### User Story 4 - Sorting (Priority: P2)

As a user, I want to sort my task list by due date or priority so that I can see the most pressing items at the top.

**Why this priority**: Sorting allows users to dynamically reorganize their view without changing the underlying data.

**Independent Test**: Can be fully tested by listing tasks with different due dates and verifying they appear in chronological order when sorted.

**Acceptance Scenarios**:

1. **Given** tasks with different due dates, **When** the user sorts by "due date", **Then** tasks with earliest dates appear first (tasks with no date appear last).
2. **Given** tasks with different priorities, **When** the user sorts by "priority", **Then** "high" priority tasks appear before "medium", which appear before "low".

---

### Edge Cases

- **Invalid Date Formats**: User inputs nonsense strings like "yesterday" or "2025/12/31" instead of the required YYYY-MM-DD.
- **Empty Search Results**: User searches for a term or tag that exists in no tasks.
- **Sort Stability**: How the system handles sorting when multiple tasks have the same priority or due date (should fall back to creation time).
- **Tag Formatting**: Handling excessive whitespace or duplicate tags (e.g., "work , work" should become just ["work"]).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow assigning an optional due date to each task in YYYY-MM-DD format.
- **FR-002**: System MUST allow assigning exactly one priority level per task: high, medium, or low (default: medium).
- **FR-003**: System MUST allow assigning zero or more tags (list of strings) to each task.
- **FR-004**: System MUST allow searching tasks by keyword across title, description, and tags.
- **FR-005**: System MUST allow filtering the task list by status, priority, tag, or due date.
- **FR-006**: System MUST allow sorting the task list by due date, priority, creation time, or title.
- **FR-007**: System MUST validate date inputs and priority levels at the time of entry.
- **FR-008**: System MUST maintain all Basic Level operations (add, list, update, delete, status toggle).
- **FR-009**: System MUST support "None" or blank for due dates.
- **FR-010**: System MUST handle "no results found" scenarios for search and filter gracefully.

### Key Entities *(include if feature involves data)*

- **Task (Enhanced)**:
  - **id**: (Basic) Unique session-level integer.
  - **title/content**: (Basic) String.
  - **status**: (Basic) Complete/Incomplete.
  - **due_date**: Date object or String (YYYY-MM-DD), nullable.
  - **priority**: Enum (High, Medium, Low), default Medium.
  - **tags**: List of Strings.
  - **created_at**: Timestamp (for sorting fallback).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can apply any filter or sort operation and see updated results in under 1 second (given in-memory processing).
- **SC-002**: 100% of invalid date formats are caught by validation with a helpful error message.
- **SC-003**: Search queries return all matches across title, description, and tags with 100% accuracy.
- **SC-004**: Displayed list shows due date, priority, and tags in a clean, readable format within the terminal's width limits.
- **SC-005**: All data remains consistent and accessible throughout the session but is correctly wiped on exit as per constraints.
