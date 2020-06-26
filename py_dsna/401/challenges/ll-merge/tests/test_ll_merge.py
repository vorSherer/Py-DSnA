import pytest

from ll_merge.ll_merge import merge_lists
from .linked_list_ import LinkedList, Node


# @pytest.mark.skip
def test_linked_list_class_exists():
    assert LinkedList


def test_node_class_exists():
    assert Node


# @pytest.mark.skip
def test_ll_merge_exists():
    assert merge_lists

@pytest.fixture
def salad_1():
    ll1 = LinkedList()
    ll1.insert("raspberry vinaigrette")
    ll1.insert("chopped nuts")
    ll1.insert("dried cranberries")
    ll1.insert("broccoli")
    ll1.insert("kale")
    ll1.insert("romaine")

    return ll1


@pytest.fixture
def salad_2():
    ll2 = LinkedList()
    ll2.insert("cucumber")
    ll2.insert("red bell pepper")
    ll2.insert("spinach")
    return ll2


def test_merge_two_lists_pass(salad_1, salad_2):
    ll1 = salad_1
    ll2 = salad_2
    assert str(merge_lists(ll1, ll2)) == "{ romaine } -> { spinach } -> { kale } -> { red bell pepper } -> { broccoli } -> { cucumber } -> { dried cranberries } -> { chopped nuts } -> { raspberry vinaigrette } -> None"


def test_merge_two_lists_fail(salad_1, salad_2):
    ll1 = salad_1
    ll2 = salad_2
    assert str(merge_lists(ll1, ll2)) != "{ romaine } -> { spinach } -> { kale } -> { red bell peppers } -> { broccoli } -> { cucumber } -> { dried cranberries } -> { chopped nuts } -> { raspberry vinaigrette } -> None"
