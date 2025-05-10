def is_positive_number(value: str) -> bool:
    """Checks if a value is a positive number."""
    try:
        number = float(value)
        return number > 0
    except ValueError:
        return False


def is_non_empty_string(value: str) -> bool:
    """Checks that a string is not empty or just spaces."""
    return isinstance(value, str) and bool(value.strip())
