import pytest
from ..stacks_and_queues import (
    Node,
    Stack,
)


def test_Node_exists():
    assert Node


def test_Stack_exists():
    assert Stack


# - - - - Node tests - - - - - #

def test_node_instantiated():
    new_node = Node("apples")
    assert new_node.value == "apples"


def test_node_intantiate_fails():
    new_node = Node("apples")
    assert new_node.value != "apple"


# @pytest.mark.skip
def test_node_str_returns():
    new_node = Node("apples")
    assert str(new_node) == "Node value = apples and next node = None."


# - - - - Stack tests - - - - - #

def test_empty_stack_returns():
    empty_stack = Stack()
    assert empty_stack.top == None
    assert empty_stack.is_empty


def test_one_node_stack_returns():
    stack = Stack()
    stack.push("apples")
    assert stack.top.value == "apples"
    assert stack.top.value != "apple"


@pytest.fixture
def stock_stack():
    stack_ = Stack()
    stack_.push("apples")
    stack_.push("bananas")
    stack_.push("cherries")
    return stack_


def test_three_node_stack_top(stock_stack):
    fruit_stack = stock_stack
    assert fruit_stack.top.value == "cherries"
    assert fruit_stack.top.next.value == "bananas"


# @pytest.mark.skip
def test_stack_node_str_returns(stock_stack):
    fruit_stack = stock_stack
    assert str(fruit_stack.top) == "Node value = cherries and next node = bananas."

# @pytest.mark.skip



# - - - - Queue tests - - - - - #


