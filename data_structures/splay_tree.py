import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def splay(self, x):
        while x.parent is not None:
            if x.parent.parent is None:
                if x == x.parent.left:
                    self.right_rotate(x.parent)
                else:
                    self.left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self.right_rotate(x.parent.parent)
                self.right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self.left_rotate(x.parent.parent)
                self.left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self.left_rotate(x.parent)
                self.right_rotate(x.parent)
            else:
                self.right_rotate(x.parent)
                self.left_rotate(x.parent)

    def insert(self, key):
        node = Node(key)
        if self.root is None:
            self.root = node
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = node
                    node.parent = current
                    self.splay(node)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    node.parent = current
                    self.splay(node)
                    return
                current = current.right

    def find(self, key):
        current = self.root
        while current is not None:
            if current.key == key:
                self.splay(current)
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, key):
        node = self.find(key)
        if node is None:
            return
        if node.left is None:
            child = node.right
            self.transplant(node, child)
        elif node.right is None:
            child = node.left
            self.transplant(node, child)
        else:
            successor = self.minimum(node.right)
            if successor.parent != node:
                self.transplant(successor, successor.right)
                successor.right = node.right
                if successor.right is not None:
                    successor.right.parent = successor
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
        self.root = node.parent

    def minimum(self, node=None):
        if node is None:
            node = self.root
        while node.left is not None:
            node = node.left
        self.splay(node)
        return node

    def maximum(self):
        node = self.root
        while node.right is not None:
            node = node.right
        self.splay(node)
        return node

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def in_order(self, node=None):
        if node is None:
            node = self.root
        keys = []
        if node.left is not None:
            keys += self.in_order(node.left)
        keys.append(node.key)
        if node.right is not None:
            keys += self.in_order(node.right)
        return keys

    def pre_order(self, node=None):
        if node is None:
            node = self.root
        keys = [node.key]
        if node.left is not None:
            keys += self.pre_order(node.left)
        if node.right is not None:
            keys += self.pre_order(node.right)
        return keys

    def post_order(self, node=None):
        if node is None:
            node = self.root
        keys = []
        if node.left is not None:
            keys += self.post_order(node.left)
        if node.right is not None:
            keys += self.post_order(node.right)
        keys.append(node.key)
        return keys


class TestSplayTree(unittest.TestCase):

    def test_insert_and_find(self):
        tree = SplayTree()
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(1)
        tree.insert(3)
        tree.insert(7)
        tree.insert(9)
        node = tree.find(3)
        self.assertEqual(node.key, 3)

    def test_delete(self):
        tree = SplayTree()
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(1)
        tree.insert(3)
        tree.insert(7)
        tree.insert(9)
        tree.delete(2)
        node = tree.find(2)
        self.assertIsNone(node)

    def test_minimum(self):
        tree = SplayTree()
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(1)
        tree.insert(3)
        tree.insert(7)
        tree.insert(9)
        node = tree.minimum()
        self.assertEqual(node.key, 1)

    def test_maximum(self):
        tree = SplayTree()
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(1)
        tree.insert(3)
        tree.insert(7)
        tree.insert(9)
        node = tree.maximum()
        self.assertEqual(node.key, 9)

    def test_in_order(self):
        tree = SplayTree()
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(1)
        tree.insert(3)
        tree.insert(7)
        tree.insert(9)
        keys = tree.in_order()
        self.assertListEqual(keys, [1, 2, 3, 5, 7, 8, 9])

    def test_pre_order(self):
        tree = SplayTree()
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(1)
        tree.insert(3)
        tree.insert(7)
        tree.insert(9)
        keys = tree.pre_order()
        self.assertListEqual(keys, [9, 8, 7, 3, 1, 2, 5])

    def test_post_order(self):
        tree = SplayTree()
        tree.insert(5)
        tree.insert(2)
        tree.insert(8)
        tree.insert(1)
        tree.insert(3)
        tree.insert(7)
        tree.insert(9)
        keys = tree.post_order()
        self.assertListEqual(keys, [2, 1, 5, 3, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
