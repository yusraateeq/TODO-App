# Research: Phase I - Todo Console Application

This document captures technical decisions made during the planning phase.

## Application Structure

**Decision**: Package-based structure with separate modules for models, services, and CLI.

**Rationale**:
- Clean separation of concerns (data, logic, presentation)
- Follows constitution quality principle V: Clean architecture
- Single responsibility per module
- Testable code with dependency injection

**Alternatives Considered**:
- Single file (todo.py): Rejected - violates separation of concerns, hard to test
- Multiple files without package: Rejected - less organized, potential namespace conflicts

## In-Memory Storage

**Decision**: Use a Python dictionary (`dict[int, Task]`) for task storage, keyed by task ID.

**Rationale**:
- O(1) lookup time for all operations
- Simple to implement and understand
- Natural fit for the ID-based access pattern
- Easy to iterate for list display

**Alternatives Considered**:
- List: Rejected - O(n) lookup for updates/deletes, less intuitive API
- Set: Rejected - cannot store task content alongside ID

## Task Identification

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

## CLI Control Flow

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

## Error Handling Strategy

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

## Python Version Selection

**Decision**: Python 3.11+

**Rationale**:
- Standard library datetime timezone awareness improvements
- Better error messages and tracebacks
- Improved performance
- dataclass stability

## Code Organization Pattern

**Decision**: Following clean architecture with three layers:

1. **Models Layer** (`todo/models/task.py`):
   - Pure data classes
   - No business logic
   - Type validation in __post_init__

2. **Services Layer** (`todo/services/task_service.py`):
   - Business logic implementation
   - Manages in-memory storage
   - Returns models to CLI layer

3. **CLI Layer** (`todo/cli/*.py`):
   - User interaction handling
   - Input validation
   - Output formatting
   - Calls services, catches exceptions, displays results

This separation ensures:
- Models can be tested independently (no CLI dependencies)
- Services can be tested with mock CLI
- CLI changes don't affect business logic
