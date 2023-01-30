import unittest
from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(selection_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(selection_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(selection_sort([-1, 2, -3]), [-3, -1, 2])
        self.assertEqual(selection_sort([1]), [1])
        self.assertEqual(selection_sort([]), [])


if __name__ == '__main__':
    unittest.main()
