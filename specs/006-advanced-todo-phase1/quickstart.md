# Quickstart: Advanced Todo Phase I

## Testing Recurring Tasks
1. Start the app.
2. Create a task with recurrence set to `daily`.
3. Set the due date + time.
4. Mark the task as `complete`.
5. Verify that a new instance of the task appears in the list with a due date exactly 24 hours after the original.

## Testing Reminders
1. Create a task with a due date 1 minute in the past.
2. Return to the main menu.
3. Verify that the task is highlighted in a special "OVERDUE TASKS" section at the top of the menu.

## Testing Datetime Validation
1. Attempt to create a task with an invalid date string (e.g., `2025-13-01`).
2. Verify the system shows an error and prompts for the correct `YYYY-MM-DD HH:MM` format.
