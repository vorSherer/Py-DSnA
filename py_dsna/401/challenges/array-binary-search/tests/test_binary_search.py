import pytest

from array_binary_search.array_binary_search import binary_search

def test_binary_search_exists():
    assert binary_search


# @pytest.mark.skip
def test_binary_search_returns_inputs():
    expected = [1,2,3,4,5], 2
    actual = binary_search([1,2,3,4,5], 2)
    assert actual == expected


# @pytest.mark.skip
def test_binary_search_returns_fail():
    expected = [1,2,3,4,5], 2
    actual = binary_search([1,2,3,4,5], 4)
    assert actual != expected


# def test_binary_search


