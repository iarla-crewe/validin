# InputValidatorPy
Console input validator for python, allows for any condition to be checked in a clean and consice syntax


## Docs (temporary):
    ```
    import input_validator as inpt
    from input_validator import get_input
    ```

    Use get_input to get valid user input

    Input validators:
    - IsNaturalNum
    - IsNaturalNumLessThan
    - IsLetters
    - IsLettersAndSymbols
    - IsAlphanumeric
    - IsAlphanumericAndSymbols
    - IsOption

    To create a new validator, 
        create a NewInputValidator() class with the condition and invalid input message wanted.
    For a validator with more advanced functionality (such as dynamic invalid input messages), 
        create an InputValidator subclass (see the docs)