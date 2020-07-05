import pytest

from ..list_queue import Queue

@pytest.fixture
def starbucks_line():
    line = Queue()
    line.enqueue("JB")
    line.enqueue("Vij")
    line.enqueue("Joseph")
    return line

def test_enqueue_three(starbucks_line):
    starbucks = starbucks_line
    expected = "JB"
    actual = starbucks.peek()
    assert actual == expected
    assert starbucks.is_empty != True

def test_dequeue_the_line(starbucks_line):
    starbucks = starbucks_line
    starbucks.dequeue()
    expected = "Vij"
    assert starbucks.dequeue() == expected
    expected_2 = "Joseph"
    assert starbucks.dequeue() == expected_2
    assert starbucks.is_empty

