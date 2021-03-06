from validin.validin import InputValidator
from validin.utils import seperate_by_commas, remove_chars


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
    """Input validator that returns true if the input is a natural number. Ignores whitespace on either side of input"""
    def is_valid(self, input: str) -> bool:
        input = input.strip()
        return (input.isdigit() and float(input).is_integer and int(input) > 0)

    def get_invalid_msg(self) -> str:
        return "Must be a whole number greater than 0"


class IsNaturalNumLessThan(IsNaturalNum):
    """Input validator that returns true if the input is a natural number less than a given limit. Ignores whitespace on either side of input
    
    Args:
        limit (str): Input must be lower than this number
    """
    limit: int
    def __init__(self, limit: int) -> None:
        try:
            self.limit = float(limit)
        except:
            raise TypeError

    def is_valid(self, input: str) -> bool:
        input = input.strip()
        return (super().is_valid(input) and int(input) < self.limit)

    def get_invalid_msg(self) -> str:
        return f"Must be a whole number between 0 and {self.limit}"


class IsNaturalNumGreaterThan(IsNaturalNum):
    """Input validator that returns true if the input is a natural number greater than a given number. Ignores whitespace on either side of input
    
    Args:
        limit (str): Input must be higher than this number
    """
    limit: int
    def __init__(self, limit: int) -> None:
        try:
            self.limit = float(limit)
        except:
            raise TypeError

    def is_valid(self, input: str) -> bool:
        input = input.strip()
        return (super().is_valid(input) and int(input) > self.limit)

    def get_invalid_msg(self) -> str:
        return f"Must be a whole number greater than {self.limit}"


class IsLetters(InputValidator):
    """Input validator that returns true if the input contains only letters and spaces"""
    def is_valid(self, input: str) -> bool:
        return input.replace(" ", "").isalpha()

    def get_invalid_msg(self) -> str:
        return "Must only contain letters"


class IsLettersAndSymbols(InputValidator):
    """Input validator that returns true if the input contains only letters, spaces, and the given symbols
    
    Args:
        symbols (str): The special characters allowed in the input, eg: "!.,?"
    """
    symbols: str
    def __init__(self, symbols: str) -> None:
        self.symbols = symbols

    def is_valid(self, input: str) -> bool:
        if input.replace(" ", "") == "": return False

        input = remove_chars(input, self.symbols + " ")
        return (
            input.isalpha() or input == ""
        )

    def get_invalid_msg(self) -> str:
        return f"Must only contain letters and {seperate_by_commas(self.symbols)}"


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
            symbols (str): The special characters allowed in the input, eg: "!.,?"
        """
    symbols: str
    def __init__(self, symbols: str) -> None:
        self.symbols = symbols

    def is_valid(self, input: str) -> bool:
        if input.replace(" ", "") == "": return False

        input = remove_chars(input, self.symbols + " ")
        return (
            input.isalnum() or input == ""
        )

    def get_invalid_msg(self) -> str:
        return f"Must only contain letters, numbers and {seperate_by_commas(self.symbols)}"


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
        return f"Must be one of the following: {seperate_by_commas(self.options)}"
