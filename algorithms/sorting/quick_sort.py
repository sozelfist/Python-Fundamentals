import unittest
import random
from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    def partition(arr: List[int], start: int, end: int) -> int:
        pivot_index = random.randint(start, end)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
        i = start - 1
        for j in range(start, end):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        return i + 1

    def sort(arr: List[int], start: int, end: int):
        if start < end:
            pivot_index = partition(arr, start, end)
            sort(arr, start, pivot_index - 1)
            sort(arr, pivot_index + 1, end)
    sort(arr, 0, len(arr) - 1)
    return arr


class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        arr = [3, 2, 1, 5, 4]
        self.assertEqual(quick_sort(arr), [1, 2, 3, 4, 5])

        arr = [1, 2, 3, 4, 5]
        self.assertEqual(quick_sort(arr), [1, 2, 3, 4, 5])

        arr = [5, 4, 3, 2, 1]
        self.assertEqual(quick_sort(arr), [1, 2, 3, 4, 5])

        arr = [-3, -2, -1, -5, -4]
        self.assertEqual(quick_sort(arr), [-5, -4, -3, -2, -1])

        arr = []
        self.assertEqual(quick_sort(arr), [])

        arr = [4, 2, 5, 2, 1, 3, 5, 4, 3]
        self.assertEqual(quick_sort(arr), [1, 2, 2, 3, 3, 4, 4, 5, 5])


if __name__ == '__main__':
    unittest.main()
