from src.list_types import types_in_list


def test_types_in_list():
    types_in_list([1, 2, 3], int) == 3
    types_in_list([1, '2', '3'], int) == 1
    types_in_list([1, '2', '3'], str) == 2
