import unittest
import random
from typing import List


def quick_sort(arr: List[int], low: int, high: int) -> List[int]:
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)
    return arr


def partition(arr: List[int], low: int, high: int) -> int:
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


class TestQuickSort(unittest.TestCase):
    def test_quick_sort_basic(self):
        self.assertEqual(quick_sort([3, 2, 1], 0, 2), [1, 2, 3])
        self.assertEqual(quick_sort([1, 2, 3], 0, 2), [1, 2, 3])
        self.assertEqual(quick_sort([-1, 2, -3], 0, 2), [-3, -1, 2])
        self.assertEqual(quick_sort([1], 0, 0), [1])
        self.assertEqual(quick_sort([], 0, 0), [])


if __name__ == '__main__':
    unittest.main()
