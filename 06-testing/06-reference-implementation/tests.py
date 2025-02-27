import pytest
from search import *
from student import Student


@pytest.mark.parametrize("students", [
    [],
    [Student(id) for id in range(0, 100)],
    [Student(id) for id in [4, 5, 6, 11, 15, 16, 17, 18, 25]]
])
@pytest.mark.parametrize("id", range(0, 100))
def test_search(students, id):
    linear_result = linear_search(students, id)
    binary_result = binary_search(students, id)
    assert linear_result is binary_result, f"failed looking up {id}"
