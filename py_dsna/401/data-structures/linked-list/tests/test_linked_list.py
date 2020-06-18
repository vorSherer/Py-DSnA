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
    ll.insert("cantaloupes")
    ll.insert("d'Anjou pears")
    return ll


def test_insert_full(starter_fruit):
    ll = starter_fruit
    assert ll.head.value == "d'Anjou pears"
    assert ll.head.next_node.value == "cantaloupes"


def test_str_output(starter_fruit):
    ll = starter_fruit
    assert str(ll) == "{ d'Anjou pears } -> { cantaloupes } -> { bananas } -> { apples } -> None"


# Will return true when finding a value within the linked list that exists
def test_find_value_in_list_pass(starter_fruit):
    ll = starter_fruit
    assert ll.includes("apples")


# Will return false when searching for a value in the linked list that does not exist
def test_find_value_in_list_fails(starter_fruit):
    ll = starter_fruit
    assert not ll.includes("kiwi")


# Can properly return a collection of all the values that exist in the linked list
def test_return_whole_list_values(starter_fruit):
    ll = starter_fruit
    assert str(ll) == "{ d'Anjou pears } -> { cantaloupes } -> { bananas } -> { apples } -> None"


# Testing TypeError trap
# @pytest.mark.skip
def test_insert_typeerror():
  with pytest.raises(TypeError):
    Node("Bogus_data", "This is NOT a Node")


# CC-06; Can successfully add a node to the end of the linked list
# @pytest.mark.skip
def test_append_node_to_end(starter_fruit):
    ll = starter_fruit
    ll.append("lemons")
    assert str(ll) == "{ d'Anjou pears } -> { cantaloupes } -> { bananas } -> { apples } -> { lemons } -> None"


# @pytest.mark.skip
def test_append_node_to_empty_list():
    ll = LinkedList()
    ll.append("lemons")
    assert str(ll) == "{ lemons } -> None"


# CC-06; Can successfully add multiple nodes to the end of a linked list
# @pytest.mark.skip
def test_append_multiple_nodes_to_end(starter_fruit):
    ll = starter_fruit
    ll.append("lemons")
    ll.append("limes")
    assert str(ll) == "{ d'Anjou pears } -> { cantaloupes } -> { bananas } -> { apples } -> { lemons } -> { limes } -> None"


# CC-06; Can successfully insert a node before a node located in the middle of a linked list
# @pytest.mark.skip
def test_insert_node_amid_list(starter_fruit):
    ll = starter_fruit
    ll.insert_before("bananas", "limes")
    expected = "{ d'Anjou pears } -> { cantaloupes } -> { limes } -> { bananas } -> { apples } -> None"
    actual = str(ll)
    assert actual == expected


# @pytest.mark.skip
def test_insert_node_to_empty_list():
    ll = LinkedList()
    ll.insert_before("apples", "lemons")
    assert -1


# CC-06; Can successfully insert a node before the first node of a linked list
# @pytest.mark.skip
def test_insert_node_before_head():
    ll = LinkedList()
    ll.append("apples")
    ll.insert_before("apples", "lemons")
    assert str(ll) == "{ lemons } -> { apples } -> None"


# @pytest.mark.skip
def test_insert_node_no_value_match():
    ll = LinkedList()
    ll.append("apples")
    ll.insert_before("Blueberries", "lemons")
    assert -1


# CC-06; Can successfully insert after a node in the middle of the linked list
# @pytest.mark.skip
def test_insert_after_amid_list(starter_fruit):
    ll = starter_fruit
    ll.insert_after("bananas", "limes")
    expected = "{ d'Anjou pears } -> { cantaloupes } -> { bananas } -> { limes } -> { apples } -> None"
    actual = str(ll)
    assert actual == expected


# @pytest.mark.skip
def test_insert_after_no_match(starter_fruit):
    ll = starter_fruit
    ll.insert_after("kiwis", "limes")
    expected = "{ d'Anjou pears } -> { cantaloupes } -> { bananas } -> { limes } -> { apples } -> None"
    actual = str(ll)
    assert -1


# @pytest.mark.skip
def test_insert_after_empty_list():
    ll = LinkedList()
    ll.insert_after("apples", "lemons")
    assert -1


# CC-06; Can successfully insert a node after the last node of the linked list
@pytest.mark.skip
def test_insert_after_end(starter_fruit):
    ll = starter_fruit
    ll.insert_after("apples", "limes")
    expected = "{ d'Anjou pears } -> { cantaloupes } -> { bananas } -> { apples } -> { limes } -> None"
    actual = str(ll)
    assert actual == expected

# CC-07; Where k is greater than the length of the linked list
@pytest.mark.skip
def test_k_greater_than_length(starter_fruit):
    ll = starter_fruit
    actual = ll.value_at_kth_from_end(5)
    expected = Exception("Value for k must be less that list length.")
    assert actual == expected


# CC-07; Where k and the length of the list are the same
@pytest.mark.skip
def test_k_same_as_length(starter_fruit):
    ll = starter_fruit
    actual = ll.value_at_kth_from_end(4)
    expected = Exception("Value for k must be less that list length.")
    assert actual == expected

# CC-07; Where k is not a positive integer
@pytest.mark.skip
def test_k_is_negative_value(starter_fruit):
    ll = starter_fruit
    actual = ll.value_at_kth_from_end(-2)
    expected = Exception("Value supplied for k must be a positive integer.")
    assert actual == expected


# CC-07; Where the linked list is of a size 1
# @pytest.mark.skip
def test_ll_size_1():
    ll = LinkedList()
    ll.insert("apples")
    actual = ll.value_at_kth_from_end(0)
    expected = "apples"
    assert actual == expected


# CC-07; “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
# @pytest.mark.skip
def test_k_amid_list(starter_fruit):
    ll = starter_fruit
    expected = "cantaloupes"
    actual = ll.value_at_kth_from_end(2)
    assert actual == expected

