import unittest
from typing import List


class Heap:
    def __init__(self, is_min: bool, arr: List[int] = None):
        self.is_min = is_min
        self.heap = arr if arr else []
        self.build_heap()

    def build_heap(self) -> None:
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i: int) -> None:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(self.heap) and (self.heap[left] < self.heap[smallest]
                                      if self.is_min else self.heap[left] > self.heap[smallest]):
            smallest = left
        if right < len(self.heap) and (self.heap[right] < self.heap[smallest]
                                       if self.is_min else self.heap[right] > self.heap[smallest]):
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def push(self, value: int) -> None:
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0 and (self.heap[i] < self.heap[(i - 1) // 2]
                         if self.is_min else self.heap[i] > self.heap[(i - 1) // 2]):
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def pop(self) -> int:
        if not self.heap:
            raise Exception("Heap is empty")
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        result = self.heap.pop()
        self.heapify(0)
        return result

    def poll(self) -> int:
        """
        Returns the root element of the heap and removes it from the heap
        """
        if not self.heap:
            raise Exception("Heap is empty")
        result = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return result

    def top(self) -> int:
        if not self.heap:
            raise Exception("Heap is empty")
        return self.heap[0]

    def __len__(self) -> int:
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    def __iter__(self):
        for i in self.heap:
            yield i


class TestHeap(unittest.TestCase):
    def test_push_pop_top_min_heap(self):
        heap = Heap(is_min=True)
        heap.push(3)
        heap.push(2)
        heap.push(1)
        self.assertEqual(heap.top(), 1)
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.pop(), 3)

    def test_push_pop_top_max_heap(self):
        heap = Heap(is_min=False)
        heap.push(3)
        heap.push(2)
        heap.push(1)
        self.assertEqual(heap.top(), 3)
        self.assertEqual(heap.pop(), 3)
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.pop(), 1)

    def test_init_with_list_min_heap(self):
        heap = Heap(is_min=True, arr=[3, 2, 1])
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.pop(), 3)

    def test_init_with_list_max_heap(self):
        heap = Heap(is_min=False, arr=[3, 2, 1])
        self.assertEqual(heap.pop(), 3)
        self.assertEqual(heap.pop(), 2)

    def test_poll_min_heap(self):
        heap = Heap(is_min=True, arr=[3, 2, 1])
        self.assertEqual(heap.poll(), 1)
        self.assertEqual(heap.poll(), 2)

    def test_poll_max_heap(self):
        heap = Heap(is_min=False, arr=[3, 2, 1])
        self.assertEqual(heap.poll(), 3)
        self.assertEqual(heap.poll(), 2)

    def test_iteration(self):
        heap = Heap(is_min=True, arr=[3, 2, 1])
        self.assertEqual(list(iter(heap)), [1, 2, 3])
        heap = Heap(is_min=False, arr=[3, 2, 1])
        self.assertEqual(list(iter(heap)), [3, 2, 1])

    def test_len(self):
        heap = Heap(is_min=True, arr=[3, 2, 1])
        self.assertEqual(len(heap), 3)
        heap = Heap(is_min=False, arr=[3, 2, 1])
        self.assertEqual(len(heap), 3)

    def test_repr(self):
        heap = Heap(is_min=True, arr=[3, 2, 1])
        self.assertEqual(repr(heap), str([1, 2, 3]))
        heap = Heap(is_min=False, arr=[3, 2, 1])
        self.assertEqual(repr(heap), str([3, 2, 1]))


if __name__ == '__main__':
    unittest.main()
