import pytest

from ..list_stack import Stack

def test_push_one_item():
    fruits = Stack()
    fruits.push("apples")
    expected = "apples"
    actual = fruits.peek()
    assert actual == expected

def test_pop_one_item():
    fruits = Stack()
    fruits.push("apples")
    fruits.push("bananas")
    fruits.push("cherries")
    fruits.pop()
    expected = "bananas"
    actual = fruits.pop()
    assert actual == expected

def test_is_empty():
    parens = Stack()
    parens.push("(")
    parens.push(")")
    parens.pop()
    parens.pop()
    actual = parens.is_empty()
    expected = True
    assert actual == expected

