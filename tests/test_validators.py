from validin import validators as valid
from validin import utils


def test_utils():
    assert utils.list_as_str(["foo"]) == "foo"
    assert utils.list_as_str([".12", "xyz"]) == ".12, xyz"
    assert utils.list_as_str(["a", "b", "100", "   "]) == "a, b, 100,    "

    assert utils.remove_chars("This is a test string", " ") == "Thisisateststring"
    assert utils.remove_chars("This is a test string", "aeiou") == "Ths s  tst strng"
    assert utils.remove_chars("This is a test string", "0123456789!£$%^&*()") == "This is a test string"


def test_IsNaturalNum():
    assert valid.IsNaturalNum.is_valid("2") == True
    assert valid.IsNaturalNum.is_valid("4321894523432732454315") == True
    assert valid.IsNaturalNum.is_valid("1 ") == True
    assert valid.IsNaturalNum.is_valid("  49 ") == True

    assert valid.IsNaturalNum.is_valid("0") == False
    assert valid.IsNaturalNum.is_valid("-2") == False
    assert valid.IsNaturalNum.is_valid("14.13") == False
    assert valid.IsNaturalNum.is_valid("") == False
    assert valid.IsNaturalNum.is_valid("foo") == False
    assert valid.IsNaturalNum.is_valid("3f") == False
    assert valid.IsNaturalNum.is_valid("1 0") == False
