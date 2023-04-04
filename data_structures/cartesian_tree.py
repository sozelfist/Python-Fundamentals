from typing import List, Optional
import unittest


class Node:
    def __init__(self, value: int, parent: Optional['Node'] = None):
        self.value = value
        self.parent = parent
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self):
        return str(self.value)

    def inorder_traversal(self) -> List[int]:
        values = []
        if self.left is not None:
            values.extend(self.left.inorder_traversal())
        values.append(self.value)
        if self.right is not None:
            values.extend(self.right.inorder_traversal())
        return values


class CartesianTree:
    def __init__(self, arr: List[int]):
        self.root = self.construct_cartesian_tree(arr)

    def construct_cartesian_tree(self, arr: List[int]) -> Optional[Node]:
        if not arr:
            return None

        min_value, min_index = min(zip(arr, range(len(arr))))
        node = Node(min_value)

        node.left = self.construct_cartesian_tree(arr[:min_index])
        if node.left:
            node.left.parent = node

        node.right = self.construct_cartesian_tree(arr[min_index + 1:])
        if node.right:
            node.right.parent = node

        return node

    def inorder_traversal(self) -> List[int]:
        if self.root is not None:
            return self.root.inorder_traversal()
        else:
            return []


class TestCartesianTree(unittest.TestCase):
    def test_inorder_traversal(self):
        # Test inorder traversal on a simple tree
        ct = CartesianTree([3, 2, 1])
        self.assertEqual(ct.inorder_traversal(), [3, 2, 1])

        # Test inorder traversal on a more complex tree
        ct = CartesianTree([3, 2, 1, 5, 4, 6])
        self.assertEqual(ct.inorder_traversal(), [3, 2, 1, 5, 4, 6])

    def test_construct_cartesian_tree(self):
        # Test construction of a simple tree
        ct = CartesianTree([1, 2, 3])
        self.assertEqual(ct.inorder_traversal(), [1, 2, 3])

        # Test construction of a more complex tree
        ct = CartesianTree([3, 2, 1, 5, 4, 6])
        self.assertEqual(ct.inorder_traversal(), [3, 2, 1, 5, 4, 6])

    def test_inorder_traversal_empty_tree(self):
        # Test inorder traversal on an empty tree
        ct = CartesianTree([])
        self.assertEqual(ct.inorder_traversal(), [])

    def test_construct_cartesian_tree_empty_list(self):
        # Test construction of a tree from an empty list
        ct = CartesianTree([])
        self.assertEqual(ct.inorder_traversal(), [])


if __name__ == '__main__':
    unittest.main()
