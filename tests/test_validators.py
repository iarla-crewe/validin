import pytest
from validin import validators as valid
from validin import utils


def test_utils():
    assert utils.seperate_by_commas(["foo"]) == "foo"
    assert utils.seperate_by_commas([".12", "xyz"]) == ".12, xyz"
    assert utils.seperate_by_commas(["a", "b", "100", "   "]) == "a, b, 100,    "

    assert utils.remove_chars("This is a test string", " ") == "Thisisateststring"
    assert utils.remove_chars("This is a test string", "aeiou") == "Ths s  tst strng"
    assert utils.remove_chars("This is a test string", "0123456789!£$%^&*()") == "This is a test string"


def test_IsNaturalNum():
    condition = valid.IsNaturalNum()
    
    assert condition.is_valid("2") == True
    assert condition.is_valid("4321894523432732454315") == True
    assert condition.is_valid("1 ") == True
    assert condition.is_valid("  49 ") == True

    assert condition.is_valid("0") == False
    assert condition.is_valid("-2") == False
    assert condition.is_valid("14.13") == False
    assert condition.is_valid("") == False
    assert condition.is_valid("foo") == False
    assert condition.is_valid("3f") == False
    assert condition.is_valid("1 0") == False


def test_IsNaturalNumLessThan():
    with pytest.raises(TypeError):
        valid.IsNaturalNumLessThan("foo")
    
    condition = valid.IsNaturalNumLessThan("5")
    assert condition.is_valid("4") == True
    assert condition.is_valid("1") == True
    assert condition.is_valid("0") == False
    assert condition.is_valid("14") == False
    assert condition.is_valid("Three") == False
    assert condition.is_valid("2.567") == False
    assert condition.is_valid("-1") == False

    condition = valid.IsNaturalNumLessThan("1.3")
    assert condition.is_valid("1") == True
    assert condition.is_valid("2") == False
    assert condition.is_valid("") == False


def test_IsLetters():
    condition = valid.IsLetters()


def test_IsLettersAndSymbols():
    condition = valid.IsLettersAndSymbols()


def test_IsAlphanumeric():
    condition = valid.IsAlphanumeric()


def test_IsAlphanumericAndSymbols():
    condition = valid.IsAlphanumericAndSymbols()


def test_IsOption():
    condition = valid.IsOption()
