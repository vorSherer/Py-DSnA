import pytest

from linked_list.linked_list import (
    Node,
    LinkedList,
)

def test_Node_exists():
    assert Node


def test_LinkedList_exists():
    assert LinkedList


def test_node_value_returns():
    apples = Node("apples")
    assert apples.has_value() == "apples"


def test_next_node_returns_none():
    apples = Node("apples")
    assert apples.get_next() == None


# Can successfully instantiate an empty linked list
def test_instance():
  ll = LinkedList()
  assert ll.head == None


# Can properly insert into the linked list
# @pytest.mark.skip
def test_insert_to_ll():
    ll = LinkedList()
    ll.insert('apple')
    expected = 'apple'
    assert ll.head.value == expected


# The head property will properly point to the first node in the linked list
# @pytest.mark.skip
def test_insert_empty():
  ll = LinkedList()
  ll.insert("apples")
  assert ll.head.value == "apples"


# Can properly insert multiple nodes into the linked list
@pytest.fixture
def starter_fruit():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    return ll


# @pytest.mark.skip
def test_insert_full(starter_fruit):
    ll = starter_fruit
    assert ll.head.value == "bananas"
    assert ll.head.next_node.value == "apples"


# @pytest.mark.skip
def test_str_output(starter_fruit):
    ll = starter_fruit
    assert str(ll) == "{ bananas } -> { apples } -> None"


# Will return true when finding a value within the linked list that exists
def test_find_value_in_list_pass(starter_fruit):
    ll = starter_fruit
    assert ll.includes("apples")


# Will return false when searching for a value in the linked list that does not exist
def test_find_value_in_list_fails(starter_fruit):
    ll = starter_fruit
    assert not ll.includes("kiwi")


# Can properly return a collection of all the values that exist in the linked list
def test_return_whole_list_values():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    ll.insert("cantaloupes")
    ll.insert("d'Anjou pears")
    assert str(ll) == "{ d'Anjou pears } -> { cantaloupes } -> { bananas } -> { apples } -> None" 

# Testing TypeError trap
# @pytest.mark.skip
def test_insert_typeerror():
  with pytest.raises(TypeError):
    Node("Bogus_data", "This is NOT a Node")
