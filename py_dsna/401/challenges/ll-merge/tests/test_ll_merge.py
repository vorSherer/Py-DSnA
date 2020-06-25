import pytest

# try:
# from ll_merge.node_ import Node
# from ll_merge.linked_list_ import LinkedList, Node  # works in terminal, not pytest
from ll_merge.ll_merge import merge_lists
# except ImportError:
# from node_ import Node
from .linked_list_ import LinkedList, Node
# from ll_merge import merge_lists


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
    ll1.insert("kale")
    ll1.insert("spinach")
    ll1.insert("romaine")
    return ll1


@pytest.fixture
def salad_2():
    ll2 = LinkedList()
    ll2.insert("cucumber")
    ll2.insert("broccoli")
    ll2.insert("red bell pepper")
    return ll2


@pytest.fixture
def salad_3():
    ll3 = LinkedList()
    ll3.insert("raspberry vinaigrette")
    ll3.insert("chopped nuts")
    ll3.insert("dried cranberries")
    return ll3


def test_merge_two_lists(salad_1, salad_2):
    ll1 = salad_1
    ll2 = salad_2
    


