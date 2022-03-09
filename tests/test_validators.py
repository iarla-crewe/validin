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

    assert condition.is_valid("") == False
    assert condition.is_valid("         ") == False
    assert condition.is_valid("0") == False
    assert condition.is_valid("-2") == False
    assert condition.is_valid("14.13") == False
    assert condition.is_valid("") == False
    assert condition.is_valid("foo") == False
    assert condition.is_valid("3f") == False
    assert condition.is_valid("1 0") == False
    assert condition.is_valid("") == False


def test_IsNaturalNumLessThan():
    with pytest.raises(TypeError):
        valid.IsNaturalNumLessThan("foo")
    
    condition = valid.IsNaturalNumLessThan("5")
    assert condition.is_valid("4") == True
    assert condition.is_valid("1") == True
    assert condition.is_valid("") == False
    assert condition.is_valid("         ") == False
    assert condition.is_valid("0") == False
    assert condition.is_valid("14") == False
    assert condition.is_valid("Three") == False
    assert condition.is_valid("2.567") == False
    assert condition.is_valid("-1") == False

    condition = valid.IsNaturalNumLessThan("1.3")
    assert condition.is_valid("1") == True
    assert condition.is_valid("") == False
    assert condition.is_valid("         ") == False
    assert condition.is_valid("2") == False


def test_IsNaturalNumGreaterThan():
    with pytest.raises(TypeError):
        valid.IsNaturalNumGreaterThan("foo")
    
    condition = valid.IsNaturalNumGreaterThan("5")
    assert condition.is_valid("1000") == True
    assert condition.is_valid("6") == True
    assert condition.is_valid("") == False
    assert condition.is_valid("         ") == False
    assert condition.is_valid("0") == False
    assert condition.is_valid("4") == False
    assert condition.is_valid("Three") == False
    assert condition.is_valid("25.567") == False
    assert condition.is_valid("-1") == False

    condition = valid.IsNaturalNumGreaterThan("1.3")
    assert condition.is_valid("2") == True
    assert condition.is_valid("") == False
    assert condition.is_valid("         ") == False
    assert condition.is_valid("1") == False


def test_IsLetters():
    condition = valid.IsLetters()

    assert condition.is_valid("abfdsafjdsak") == True
    assert condition.is_valid("Hello there") == True
    assert condition.is_valid("            s                                                            m") == True
    
    assert condition.is_valid("") == False
    assert condition.is_valid("         ") == False
    assert condition.is_valid("abcd567") == False
    assert condition.is_valid("Hello.there") == False
    assert condition.is_valid("a'") == False


def test_IsLettersAndSymbols():
    condition = valid.IsLettersAndSymbols("!.,")

    assert condition.is_valid("Hello!") == True
    assert condition.is_valid("fOo") == True
    assert condition.is_valid(".a......") == True
    
    condition = valid.IsLettersAndSymbols("#@")

    assert condition.is_valid("                            #") == True
    assert condition.is_valid("@the building") == True

    assert condition.is_valid("Hello!") == False
    assert condition.is_valid("@@@@.@@@@") == False
    assert condition.is_valid("") == False
    assert condition.is_valid("         ") == False


def test_IsAlphanumeric():
    condition = valid.IsAlphanumeric()

    assert condition.is_valid("abcdefghijklmnopqrstuvwxyz") == True
    assert condition.is_valid("12345") == True
    assert condition.is_valid("I have 4 things") == True
    assert condition.is_valid("4lph4num3r1c") == True
    assert condition.is_valid("Пpивëт") == True

    assert condition.is_valid("") == False
    assert condition.is_valid("         ") == False
    assert condition.is_valid("Symbols!") == False
    assert condition.is_valid("400.213") == False
    assert condition.is_valid("//") == False


def test_IsAlphanumericAndSymbols():
    condition = valid.IsAlphanumericAndSymbols("!.,")

    assert condition.is_valid("Hello!") == True
    assert condition.is_valid("And12345...")
    assert condition.is_valid("fOo  45") == True
    assert condition.is_valid(".2......") == True
    
    condition = valid.IsAlphanumericAndSymbols("#@")

    assert condition.is_valid("                            #") == True
    assert condition.is_valid("@the building") == True
    assert condition.is_valid("123456789###") == True

    assert condition.is_valid("Hello!") == False
    assert condition.is_valid("@@@@.@@@@") == False
    assert condition.is_valid("s0m3 t3xt h3r3.") == False
    assert condition.is_valid("") == False
    assert condition.is_valid("         ") == False


def test_IsOption():
    condition = valid.IsOption("1", "2")

    assert condition.is_valid("1") == True
    assert condition.is_valid("2") == True

    assert condition.is_valid("3") == False
    assert condition.is_valid("  1    ") == False

    condition = valid.IsOption("the first one", "some other thing", "foo")

    assert condition.is_valid("the first one") == True
    assert condition.is_valid("some other thing") == True
    assert condition.is_valid("foo") == True

    assert condition.is_valid("") == False
    assert condition.is_valid("         ") == False
    assert condition.is_valid("literally anything else") == False
    assert condition.is_valid("123") == False
    assert condition.is_valid("tHe first one") == False
    assert condition.is_valid("FOO") == False
    assert condition.is_valid("sómë óthër thíng") == False
