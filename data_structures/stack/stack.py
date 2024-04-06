import unittest


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self) -> int:
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


class TestStack(unittest.TestCase):
    def test_push(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        self.assertEqual(my_stack.size(), 3)

    def test_pop(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        self.assertEqual(my_stack.pop(), 3)
        self.assertEqual(my_stack.pop(), 2)
        self.assertEqual(my_stack.pop(), 1)
        self.assertEqual(my_stack.size(), 0)

    def test_pop_empty(self):
        my_stack = Stack()
        with self.assertRaises(Exception) as context:
            my_stack.pop()
        self.assertTrue("Stack is empty" in str(context.exception))

    def test_peek(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        self.assertEqual(my_stack.peek(), 2)
        self.assertEqual(my_stack.pop(), 2)
        self.assertEqual(my_stack.peek(), 1)
        self.assertEqual(my_stack.size(), 1)

    def test_peek_empty(self):
        my_stack = Stack()
        with self.assertRaises(Exception) as context:
            my_stack.peek()
        self.assertTrue("Stack is empty" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
