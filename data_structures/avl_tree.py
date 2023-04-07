import unittest


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node: Node) -> int:
        if not node:
            return 0
        return node.height

    def get_balance(self, node: Node) -> int:
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, node: Node) -> Node:
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left_child.height = 1 + max(self.get_height(left_child.left), self.get_height(left_child.right))
        return left_child

    def left_rotate(self, node: Node) -> Node:
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right_child.height = 1 + max(self.get_height(right_child.left), self.get_height(right_child.right))
        return right_child

    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def _insert(self, node: Node, key: int) -> Node:
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def search(self, key: int) -> Node | None:
        curr = self.root
        while curr:
            if key == curr.key:
                return curr
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def delete(self, key: int) -> None:
        self.root = self._delete(self.root, key)

    def _delete(self, node: Node, key: int) -> Node:
        if not node:
            return None
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                successor = self._find_successor(node.right)
                node.key = successor.key
                node.right = self._delete(node.right, successor.key)
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) >= 0:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        if balance < -1:
            if self.get_balance(node.right) <= 0:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        return node

    def _find_successor(self, node: Node) -> Node:
        if not node.left:
            return node
        return self._find_successor(node.left)

    def inorder_traversal(self) -> list[int]:
        res = []
        self._inorder_traversal(self.root, res)
        return res

    def _inorder_traversal(self, node: Node, res: list[int]) -> None:
        if node:
            self._inorder_traversal(node.left, res)
            res.append(node.key)
            self._inorder_traversal(node.right, res)

    def preorder_traversal(self) -> list[int]:
        res = []
        self._preorder_traversal(self.root, res)
        return res

    def _preorder_traversal(self, node: Node, res: list[int]) -> None:
        if node:
            res.append(node.key)
            self._preorder_traversal(node.left, res)
            self._preorder_traversal(node.right, res)

    def postorder_traversal(self) -> list[int]:
        res = []
        self._postorder_traversal(self.root, res)
        return res

    def _postorder_traversal(self, node: Node, res: list[int]) -> None:
        if node:
            self._postorder_traversal(node.left, res)
            self._postorder_traversal(node.right, res)
            res.append(node.key)


class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def test_insert(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.insert(40)
        self.tree.insert(50)
        self.tree.insert(25)
        self.assertEqual(self.tree.root.key, 30)
        self.assertEqual(self.tree.root.left.key, 20)
        self.assertEqual(self.tree.root.right.key, 40)

    def test_search(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.insert(40)
        self.tree.insert(50)
        self.tree.insert(25)
        self.assertEqual(self.tree.search(20).key, 20)
        self.assertEqual(self.tree.search(35), None)

    def test_delete(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.insert(40)
        self.tree.insert(50)
        self.tree.insert(25)
        self.tree.delete(20)
        self.assertEqual(self.tree.root.key, 30)
        self.assertEqual(self.tree.root.left.key, 25)
        self.tree.delete(30)
        self.assertEqual(self.tree.root.key, 40)
        self.assertEqual(self.tree.root.right.key, 50)

    def test_inorder_traversal(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.insert(40)
        self.tree.insert(50)
        self.tree.insert(25)
        self.assertEqual(self.tree.inorder_traversal(), [10, 20, 25, 30, 40, 50])

    def test_preorder_traversal(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.insert(40)
        self.tree.insert(50)
        self.tree.insert(25)
        self.assertEqual(self.tree.preorder_traversal(), [30, 20, 10, 25, 40, 50])

    def test_postorder_traversal(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.insert(40)
        self.tree.insert(50)
        self.tree.insert(25)
        self.assertEqual(self.tree.postorder_traversal(), [10, 25, 20, 50, 40, 30])


if __name__ == '__main__':
    unittest.main()
