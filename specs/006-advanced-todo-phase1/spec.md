# Feature Specification: Advanced Todo Phase I

**Feature Branch**: `006-advanced-todo-phase1`
**Created**: 2025-12-31
**Status**: Draft
**Input**: User description: "Create the Advanced Level specification for Phase I of the \"Evolution of Todo\" project. Phase I Scope (remains unchanged): In-memory Python console application only, Single user, No persistence — data lost on exit, Menu-driven CLI. Required Advanced Features: 1. Recurring Tasks – Support repeating tasks (e.g., daily, weekly, monthly); auto-reschedule by creating new instances when marked complete. 2. Due Dates & Time Reminders – Enhance due dates with full datetime (YYYY-MM-DD HH:MM); simulate reminders in console (e.g., list overdue tasks on startup/menu); no actual browser notifications."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Recurring Tasks (Priority: P1)

As a user, I want to create tasks that repeat on a regular schedule (daily, weekly, monthly) so that I don't have to manually recreate common tasks every time I finish them.

**Why this priority**: Core advanced feature that provides significant utility for routine management. It defines the "Advanced" level of the application.

**Independent Test**: Create a task with a "daily" recurrence. Mark it complete. Verify that a new instance of the task is automatically created for the next day.

**Acceptance Scenarios**:

1. **Given** the main menu, **When** I create a new task with recurrence 'daily', **Then** the task should be saved with the recurrence attribute.
2. **Given** an incomplete recurring task, **When** I mark it as complete, **Then** the system should create a NEW task with the same title/description but with the due date advanced by the recurrence period.

---

### User Story 2 - Datetime Due Dates and Reminders (Priority: P2)

As a user, I want to set specific times for my due dates and see reminders for overdue tasks when I start the app or view the menu, so that I can stay on top of time-sensitive commitments.

**Why this priority**: Enhances the intermediate "due date" feature to support precise scheduling and provides pro-active feedback (reminders).

**Independent Test**: Set a task due date to 5 minutes ago. Return to the main menu. Verify that the task is listed in a "Overdue/Upcoming Reminders" section.

**Acceptance Scenarios**:

1. **Given** the task creation flow, **When** I enter a due date in 'YYYY-MM-DD HH:MM' format, **Then** the system should validate and store the full datetime.
2. **Given** the main menu is displayed, **When** there are tasks with due dates in the past, **Then** those tasks should be highlighted as "OVERDUE" in a reminder section before the main options.

---

### Edge Cases

- **Invalid Recurrence**: User enters a string that isn't 'daily', 'weekly', or 'monthly'. System should prompt for re-entry.
- **Invalid Datetime Format**: User enters '2025-13-45' or misses the time. System should display the expected format and ask again.
- **Leap Years/Month Ends**: Setting a monthly task on the 31st. System should handle the next occurrence safely (e.g., Feb 28th/29th). [Assumption: We will use standard library datetime arithmetic which handles month logic].
- **No Overdue Tasks**: Reminder section should be omitted or state "No overdue tasks" if the list is clean.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST support specifying recurrence types: 'none', 'daily', 'weekly', 'monthly'.
- **FR-002**: System MUST automatically generate a new task instance when a recurring task (recurrence != 'none') is marked as complete.
- **FR-003**: System MUST support due dates with precision down to the minute (YYYY-MM-DD HH:MM).
- **FR-004**: System MUST display a list of overdue tasks (due date < current time) at the top of the main menu.
- **FR-005**: System MUST preserve all existing search, filter, and sort capabilities, updated to work with datetime objects.
- **FR-006**: System MUST persist all data strictly in-memory (no file I/O).

### Key Entities *(include if feature involves data)*

- **Task**:
    - Title (String)
    - Description (String)
    - Priority (Enum: Low, Medium, High)
    - Status (Enum: Incomplete, Done)
    - Due Date (Datetime: YYYY-MM-DD HH:MM, optional)
    - Recurrence (Enum: None, Daily, Weekly, Monthly)
    - Created At (Datetime)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can set up a recurring task in under 30 seconds from the main menu.
- **SC-002**: 100% of expired tasks are correctly listed in the "Reminders" section on startup/refresh.
- **SC-003**: The system correctly calculates the next occurrence for all three recurrence types (daily, weekly, monthly) 100% of the time.
- **SC-004**: No data is written to disk at any point during execution.
