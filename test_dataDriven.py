#From: https://codereview.stackexchange.com/questions/276551/table-driven-tests-in-python-using-pytest
# 2nd test is designed to fail on purpose
import pytest
from dataclasses import dataclass

def say_hello(name: str) -> str:
    return f"Hello {name}"

def nashville(name) :
    return 'Hello ' + name

input1 = 'Jason Aldean'
expOutput1 = 'Hello Jason Aldean'

# ------------------------------------------------------------------------------
# TESTS
# ------------------------------------------------------------------------------

@dataclass
class TestData:
    id: str
    input: tuple
    expected: any
    __test__ = False


class TestClass:
    testdata = [
        TestData(id="boy name", input=("Vipin",), expected="Hello Vipin"),
        TestData(id="girl name", input=("Geethu",), expected="FAIL"),
        TestData(id="girl name", input=(input1,), expected=expOutput1),
        TestData(id="girl name", input=(input1,), expected=nashville(input1)), # Where the expectation is dynamically generated based on the input
    ]

    @pytest.mark.parametrize(
        "input,expected",
        map(lambda x: (x.input, x.expected), testdata),
        ids=map(lambda x: x.id, testdata),
    )
    def test(self, input, expected):
        actual = say_hello(*input)
        assert actual == expected