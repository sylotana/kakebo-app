def is_positive_number(value: float) -> bool:
    """Checks if a value is a positive number."""
    return isinstance(value, int | float) and value > 0


def is_non_empty_string(value: str) -> bool:
    """Checks that a string is not empty or just spaces."""
    return isinstance(value, str) and bool(value.strip())
