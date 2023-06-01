import pytest
from intervals import overlapping_intervals


@pytest.mark.parametrize("interval1,interval2", [
    ((1, 5), (3, 6)),
    ((1, 5), (5, 6)),
    ((1, 10), (3, 6)),
    ((6, 8), (3, 6)),
    ((5, 7), (4, 8)),
])
def test_overlapping_intervals(interval1, interval2):
    assert overlapping_intervals(
        interval1, interval2), f"{interval1} overlaps with {interval2}"
