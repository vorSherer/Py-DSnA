from linked_list.linked_list import (
    LinkedList,
    Node
)

def test_LinkedList_exists():
    assert LinkedList()


def test_Node_exists():
    assert Node


# *** Can successfully instantiate an empty linked list

def test_instance():
  ll = LinkedList()
  assert ll.head == None


# *** Can properly insert into the linked list

# *** The head property will properly point to the first node in the linked list

def test_insert_empty():
  ll = LinkedList()
  ll.insert("apples")
  assert ll.head.value == "apples"

# *** Can properly insert multiple nodes into the linked list

def test_insert_full():
    # Replace next 3 lines with a Fixture
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    assert ll.head.value == "bananas"
    assert ll.head.next_node.value == "apples"


def test_str_output():
    # Replace next 3 lines with a Fixture

    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    assert str(ll) == "{ bananas } -> { apples } -> NULL"



# *** Will return true when finding a value within the linked list that exists


# *** Will return false when searching for a value in the linked list that does not exist


# *** Can properly return a collection of all the values that exist in the linked list


# def test_insert_empty():
#   with pytest.raises(TypeError):
#     Node("ugh", "this is NOT a Node")

