import unittest
from typing import List


def heap_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def heapify(arr: List[int], n: int, i: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


class TestHeapSort(unittest.TestCase):
    def test_heap_sort_basic(self):
        self.assertEqual(heap_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(heap_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(heap_sort([-1, 2, -3]), [-3, -1, 2])
        self.assertEqual(heap_sort([1]), [1])
        self.assertEqual(heap_sort([]), [])

    def test_heap_sort_performance(self):
        import random
        for i in range(0, 10):
            arr = random.sample(range(-10000, 10000), 10000)
            self.assertEqual(heap_sort(arr), sorted(arr))

    def test_heap_sort_large_input(self):
        import random
        arr = random.sample(range(-1000000, 1000000), 100000)
        self.assertEqual(heap_sort(arr), sorted(arr))


if __name__ == '__main__':
    unittest.main()
