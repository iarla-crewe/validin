from validin import validators as valid
from validin.validin import InputValidator

def test_validator(validator: InputValidator, input, correct_out):
    assert validator.is_valid(input) == correct_out

def run_tests():
    test_validator(valid.IsNaturalNum, "4", True)