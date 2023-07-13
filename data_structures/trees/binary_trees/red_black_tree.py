from __future__ import annotations

import unittest


class Node:
    def __init__(
        self, key: int, color: str, left=None, right=None, parent=None
    ):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, "black")
        self.root = self.nil

    def search(self, key: int) -> Node | None:
        current = self.root
        while current != self.nil and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current if current != self.nil else None

    def minimum(self, node: Node) -> Node:
        while node.left != self.nil:
            node = node.left
        return node

    def maximum(self, node: Node) -> Node:
        while node.right != self.nil:
            node = node.right
        return node

    def transplant(self, u: Node, v: Node) -> None:
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def left_rotate(self, x: Node) -> None:
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x: Node) -> None:
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key: int) -> None:
        z = Node(key, "red", left=self.nil, right=self.nil)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self.insert_fixup(z)

    def insert_fixup(self, z: Node) -> None:
        while z.parent.color == "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "black"

    def delete(self, key: int) -> None:
        z = self.search(key)
        if z == self.nil:
            return
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "black":
            self.delete_fixup(x)

    def delete_fixup(self, x: Node) -> None:
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.right.color == "black":
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "black" and w.left.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.left.color == "black":
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"

    def find_min(self) -> Node | None:
        """
        Returns the node with the minimum key value in the tree.
        """
        current = self.root
        while current.left != self.nil:
            current = current.left
        return current if current != self.nil else None

    def find_max(self) -> Node | None:
        """
        Returns the node with the maximum key value in the tree.
        """
        current = self.root
        while current.right != self.nil:
            current = current.right
        return current if current != self.nil else None

    def in_order_traversal(self, node: Node | None) -> None:
        """
        Traverses the tree in in-order and prints the key values of the nodes.
        """
        if node != self.nil:
            self.in_order_traversal(node.left)
            print(node.key)
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node: Node | None) -> None:
        """
        Traverses the tree in pre-order and prints the key values of the nodes.
        """
        if node != self.nil:
            print(node.key)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node: Node | None) -> None:
        """
        Traverses the tree in post-order and prints the key
        values of the nodes.
        """
        if node != self.nil:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.key)


class TestRedBlackTree(unittest.TestCase):
    def setUp(self):
        self.tree = RedBlackTree()

    def test_insert(self):
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(12)
        self.tree.insert(20)

        self.assertEqual(self.tree.search(5).key, 5)
        self.assertEqual(self.tree.minimum(self.tree.root).key, 3)
        self.assertEqual(self.tree.maximum(self.tree.root).key, 20)
        self.assertIsNone(self.tree.search(30))

    def test_delete(self):
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(12)
        self.tree.insert(20)

        self.tree.delete(5)
        self.assertIsNone(self.tree.search(5))
        self.tree.delete(20)
        self.assertIsNone(self.tree.search(20))
        self.tree.delete(10)
        self.assertIsNone(self.tree.search(10))
        self.tree.delete(12)
        self.assertIsNone(self.tree.search(12))


if __name__ == "__main__":
    unittest.main()
