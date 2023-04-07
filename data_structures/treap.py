import unittest


class Node:
    def __init__(self, key: int, priority: int):
        self.key = key
        self.priority = priority
        self.left: Node | None = None
        self.right: Node | None = None


class Treap:
    def __init__(self):
        self.root: Node | None = None

    def _rotate_left(self, node: Node) -> Node:
        # Perform a left rotation of the given node and its right child
        y = node.right
        node.right = y.left
        y.left = node
        return y

    def _rotate_right(self, node: Node) -> Node:
        # Perform a right rotation of the given node and its left child
        x = node.left
        node.left = x.right
        x.right = node
        return x

    def insert(self, key: int, priority: int) -> None:
        # Insert a new node with the given key and priority into the Treap
        if self.root is None:
            self.root = Node(key, priority)
        else:
            self.root = self._insert_helper(self.root, key, priority)

    def _insert_helper(self, node: Node, key: int, priority: int) -> Node:
        # Recursively insert a new node with the given key and priority into the Treap
        if node is None:
            return Node(key, priority)

        if key < node.key:
            node.left = self._insert_helper(node.left, key, priority)
            if node.left.priority < node.priority:
                node = self._rotate_right(node)
        else:
            node.right = self._insert_helper(node.right, key, priority)
            if node.right.priority < node.priority:
                node = self._rotate_left(node)

        return node

    def delete(self, key: int) -> None:
        # Delete the node with the given key from the Treap
        if self.root is None:
            return
        self.root = self._delete_helper(self.root, key)

    def _delete_helper(self, node: Node, key: int) -> Node | None:
        # Recursively delete the node with the given key from the Treap
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_helper(node.left, key)
        elif key > node.key:
            node.right = self._delete_helper(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            elif node.left.priority < node.right.priority:
                node = self._rotate_right(node)
                node.right = self._delete_helper(node.right, key)
            else:
                node = self._rotate_left(node)
                node.left = self._delete_helper(node.left, key)

        return node

    def search(self, key: int) -> Node | None:
        # Search for a node with the given key in the Treap
        node = self.root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return (node.key, node.priority)
        return None

    def in_order_traversal(self, node: Node | None = None) -> list[tuple]:
        result = []
        if not node:
            node = self.root
        if node.left:
            result.extend(self.in_order_traversal(node.left))
        result.append((node.key, node.priority))
        if node.right:
            result.extend(self.in_order_traversal(node.right))
        return result

    def pre_order_traversal(self, node: Node | None = None) -> list[tuple]:
        result = []
        if not node:
            node = self.root
        result.append((node.key, node.priority))
        if node.left:
            result.extend(self.pre_order_traversal(node.left))
        if node.right:
            result.extend(self.pre_order_traversal(node.right))
        return result

    def post_order_traversal(self, node: Node | None = None) -> list[tuple]:
        result = []
        if not node:
            node = self.root
        if node.left:
            result.extend(self.post_order_traversal(node.left))
        if node.right:
            result.extend(self.post_order_traversal(node.right))
        result.append((node.key, node.priority))
        return result


class TestTreap(unittest.TestCase):
    def test_insert(self):
        treap = Treap()
        treap.insert(5, 10)
        treap.insert(3, 20)
        treap.insert(7, 30)
        treap.insert(2, 40)
        treap.insert(4, 50)
        treap.insert(6, 60)
        treap.insert(8, 70)

        expected_in_order = [(2, 40), (3, 20), (4, 50), (5, 10), (6, 60), (7, 30), (8, 70)]
        self.assertEqual(treap.in_order_traversal(), expected_in_order)

        expected_pre_order = [(5, 10), (3, 20), (2, 40), (4, 50), (7, 30), (6, 60), (8, 70)]
        self.assertEqual(treap.pre_order_traversal(), expected_pre_order)

    def test_delete(self):
        treap = Treap()
        treap.insert(5, 10)
        treap.insert(3, 20)
        treap.insert(7, 30)
        treap.insert(2, 40)
        treap.insert(4, 50)
        treap.insert(6, 60)
        treap.insert(8, 70)

        treap.delete(2)
        expected_in_order = [(3, 20), (4, 50), (5, 10), (6, 60), (7, 30), (8, 70)]
        self.assertEqual(treap.in_order_traversal(), expected_in_order)

        treap.delete(7)
        expected_pre_order = [(5, 10), (3, 20), (4, 50), (6, 60), (8, 70)]
        self.assertEqual(treap.pre_order_traversal(), expected_pre_order)

    def test_search(self):
        treap = Treap()
        treap.insert(5, 10)
        treap.insert(3, 20)
        treap.insert(7, 30)
        treap.insert(2, 40)
        treap.insert(4, 50)
        treap.insert(6, 60)
        treap.insert(8, 70)

        self.assertEqual(treap.search(2), (2, 40))
        self.assertEqual(treap.search(7), (7, 30))
        self.assertEqual(treap.search(9), None)


if __name__ == '__main__':
    unittest.main()
