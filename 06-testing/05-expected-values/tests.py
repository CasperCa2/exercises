import pytest
from mergesort import split_in_two


@pytest.mark.parametrize("ns", [
    list(range(n)) for n in range(101)
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    assert left + right == ns
    assert abs(len(left)-len(right)) <= 1
