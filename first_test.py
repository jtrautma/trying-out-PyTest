import pytest

def addNumbers(x) :
    return x + 5

def test_method() :
    assert addNumbers(3) == 8