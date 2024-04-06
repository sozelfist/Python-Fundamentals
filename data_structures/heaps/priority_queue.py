import unittest


class PriorityQueue:
    def __init__(
        self, is_min_heap: bool = True, values: list[tuple[int, str]] | None = None
    ):
        self.heap = []
        self.is_min_heap = is_min_heap
        if values:
            self.heap = values
            self.build_heap()

    def should_swap(self, parent: tuple[int, str], child: tuple[int, str]) -> bool:
        if self.is_min_heap:
            return parent[0] > child[0]
        else:
            return parent[0] < child[0]

    def insert(self, value: tuple[int, str]):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def peek(self) -> tuple[int, str]:
        if len(self.heap) == 0:
            raise ValueError("Heap is empty")
        return self.heap[0]

    def poll(self) -> tuple[int, str]:
        if len(self.heap) == 0:
            raise ValueError("Heap is empty")
        value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return value

    def heapify_up(self, index: int):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.should_swap(self.heap[parent_index], self.heap[index]):
                self.heap[parent_index], self.heap[index] = (
                    self.heap[index],
                    self.heap[parent_index],
                )
                index = parent_index
            else:
                break

    def heapify_down(self, index: int):
        while index < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            if left_child_index >= len(self.heap):
                break
            if right_child_index >= len(self.heap):
                swap_index = left_child_index
            else:
                if self.should_swap(
                    self.heap[left_child_index], self.heap[right_child_index]
                ):
                    swap_index = left_child_index
                else:
                    swap_index = right_child_index
            if self.should_swap(self.heap[index], self.heap[swap_index]):
                self.heap[index], self.heap[swap_index] = (
                    self.heap[swap_index],
                    self.heap[index],
                )
                index = swap_index
            else:
                break

    def build_heap(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def __str__(self):
        return str(self.heap)


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    def test_insert(self):
        self.pq.insert((1, "a"))
        self.pq.insert((2, "b"))
        self.pq.insert((3, "c"))
        self.assertEqual(self.pq.heap, [(1, "a"), (2, "b"), (3, "c")])

    def test_peek(self):
        self.pq.insert((1, "a"))
        self.pq.insert((2, "b"))
        self.pq.insert((3, "c"))
        self.assertEqual(self.pq.peek(), (1, "a"))

    def test_poll(self):
        self.pq.insert((1, "a"))
        self.pq.insert((2, "b"))
        self.pq.insert((3, "c"))
        self.assertEqual(self.pq.poll(), (1, "a"))
        self.assertEqual(self.pq.heap, [(2, "b"), (3, "c")])

    def test_init_with_list(self):
        pq = PriorityQueue(values=[(3, "c"), (2, "b"), (1, "a")])
        self.assertEqual(pq.heap, [(2, "b"), (3, "c"), (1, "a")])

    def test_init_max_heap(self):
        pq = PriorityQueue(is_min_heap=False, values=[(3, "c"), (2, "b"), (1, "a")])
        self.assertEqual(pq.heap, [(3, "c"), (2, "b"), (1, "a")])


if __name__ == "__main__":
    unittest.main()
