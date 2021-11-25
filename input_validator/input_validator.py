from abc import ABC, abstractmethod


class InputValidator(ABC):
    """A abstract class for conditions that validate user input."""
    @abstractmethod
    def is_valid(self, input: str) -> bool:
        """Returns true if the inputs passes the class's condition."""
        pass

    @abstractmethod
    def get_invalid_msg(self) -> str:
        """Returns a message to display if input is invalid."""
        pass


def get_input(prompt: str, condition: InputValidator, bold_input: bool=True) -> str:
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
