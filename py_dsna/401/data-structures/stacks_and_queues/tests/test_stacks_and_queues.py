import pytest
from ..stacks_and_queues import (
    Node,
    Stack,
    Queue,
)


def test_Node_exists():
    assert Node


def test_Stack_exists():
    assert Stack


def test_Queue_exists():
    assert Queue


# - - - - Node tests - - - - - #

def test_node_instantiates():
    new_node = Node("apples")
    assert new_node.value == "apples"


def test_node_intantiate_fails():
    new_node = Node("apples")
    assert new_node.value != "apple"


def test_node_str_returns():
    new_node = Node("apples")
    assert str(new_node) == "Node value = apples and next node = None."


def test_node_repr_returns():
    new_node = Node("apples")
    assert repr(new_node) == "<Node> class; value=apples, next=None"


# - - - - Stack tests - - - - - #

def test_empty_stack_returns():
    empty_stack = Stack()
    assert empty_stack.top == None


def test_stack_isempty_returns():
    empty_stack = Stack()
    assert empty_stack.is_empty


def test_one_item_stack_returns():
    stack = Stack()
    stack.push("apples")
    assert stack.top.value == "apples"


def test_one_item_stack_fails():
    stack = Stack()
    stack.push("apples")
    assert stack.top.value != "apple"


def test_one_item_stack_next_returns():
    stack = Stack()
    stack.push("apples")
    assert stack.top.next == None


def test_one_item_stack_isempty_fails():
    stack = Stack()
    stack.push("apples")
    assert stack.is_empty != True


# @pytest.mark.skip
def test_one_item_popped_stack_isempty_pass():
    stack = Stack()
    stack.push("apples")
    assert stack.top.value == "apples"
    stack.pop()
    assert stack.top == None 
    expected = True
    actual = stack.is_empty()
    assert actual == expected



@pytest.fixture
def stock_stack():
    stack_ = Stack()
    stack_.push("apples")
    stack_.push("bananas")
    stack_.push("cherries")
    return stack_


def test_three_item_stack_top(stock_stack):
    fruit_stack = stock_stack
    assert fruit_stack.top.value == "cherries"


def test_three_item_stack_top_next(stock_stack):
    fruit_stack = stock_stack
    assert fruit_stack.top.next.value == "bananas"


def test_three_item_stack_not_empty(stock_stack):
    fruit_stack = stock_stack
    assert fruit_stack.is_empty != True

    
# @pytest.mark.skip
def test_stack_top_item_str_returns(stock_stack):
    fruit_stack = stock_stack
    assert str(fruit_stack.top) == "Node value = cherries and next node = bananas."


# @pytest.mark.skip
def test_three_item_stack_peek_pass(stock_stack):
    fruit_stack = stock_stack
    assert fruit_stack.top.value == "cherries"
    # assert fruit_stack.peek() == "cherries"
    

@pytest.mark.skip
def test_three_item_stack_pop_pass(stock_stack):
    fruit_stack = stock_stack
    assert fruit_stack.pop == "cherries"


@pytest.mark.skip
def test_pop_two_from_three_item_stack(stock_stack):
    fruit_stack = stock_stack
    fruit_stack.pop()
    expected = "bananas"
    actual = fruit_stack.pop()
    assert actual == expected


@pytest.mark.skip
def test_stack_str_returns():
    stack = Stack()
    stack.push("apples")
    assert str(Stack.top) == "Stack class; top = apples."

    
@pytest.mark.skip
def test_stack_item_repr_returns():
    stack = Stack()
    assert repr(stack.top) == "Node value = cherries and next node = bananas."


# - - - - Queue tests - - - - - #

# @pytest.mark.skip
def test_Queue_instantiates():
    new_queue = Queue()
    actual = new_queue.peek()
    expected = None
    assert actual == expected


@pytest.mark.skip
def test_queue_isempty():
    blank = Queue()
    expected = True
    actual = blank.is_empty
    assert actual == expected


@pytest.mark.skip
def test_enqueue_one_item_pass():
    prism = Queue()
    prism.enqueue("red")
    actual = prism.front.value
    expected = "red"
    assert actual == expected


@pytest.mark.skip
def test_peek_at_item_pass():
    prism = Queue()
    prism.enqueue("red")
    actual = prism.peek()
    expected = "red"
    assert actual == expected


@pytest.mark.skip
def test_dequeue_item_pass():
    prism = Queue()
    prism.enqueue("red")
    prism.enqueue("orange")
    prism.dequeue()
    actual = prism.peek()
    expected = "red"
    assert actual == expected

