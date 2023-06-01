import pytest
from parentheses import matching_parentheses


@pytest.mark.parametrize("string", [
    '(',
    ')',
    ')(',
    '(()))(()',
])
def test_false_matching_parentheses(string):
    actual = matching_parentheses(string)
    assert actual == False, f"{string} doesn't have matching parentheses"


@pytest.mark.parametrize("string", [
    '',
    '()',
    '(())',
    '()()()',
    '(())()',
])
def test_matching_parentheses(string):
    actual = matching_parentheses(string)
    assert actual == True, f"{string} does have matching parentheses"
