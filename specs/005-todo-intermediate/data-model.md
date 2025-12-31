# Data Model: Enhanced Task

## Entity: Task
Represents a todo item with extended metadata for organization and retrieval.

### Attributes
- **id** (int): Unique session-level identifier (Incremental).
- **content** (str): The task description (1-500 chars).
- **status** (str): "complete" or "incomplete".
- **due_date** (Optional[date]): Target completion date (YYYY-MM-DD).
- **priority** (str): "high", "medium", or "low".
- **tags** (list[str]): List of categorization labels.
- **created_at** (datetime): Timestamp for default sorting and stability.

### Validation Rules
- **Date**: Must match YYYY-MM-DD or be None/Empty.
- **Priority**: Must be one of ["high", "medium", "low"].
- **Content**: Non-empty, max 500 characters.
- **Tags**: Case-insensitive, stripped of extra whitespace, no duplicates.

### State Transitions
- **Add**: Initialize with metadata.
- **Toggle Status**: Incomplete <-> Complete.
- **Update**: Modify any attribute.
- **Delete**: Remove from memory.
