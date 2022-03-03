def seperate_by_commas(list) -> str: 
    """Utility method used by some build-in validators.
    Joins together lists and seperates strings by commas."""
    return ", ".join(list)


def remove_chars(string: str, chars: str) -> str:
    """Utility method used by some build-in validators.
    Removes all given chars from a string and returns result."""
    for char in chars: 
        string = string.replace(char, "")
    return string
    