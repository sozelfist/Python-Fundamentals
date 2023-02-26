from typing import Generic, Optional, TypeVar, Iterable
import unittest


T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.prev = None
        self.next = None


class Deque(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.count = 0

    def __len__(self) -> int:
        return self.count

    def appendleft(self, value: T) -> None:
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.count += 1

    def popleft(self) -> T:
        if self.head is None:
            raise IndexError('pop from an empty deque')
        value = self.head.value
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.count -= 1
        return value

    def append(self, value: T) -> None:
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def pop(self) -> T:
        if self.tail is None:
            raise IndexError('pop from an empty deque')
        value = self.tail.value
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.count -= 1
        return value

    def clear(self) -> None:
        self.head = self.tail = None
        self.count = 0

    def extend(self, iterable: Iterable) -> None:
        for value in iterable:
            self.append(value)

    def extendleft(self, iterable: Iterable) -> None:
        for value in reversed(iterable):
            self.appendleft(value)

    def remove(self, value: T) -> None:
        node = self.head
        while node is not None:
            if node.value == value:
                if node is self.head:
                    self.popleft()
                elif node is self.tail:
                    self.pop()
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.count -= 1
                return
            node = node.next
        raise ValueError(f"{value} is not in deque")

    def rotate(self, n: int = 1) -> None:
        if not self.head or not self.tail:
            return
        if n > 0:
            for _ in range(n):
                self.appendleft(self.pop())
        else:
            for _ in range(abs(n)):
                self.append(self.popleft())


class TestDeque(unittest.TestCase):
    def test_append(self):
        deque = Deque[int]()
        deque.append(1)
        deque.append(2)
        deque.append(3)
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque.pop(), 3)
        self.assertEqual(deque.pop(), 2)
        self.assertEqual(deque.pop(), 1)

    def test_appendleft(self):
        deque = Deque[int]()
        deque.appendleft(1)
        deque.appendleft(2)
        deque.appendleft(3)
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque.pop(), 1)
        self.assertEqual(deque.pop(), 2)
        self.assertEqual(deque.pop(), 3)

    def test_extend(self):
        deque = Deque[int]()
        deque.extend([1, 2, 3])
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque.pop(), 3)
        self.assertEqual(deque.pop(), 2)
        self.assertEqual(deque.pop(), 1)

    def test_extendleft(self):
        deque = Deque[int]()
        deque.extendleft([1, 2, 3])
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque.pop(), 3)
        self.assertEqual(deque.pop(), 2)
        self.assertEqual(deque.pop(), 1)

    def test_pop(self):
        deque = Deque[int]()
        deque.extend([1, 2, 3])
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque.pop(), 3)
        self.assertEqual(deque.pop(), 2)
        self.assertEqual(deque.pop(), 1)
        self.assertRaises(IndexError, deque.pop)

    def test_popleft(self):
        deque = Deque[int]()
        deque.extend([1, 2, 3])
        self.assertEqual(len(deque), 3)
        self.assertEqual(deque.popleft(), 1)
        self.assertEqual(deque.popleft(), 2)
        self.assertEqual(deque.popleft(), 3)
        self.assertRaises(IndexError, deque.popleft)


if __name__ == '__main__':
    unittest.main()
