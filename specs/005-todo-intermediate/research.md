# Research: Implementation Logic for Intermediate Todo Features

## Decision: Data Structure
- **Choice**: Use a Python `dataclass` for the `Task` model.
- **Rationale**: Provides clear structure, type hinting, and easy default values (like priority="medium").
- **Alternatives**: Dictionary (too loose, harder to validate), custom Class (more boilerplate than dataclass).

## Decision: Date Handling
- **Choice**: Use `datetime.date.fromisoformat()` for validation and storage.
- **Rationale**: Built-in Python support for YYYY-MM-DD.
- **Validation**: Strict try-except block to catch `ValueError` for incorrect formats.

## Decision: Sorting Logic
- **Choice**: Multi-key sorting using `list.sort(key=...)` with a custom priority mapping.
- **Rationale**: Efficient and built-in. Priority mapping: `{"high": 0, "medium": 1, "low": 2}` to ensure high appears first when sorting ascending.

## Decision: Search & Filter Performance
- **Choice**: Simple list comprehensions for in-memory filtering.
- **Rationale**: O(n) is perfectly acceptable for the small scale (thousands of tasks) of a console application session.
