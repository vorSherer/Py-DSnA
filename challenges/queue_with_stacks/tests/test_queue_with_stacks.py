import pytest

# from queue_with_stacks.queue_with_stacks import PseudoQueue
# from ..queue_with_stacks import PseudoQueue
# from .queue_with_stacks import PseudoQueue
from queue_with_stacks import PseudoQueue

# from queue_with_stacks import Stack

@pytest.mark.skip
def test_stack_exists():
    assert Stack


@pytest.mark.skip
def test_pq_exists():
    assert PseudoQueue


@pytest.mark.skip
def test_enqueue_one():
    pq = PseudoQueue()
    pq.enqueue("penny")


# @pytest.fixture
# def coin_stack():
#     coins = PseudoQueue()
#     coins.enqueue("penny")
#     coins.enqueue("nickel")
#     coins.enqueue("dime")
#     return coins

