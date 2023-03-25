import unittest
from typing import List, TypeVar

T = TypeVar('T')


class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.buffer: List[T] = [None] * capacity
        self.head = 0
        self.tail = 0

    def is_empty(self) -> bool:
        return self.head == self.tail

    def is_full(self) -> bool:
        return (self.tail + 1) % self.capacity == self.head

    def enqueue(self, item: T) -> None:
        if self.is_full():
            raise ValueError("Circular buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity

    def dequeue(self) -> T:
        if self.is_empty():
            raise ValueError("Circular buffer is empty")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        return item


class TestCircularBuffer(unittest.TestCase):
    def test_enqueue_dequeue(self):
        buffer = CircularBuffer(4)
        buffer.enqueue(1)
        buffer.enqueue(2)
        buffer.enqueue(3)
        self.assertEqual(buffer.dequeue(), 1)
        buffer.enqueue(4)
        self.assertEqual(buffer.dequeue(), 2)
        self.assertEqual(buffer.dequeue(), 3)
        self.assertEqual(buffer.dequeue(), 4)

    def test_is_empty(self):
        buffer = CircularBuffer(3)
        self.assertTrue(buffer.is_empty())
        buffer.enqueue(1)
        self.assertFalse(buffer.is_empty())
        buffer.dequeue()
        self.assertTrue(buffer.is_empty())

    def test_is_full(self):
        buffer = CircularBuffer(4)
        self.assertFalse(buffer.is_full())
        buffer.enqueue(1)
        buffer.enqueue(2)
        buffer.enqueue(3)
        self.assertTrue(buffer.is_full())
        buffer.dequeue()
        self.assertFalse(buffer.is_full())

    def test_enqueue_full_buffer(self):
        buffer = CircularBuffer(3)
        buffer.enqueue(1)
        buffer.enqueue(2)
        with self.assertRaises(ValueError):
            buffer.enqueue(3)

    def test_dequeue_empty_buffer(self):
        buffer = CircularBuffer(2)
        with self.assertRaises(ValueError):
            buffer.dequeue()


if __name__ == '__main__':
    unittest.main()
