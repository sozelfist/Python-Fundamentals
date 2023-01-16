import unittest


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item: int) -> None:
        self.items.append(item)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def __repr__(self) -> str:
        return str(self)


class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        my_queue = Queue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertEqual(my_queue.dequeue(), 1)
        self.assertEqual(my_queue.dequeue(), 2)
        self.assertEqual(my_queue.dequeue(), 3)

    def test_peek(self):
        my_queue = Queue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertEqual(my_queue.peek(), 1)
        self.assertEqual(my_queue.peek(), 1)

    def test_is_empty(self):
        my_queue = Queue()
        self.assertEqual(my_queue.is_empty(), True)
        my_queue.enqueue(1)
        self.assertEqual(my_queue.is_empty(), False)

    def test_size(self):
        my_queue = Queue()
        self.assertEqual(my_queue.size(), 0)
        my_queue.enqueue(1)
        self.assertEqual(my_queue.size(), 1)

    def test_exception(self):
        my_queue = Queue()
        with self.assertRaises(IndexError):
            my_queue.dequeue()
        with self.assertRaises(IndexError):
            my_queue.peek()


if __name__ == '__main__':
    unittest.main()
