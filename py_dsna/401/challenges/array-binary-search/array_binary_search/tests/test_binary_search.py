import pytest


from array_binary_search.array_binary_search import binary_search

def test_binary_search_exists():
    assert binary_search


# @pytest.mark.skip
def test_binary_search_returns_inputs():
    expected = 1
    actual = binary_search([1,2,3,4,5], 2)
    assert actual == expected


# @pytest.mark.skip
def test_binary_search_returns_fail():
    expected = -1
    actual = binary_search([1,2,3,4,5], 4)
    assert actual != expected


# @pytest.mark.skip
def test_binary_search_no_match():
    expected = -1
    actual = binary_search([11,22,33,44,55,66,77], 90)
    assert actual == expected


def test_search_100_pass():
    expected = 43
    test_list = [i for i in range(100)]
    actual = binary_search(test_list, 43)
    assert actual == expected


def test_search_10000_pass():
    expected = 9998
    test_list2 = [i for i in range(10000)]
    actual = binary_search(test_list2, 9998)
    assert actual == expected

# @pytest.mark.skip
def test_search_100000_pass():
    expected = 441
    test_list3 = [i for i in range(100000)]
    actual = binary_search(test_list3, 441)
    assert actual == expected

