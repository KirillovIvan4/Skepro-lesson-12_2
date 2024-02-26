import pytest

from src.list_types import types_count


def test_types_count_1():
    assert types_count([1, 2, 3], int) == 3
    assert types_count([1, '2', '3'], int) == 1
    assert types_count([1, '2', '3'], str) == 2


@pytest.mark.parametrize('array, type_in_array, expected',[
    ([1, 2, 3], int, 3),
    ([1, '2', '3'], int, 1),
    ([1, '2', '3'], str, 2)
])
def test_types_count_2(array, type_in_array, expected):
    assert types_count(array, type_in_array) == expected