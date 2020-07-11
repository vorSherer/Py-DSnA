import pytest

from array_shift.array_shift import insert_shift_array
# from array_shift import insert_shift_array

def test_insert_shift_array_exists():
    assert insert_shift_array


# @pytest.mark.skip
def test_insert_shift_array_pass():
    expected = [2,4,5,6,8]
    actual = insert_shift_array([2,4,6,8], 5)
    assert actual == expected


# @pytest.mark.skip
def test_insert_shift_array_fail():
    expected = [2,4,5,6,8]
    actual = insert_shift_array([2,4,6,8], 7)
    assert actual != expected


# @pytest.mark.skip
def test_insert_shift_array_pass2():
    expected = [4,8,15,16,23,42]
    actual = insert_shift_array([4,8,15,23,42], 16)
    assert actual == expected


# @pytest.mark.skip
def test_insert_shift_array_string():
    expected = ["one","two","three","four","five","six"]
    actual = insert_shift_array(["one","two","three","five","six"], "four")
    assert actual == expected
