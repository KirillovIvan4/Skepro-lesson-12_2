from src.append_array import append_array


def test_append_array_1(array_fixture):
    assert append_array(array_fixture, 4) == [1, 2, 3, 4]


def test_append_array_2(array_fixture):
    assert append_array(array_fixture, 5) == [1, 2, 3, 5]