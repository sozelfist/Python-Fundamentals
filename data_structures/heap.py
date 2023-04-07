import unittest


class Heap:
    def __init__(self, is_min: bool, arr: list[int] | None = None):
        self.is_min = is_min
        self._heap = arr if arr else []
        self._heapify()

    def _heapify(self) -> None:
        n = len(self._heap)
        start = n // 2 - 1
        for i in range(start, -1, -1):
            self._sift_down(i, n)

    def _sift_down(self, i: int, n: int) -> None:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < n and (self._heap[left] < self._heap[smallest]
                         if self.is_min else self._heap[left] > self._heap[smallest]):
            smallest = left
        if right < n and (self._heap[right] < self._heap[smallest]
                          if self.is_min else self._heap[right] > self._heap[smallest]):
            smallest = right

        if smallest != i:
            self._heap[i], self._heap[smallest] = self._heap[smallest], self._heap[i]
            self._sift_down(smallest, n)

    def push(self, value: int) -> None:
        self._heap.append(value)
        self._sift_up(len(self._heap) - 1)

    def _sift_up(self, i: int) -> None:
        parent = (i - 1) // 2
        if parent >= 0 and (self._heap[i] < self._heap[parent]
                            if self.is_min else self._heap[i] > self._heap[parent]):
            self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
            self._sift_up(parent)

    def pop(self) -> int:
        if not self._heap:
            raise Exception("Heap is empty")
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._sift_down(0, len(self._heap))
        return result

    def poll(self) -> int:
        """
        Returns the root element of the heap and removes it from the heap
        """
        if not self._heap:
            raise Exception("Heap is empty")
        result = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._sift_down(0, len(self._heap))
        return result

    def top(self) -> int:
        if not self._heap:
            raise Exception("Heap is empty")
        return self._heap[0]

    def __len__(self) -> int:
        return len(self._heap)

    def __repr__(self):
        return str(self._heap)

    def __iter__(self):
        yield from self._heap


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
