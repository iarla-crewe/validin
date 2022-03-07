from abc import ABC, abstractmethod


class InputValidator(ABC):
    """An abstract class that get_input() uses to validate user input."""
    @abstractmethod
    def is_valid(self, input: str) -> bool:
        """Returns true if the inputs passes the class's condition."""
        pass

    @abstractmethod
    def get_invalid_msg(self) -> str:
        """Returns a message to display if input is invalid."""
        pass


def get_input(prompt: str, condition: InputValidator=None, bold: bool=True) -> str:
    """Gets the users input and only returns once they have provided an input that passes the condition
    
    Args:
        prompt (str): String written to standard output in front of the user input.
        condition (InputCondition, optional): An InputCondition subclass used to check if inputted data is valid
            (Accepts all inputs if set to None)
        *condition_args (any, optional): Arguments passed into the InputCondition.
        bold_input (bool, optional): Formats the inputted text to be bold. Defaults to True.
    """
    BOLD_START = "\033[1m"                                      # Chars that start bold text in standard output
    BOLD_END = "\033[0m"                                        # Chars that end formatting in standard output
    format = BOLD_START if bold else ""                         # Set formatting if bold_input is True

    while True:
        raw_input: str = input(f"{prompt}{format}")             # Get and format user's input
        print(BOLD_END, end="")                                 # End input formatting
        if not condition or condition.is_valid(raw_input):      # Only return if input is valid
            return raw_input
        
        invalid_message = condition.get_invalid_msg()           # Print message if invalid
        if invalid_message: 
            invalid_message = f": {invalid_message}"
        print(f"Invalid Input{invalid_message}")