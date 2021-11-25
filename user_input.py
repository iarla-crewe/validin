"""
Use get_input to get valid user input

Input validators:
- IsNaturalNum
- IsNaturalNumLessThan
- IsLetters
- IsLettersAndSymbols
- IsAlphanumeric
- IsAlphanumericAndSymbols
- IsOption

To create a new validator, just create a class that inherits from InputCondition
"""


from abc import ABC, abstractmethod


def _list_as_str(list: list) -> str: 
    """Joins together options into a string, seperated by commas"""
    return ", ".join(list)


def _remove_chars(string: str, *chars: str) -> str:
    """Removes all given chars from a string and returns result"""
    for char in chars: 
        string = string.replace(char, "")
    return string

class InputCondition(ABC):
    """A abstract class for conditions that validate user input."""
    @abstractmethod
    def is_valid(self, input: str) -> bool:
        """Returns true if the inputs passes the class's condition"""
        pass

    @abstractmethod
    def get_invalid_msg(self) -> str:
        """Returns a message to display if input is invalid"""
        pass


#region Input validators

class IsNaturalNum(InputCondition):
    """Input validator that returns true if the input is a natural number"""
    def is_valid(self, input: str) -> bool:
        return (input.isdigit() and float(input).is_integer and int(input) > 0)

    def get_invalid_msg(self) -> str:
        return "Must be a whole number greater than 0"


class IsNaturalNumLessThan(IsNaturalNum):
    """Input validator that returns true if the input is a natural number less than a given limit
    
    Args:
        limit (str): Input must be lower than this number
    """
    limit: int
    def __init__(self, limit: int) -> None:
        self.limit = limit

    def is_valid(self, input: str) -> bool:
        return (super().is_valid(input) and int(input) < self.limit)

    def get_invalid_msg(self) -> str:
        return f"Must be a whole number between 0 and {self.limit}"


class IsLetters(InputCondition):
    """Input validator that returns true if the input contains only letters and spaces"""
    def is_valid(self, input: str) -> bool:
        return input.replace(" ", "").isalpha()

    def get_invalid_msg(self) -> str:
        return "Must only contain letters"


class IsLettersAndSymbols(InputCondition):
    """Input validator that returns true if the input contains only letters, spaces, and the given symbols
    
    Args:
        *symbols (str): The special characters allowed in the input
    """
    symbols: tuple[str]
    def __init__(self, *symbols: str) -> None:
        self.symbols = symbols

    def is_valid(self, input: str) -> bool:
        input = _remove_chars(input, *self.symbols)
        return input.replace(" ", "").isalpha()

    def get_invalid_msg(self) -> str:
        return f"Must only contain letters and {_list_as_str(self.symbols)}"


class IsAlphanumeric(InputCondition):
    """Input validator that returns true if the input contains only letters, numbers and spaces"""
    def is_valid(self, input: str) -> bool:
        return input.replace(" ", "").isalnum()

    def get_invalid_msg(self) -> str:
        return "Must only contain letters or numbers"


class IsAlphanumericAndSymbols(InputCondition):
    """Input validator that returns true if the input contains only 
        letters, numbers, spaces, and the given symbols
        
        Args:
            *symbols (str): The special characters allowed in the input
        """
    symbols: tuple[str]
    def __init__(self, *symbols: str) -> None:
        self.symbols = symbols

    def is_valid(self, input: str) -> bool:
        input = _remove_chars(input, *self.symbols)
        return input.replace(" ", "").isalnum()

    def get_invalid_msg(self) -> str:
        return f"Must only contain letters, numbers and {_list_as_str(self.symbols)}"


class IsOption(InputCondition):
    """Input validator that returns true if the input is exactly one of the given options
    
    Args:
        *options (str): The list of options that the input must match
    """
    options: tuple[str]
    def __init__(self, *options: str) -> None:
        self.options = options

    def is_valid(self, input: str) -> bool:
        return (input in self.options)

    def get_invalid_msg(self) -> str:
        return f"Must be one of the following: {_list_as_str(self.options)}"


#endregion


def get_input(prompt: str, condition: InputCondition, *condition_args, bold_input: bool=True) -> str:
    """Gets the users input and only returns one that passes the input condition
    
    Args:
        prompt (str): A string written to standard output in front of the user input.
        condition (InputCondition): An InputCondition subclass used to check if the inputted data is valid.
        *condition_args (any, optional): Arguments passed into the InputCondition.
        bold_input (bool, optional): Formats the inputted text to be bold. Defaults to True.
    """
    BOLD_START = "\033[1m"                                      # Chars that start bold text in standard output
    BOLD_END = "\033[0m"                                        # Chars that end formatting in standard output

    format = ""
    if bold_input: format = BOLD_START

    while True:
        raw_input: str = input(f"{prompt}{format}")             # Get and format user's input
        print(BOLD_END, end="")                                 # End input formatting
        if condition.is_valid(raw_input):                       # Only return if input is valid
            return raw_input
        print(f"Invalid Input: {condition.get_invalid_msg()}")  # Print message if invalid
