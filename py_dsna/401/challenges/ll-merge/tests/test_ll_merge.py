import pytest

from ll_merge.ll_merge import (
    LinkedList,
    Node,
)


def test_linked_list_class_exists():
    assert LinkedList


# @pytest.mark.skip
def test_ll_merge_exists():
    assert LinkedList.merge_lists

