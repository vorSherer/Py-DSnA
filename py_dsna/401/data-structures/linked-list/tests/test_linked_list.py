from linked_list.linked_list import (
    Node,
    LinkedList,
)

def test_Node_exists():
    assert Node


def test_LinkedList_exists():
    assert LinkedList


# Can successfully instantiate an empty linked list
def test_instance():
  ll = LinkedList()
  assert ll.head == None


# Can properly insert into the linked list
def test_insert_to_ll():
    ll = LinkedList()
    ll.insert('apple')
    expected = 'apple'
    assert ll.head.value == expected
    
# The head property will properly point to the first node in the linked list

# Can properly insert multiple nodes into the linked list

# Will return true when finding a value within the linked list that exists

# Will return false when searching for a value in the linked list that does not exist

# Can properly return a collection of all the values that exist in the linked list
