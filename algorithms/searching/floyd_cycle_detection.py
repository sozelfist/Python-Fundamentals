import unittest
from typing import Optional


class ListNode:
    def __init__(self, val: float | None, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    """
    Determines whether a linked list has a cycle using
    the Floyd cycle detection algorithm.

    Args:
        head (Optional[ListNode]): The head node of the linked list.

    Returns:
        bool: True if the linked list has a cycle, False otherwise.
    """
    if head is None:
        return False

    slow, fast = head, head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True

        slow, fast = slow.next, fast.next.next

    return False


class TestHasCycle(unittest.TestCase):
    def setUp(self):
        self.node1 = ListNode(1)
        self.node2 = ListNode(2)
        self.node3 = ListNode(3)
        self.node4 = ListNode(4)

    def test_empty_list(self):
        self.assertFalse(has_cycle(None))

    def test_no_cycle(self):
        self.node1.next = self.node2
        self.node2.next = self.node3
        self.node3.next = self.node4
        self.assertFalse(has_cycle(self.node1))

    def test_cycle(self):
        self.node1.next = self.node2
        self.node2.next = self.node3
        self.node3.next = self.node4
        self.node4.next = self.node2
        self.assertTrue(has_cycle(self.node1))


if __name__ == '__main__':
    unittest.main()
