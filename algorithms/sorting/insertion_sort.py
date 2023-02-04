import unittest
from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(insertion_sort([5, 2, 9, 1, 5]), [1, 2, 5, 5, 9])
        self.assertEqual(insertion_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort([3, 2, 1, 2, 3]), [1, 2, 2, 3, 3])
        self.assertEqual(insertion_sort([-5, 2, 9, 1, -2]), [-5, -2, 1, 2, 9])
        self.assertEqual(insertion_sort([]), [])


if __name__ == '__main__':
    unittest.main()
