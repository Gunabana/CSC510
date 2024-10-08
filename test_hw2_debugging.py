"""Import the pytest suite"""
from hw2_debugging import merge_sort


def test_single_value():
    """Tests that a single element is returned"""
    assert merge_sort([1]) == [1]


def test_two_values():
    """Tests that two elements are sorted"""
    assert merge_sort([2, 1]) == [1, 2]


def test_long_array():
    """Test a long array"""
    assert merge_sort([21, 48, 21, 2, 0, 4, -3, 100]
                      ) == [-3, 0, 2, 4, 21, 21, 48, 100]


def empty_array():
    """Tests an empty array"""
    assert not merge_sort([])
