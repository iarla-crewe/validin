from validin import InputValidator
from utils import list_as_str, remove_chars


class NewValidator(InputValidator):
    """A generic class for creating custom validators.
        
    Args:
        condition (function): The function that will be ran to check if input is valid. Must return a bool.
        *condition_args (any, optional): Arguments passed into the condition function, eg: min/max values, invalid chars etc.
        invalid_msg (str, optional): Message to be displayed if user enters invalid input.
    """
    _condition: object
    _args: tuple
    _invalid_msg: str

    def __init__(self, condition, *condition_args, invalid_msg: str="") -> None:
        self._condition = condition
        self._args = condition_args
        self._invalid_msg = invalid_msg

    def is_valid(self, input: str) -> bool:
        if not self._args: 
            result = self._condition(input)
        else: 
            result = self._condition(input, *self._args)
        return result

    def get_invalid_msg(self) -> str:
        return self._invalid_msg


class IsNaturalNum(InputValidator):
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


class IsLetters(InputValidator):
    """Input validator that returns true if the input contains only letters and spaces"""
    def is_valid(self, input: str) -> bool:
        return input.replace(" ", "").isalpha()

    def get_invalid_msg(self) -> str:
        return "Must only contain letters"


class IsLettersAndSymbols(InputValidator):
    """Input validator that returns true if the input contains only letters, spaces, and the given symbols
    
    Args:
        *symbols (str): The special characters allowed in the input
    """
    symbols: tuple[str]
    def __init__(self, *symbols: str) -> None:
        self.symbols = symbols

    def is_valid(self, input: str) -> bool:
        input = remove_chars(input, *self.symbols)
        return input.replace(" ", "").isalpha()

    def get_invalid_msg(self) -> str:
        return f"Must only contain letters and {list_as_str(self.symbols)}"


class IsAlphanumeric(InputValidator):
    """Input validator that returns true if the input contains only letters, numbers and spaces"""
    def is_valid(self, input: str) -> bool:
        return input.replace(" ", "").isalnum()

    def get_invalid_msg(self) -> str:
        return "Must only contain letters or numbers"


class IsAlphanumericAndSymbols(InputValidator):
    """Input validator that returns true if the input contains only 
        letters, numbers, spaces, and the given symbols
        
        Args:
            *symbols (str): The special characters allowed in the input
        """
    symbols: tuple[str]
    def __init__(self, *symbols: str) -> None:
        self.symbols = symbols

    def is_valid(self, input: str) -> bool:
        input = remove_chars(input, *self.symbols)
        return input.replace(" ", "").isalnum()

    def get_invalid_msg(self) -> str:
        return f"Must only contain letters, numbers and {list_as_str(self.symbols)}"


class IsOption(InputValidator):
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
        return f"Must be one of the following: {list_as_str(self.options)}"
