import unittest
from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class FibonacciHeapNode(Generic[T]):
    def __init__(self, key: float, value: T) -> None:
        self.key = key
        self.value = value
        self.parent: Optional[FibonacciHeapNode[T]] = None
        self.child: Optional[FibonacciHeapNode[T]] = None
        self.left: Optional[FibonacciHeapNode[T]] = None
        self.right: Optional[FibonacciHeapNode[T]] = None
        self.degree = 0
        self.marked = False


class FibonacciHeap(Generic[T]):
    def __init__(self) -> None:
        self.min_node: Optional[FibonacciHeapNode[T]] = None
        self.num_nodes = 0

    def insert(self, key: float, value: T) -> FibonacciHeapNode[T]:
        node = FibonacciHeapNode[T](key, value)
        node.left = node.right = node
        self._merge_with_list(node)
        self.num_nodes += 1
        return node

    def find_min(self) -> Optional[T]:
        return self.min_node.value if self.min_node is not None else None

    def delete_min(self) -> Optional[T]:
        if self.min_node is None:
            return None

        # detach min node from root list
        min_node = self.min_node
        if min_node.right == min_node:
            self.min_node = None
        else:
            self._remove_from_list(min_node)
            self.min_node = min_node.right

        # merge child list of min node with root list
        if min_node.child is not None:
            self._merge_with_list(min_node.child)

        # consolidate trees
        if self.min_node is not None:
            unmarked_trees = {}
            node = self.min_node
            while True:
                degree = node.degree
                while degree in unmarked_trees:
                    other = unmarked_trees[degree]
                    if other.key < node.key:
                        node, other = other, node
                    self._link(other, node)
                    del unmarked_trees[degree]
                    degree += 1
                unmarked_trees[degree] = node
                node = node.right
                if node == self.min_node:
                    break

            for node in unmarked_trees.values():
                if node.key < self.min_node.key:
                    self.min_node = node

        self.num_nodes -= 1
        return min_node.value

    def decrease_key(self, node: FibonacciHeapNode[T], new_key: float) -> None:
        assert new_key < node.key, 'New key must be less than old key'
        node.key = new_key

        parent = node.parent
        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)

        if node.key < self.min_node.key:
            self.min_node = node

    def is_empty(self) -> bool:
        return self.num_nodes == 0

    def _merge_with_list(self, node: FibonacciHeapNode[T]) -> None:
        if self.min_node is None:
            self.min_node = node
        else:
            self._insert_into_list(self.min_node, node)
            if node.key < self.min_node.key:
                self.min_node = node

    def _insert_into_list(self, head: FibonacciHeapNode[T], node: FibonacciHeapNode[T]) -> None:
        node.left = head.left
        node.right = head
        head.left.right = node
        head.left = node

    def _remove_from_list(self, node: FibonacciHeapNode[T]) -> None:
        node.left.right = node.right
        node.right.left = node.left

    def _link(self, node1: FibonacciHeapNode[T], node2: FibonacciHeapNode[T]) -> None:
        # make node1 a child of node2
        self._remove_from_list(node1)
        node1.parent = node2
        node1.marked = False
        if node2.child is None:
            node2.child = node1
            node1.left = node1.right = node1
        else:
            self._insert_into_list(node2.child, node1)
        node2.degree += 1

    def _cut(self, node: FibonacciHeapNode[T], parent: FibonacciHeapNode[T]) -> None:
        self._remove_from_list(node)
        parent.degree -= 1
        node.parent = None
        node.marked = False
        self._merge_with_list(node)

    def _cascading_cut(self, node: FibonacciHeapNode[T]) -> None:
        parent = node.parent
        if parent is not None:
            if not node.marked:
                node.marked = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)


class TestFibonacciHeap(unittest.TestCase):
    def test_insert_find_min(self):
        # create a new Fibonacci heap
        heap = FibonacciHeap[int]()

        # insert some elements into the heap
        heap.insert(5, 5)
        heap.insert(3, 3)
        heap.insert(7, 7)
        heap.insert(1, 1)

        # check that the minimum element in the heap is correct
        self.assertEqual(heap.find_min(), 1)

    def test_delete_min(self):
        # create a new Fibonacci heap
        heap = FibonacciHeap[int]()

        # insert some elements into the heap
        heap.insert(5, 5)
        heap.insert(3, 3)
        heap.insert(7, 7)
        heap.insert(1, 1)

        # delete the minimum element from the heap
        heap.delete_min()

        # check that the minimum element in the heap is correct
        self.assertEqual(heap.find_min(), 3)

    def test_empty_heap(self):
        # create a new Fibonacci heap
        heap = FibonacciHeap[int]()

        # check that the minimum element in an empty heap is None
        self.assertIsNone(heap.find_min())

        # deleting the minimum element from an empty heap should return None
        self.assertIsNone(heap.delete_min())


if __name__ == '__main__':
    unittest.main()
