import unittest
from typing import Union


class BinaryTree:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data: int) -> None:
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data: int, parent: Union[None, 'BinaryTree'] = None) -> Union[None, 'BinaryTree']:
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self) -> int:
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, data: int) -> Union[None, 'BinaryTree']:
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                    del node
                else:
                    self.data = None
            elif children_count == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    del node
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def __str__(self):
        return self._print_tree("", True, "")

    def _print_tree(self, prefix: str, is_tail: bool, s: str) -> str:
        s += prefix + ("└── " if is_tail else "├── ") + str(self.data) + "\n"
        children = []
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)
        for i, child in enumerate(children):
            s = child._print_tree(
                prefix + ("    " if is_tail else "│   "), i == len(children) - 1, s)
        return s


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.binary_tree = BinaryTree(10)
        self.binary_tree.insert(5)
        self.binary_tree.insert(15)
        self.binary_tree.insert(3)
        self.binary_tree.insert(7)
        self.binary_tree.insert(12)
        self.binary_tree.insert(17)

    def test_insert(self):
        self.binary_tree.insert(1)
        self.binary_tree.insert(2)
        self.assertEqual(self.binary_tree.left.left.data, 3)
        self.assertEqual(self.binary_tree.left.left.left.data, 1)

    def test_lookup(self):
        node, parent = self.binary_tree.lookup(7)
        self.assertEqual(node.data, 7)
        self.assertEqual(parent.data, 5)

    def test_children_count(self):
        node, _ = self.binary_tree.lookup(7)
        self.assertEqual(node.children_count(), 0)
        node, _ = self.binary_tree.lookup(15)
        self.assertEqual(node.children_count(), 2)

    def test_delete(self):
        self.binary_tree.delete(15)
        node, _ = self.binary_tree.lookup(15)
        self.assertIsNone(node)
        self.assertEqual(self.binary_tree.right.data, 17)

    # if you have a test string method, let's create pull request to add
    # the method


if __name__ == "__main__":
    unittest.main()
