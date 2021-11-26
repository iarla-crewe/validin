def list_as_str(list: list) -> str: 
    """Utility method used by some build-in validators.
    Joins together options into a string, seperated by commas."""
    return ", ".join(list)


def remove_chars(string: str, *chars: str) -> str:
    """Utility method used by some build-in validators.
    Removes all given chars from a string and returns result."""
    for char in chars: 
        string = string.replace(char, "")
    return string
    