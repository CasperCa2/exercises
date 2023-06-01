import pytest
from mystatistics import average


@pytest.mark.parametrize("ns,expected", [
    ([1], 1),
    ([12, 15, 5], 10.67),
    ([5, 3], 4),
    ([.1, .1, .1], .1),
])
def test_average(ns, expected):
    actual = average(ns)
    assert pytest.approx(expected, abs=0.01) == actual
