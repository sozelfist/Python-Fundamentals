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
        self.tree = BinaryTree(8)
        self.tree.insert(3)
        self.tree.insert(10)
        self.tree.insert(1)
        self.tree.insert(6)
        self.tree.insert(14)
        self.tree.insert(4)
        self.tree.insert(7)
        self.tree.insert(13)

    def test_insert(self):
        self.tree.insert(5)
        self.assertEqual(
            str(self.tree), "8\n├── 3\n│   ├── 1\n│   │   └── None\n│   │\n│   └── 6\n│       ├── 4\n│       \
                │   └── None\n│       │\n│       └── 7\n│           └── None\n│\n└── 14\n    ├── 13\n    \
                    │   └── None\n    │\n    └── None\n"
        )

    def test_lookup(self):
        node, parent = self.tree.lookup(14)
        self.assertEqual(node.data, 14)
        self.assertEqual(parent.data, 10)

    def test_delete(self):
        self.tree.delete(10)
        self.assertEqual(str(self.tree), "8\n├── 3\n│   ├── 1\n│   \
        │   └── None\n│   │\n│   └── 6\n│       \
        ├── 4\n│       │   └── None\n│       │\n│       └── 7\n│           └── None\n│\n└── 14\n    ├── 13\n    \
        │   └── None\n    │\n    └── None\n")
        self.tree.delete(3)
        self.assertEqual(str(
            self.tree), "8\n├── 6\n│   ├── 4\n│   │   └── None\n│   │\n│   └── 7\n│       └── None\n│\n└── 14\n    \
        ├── 13\n    │   └── None\n    │\n    └── None\n")
        self.tree.delete(8)
        self.assertEqual(str(self.tree), "6\n├── 4\n│   └── None\n│\n└── 7\n    └── None\n")


if __name__ == '__main__':
    unittest.main()
