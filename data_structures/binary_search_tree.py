import unittest


class BST:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data: int) -> None:
        if data <= self.data:
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data)

    def find(self, data: int) -> bool:
        if data == self.data:
            return True
        if data < self.data:
            if self.left is None:
                return False
            return self.left.find(data)
        else:
            if self.right is None:
                return False
            return self.right.find(data)

    def min_value(self) -> int:
        current = self
        while current.left is not None:
            current = current.left
        return current.data

    def max_value(self) -> int:
        current = self
        while current.right is not None:
            current = current.right
        return current.data

    def delete(self, data: int) -> None:
        if data < self.data:
            self.left = self.left.delete(data)
        elif data > self.data:
            self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.min_value()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

    def preorder(self) -> list[int]:
        result = []
        result.append(self.data)
        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result

    def inorder(self) -> list[int]:
        result = []
        if self.left:
            result += self.left.inorder()
        result.append(self.data)
        if self.right:
            result += self.right.inorder()
        return result

    def postorder(self) -> list[int]:
        result = []
        if self.left:
            result += self.left.postorder()
        if self.right:
            result += self.right.postorder()
        result.append(self.data)
        return result

    def height(self) -> int:
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return max(left_height, right_height) + 1

    def size(self) -> int:
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return left_size + right_size + 1

    def is_balanced(self) -> bool:
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        if abs(left_height - right_height) > 1:
            return False
        left_balanced = self.left.is_balanced() if self.left else True
        right_balanced = self.right.is_balanced() if self.right else True
        return left_balanced and right_balanced


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BST(5)

    def test_insert(self):
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.bst.insert(2)
        self.bst.insert(9)
        self.assertEqual(self.bst.find(3), True)
        self.assertEqual(self.bst.find(7), True)
        self.assertEqual(self.bst.find(1), True)
        self.assertEqual(self.bst.find(4), True)
        self.assertEqual(self.bst.find(6), True)
        self.assertEqual(self.bst.find(8), True)
        self.assertEqual(self.bst.find(2), True)
        self.assertEqual(self.bst.find(9), True)

    def test_delete(self):
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.bst.insert(2)
        self.bst.insert(9)
        self.bst.delete(3)
        self.assertEqual(self.bst.find(3), False)
        self.assertEqual(self.bst.find(7), True)
        self.assertEqual(self.bst.find(1), True)
        self.assertEqual(self.bst.find(4), True)
        self.assertEqual(self.bst.find(6), True)
        self.assertEqual(self.bst.find(8), True)
        self.assertEqual(self.bst.find(2), True)
        self.assertEqual(self.bst.find(9), True)

    def test_min_value(self):
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.bst.insert(2)
        self.bst.insert(9)
        self.assertEqual(self.bst.min_value(), 1)

    def test_max_value(self):
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.bst.insert(2)
        self.bst.insert(9)
        self.assertEqual(self.bst.max_value(), 9)

    def test_preorder(self):
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.bst.insert(2)
        self.bst.insert(9)
        self.assertEqual(self.bst.preorder(), [5, 3, 1, 2, 4, 7, 6, 8, 9])

    def test_inorder(self):
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.bst.insert(2)
        self.bst.insert(9)
        self.assertEqual(self.bst.inorder(), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_postorder(self):
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.bst.insert(2)
        self.bst.insert(9)
        self.assertEqual(self.bst.postorder(), [2, 1, 4, 3, 6, 9, 8, 7, 5])

    def test_height(self):
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.bst.insert(2)
        self.bst.insert(9)
        self.assertEqual(self.bst.height(), 4)

    def test_size(self):
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.bst.insert(2)
        self.bst.insert(9)
        self.assertEqual(self.bst.size(), 9)

    def test_is_balanced(self):
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.bst.insert(2)
        self.bst.insert(9)
        self.assertEqual(self.bst.is_balanced(), True)

    def test_is_balanced_unbalanced(self):
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.bst.insert(2)
        self.bst.insert(9)
        self.bst.insert(10)
        self.bst.insert(11)
        self.bst.insert(12)
        self.assertEqual(self.bst.is_balanced(), False)


if __name__ == '__main__':
    unittest.main()
