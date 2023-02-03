import unittest
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        # check if the list is already sorted
        for j in range(n - 1, i, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


class TestBubbleSort(unittest.TestCase):
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = bubble_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorted_arr = bubble_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_random_unsorted(self):
        arr = [3, 5, 2, 1, 4]
        sorted_arr = bubble_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_duplicates(self):
        arr = [3, 5, 3, 1, 4]
        sorted_arr = bubble_sort(arr)
        self.assertEqual(sorted_arr, [1, 3, 3, 4, 5])

    def test_negative_elements(self):
        arr = [3, -5, 2, -1, 4]
        sorted_arr = bubble_sort(arr)
        self.assertEqual(sorted_arr, [-5, -1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
