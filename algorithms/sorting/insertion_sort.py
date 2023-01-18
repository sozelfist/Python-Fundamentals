import unittest
from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(insertion_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(insertion_sort([-1, 2, -3]), [-3, -1, 2])
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort([]), [])

    def test_insertion_sort_performance(self):
        import random
        for i in range(0, 10000):
            test_arr = random.sample(range(-10000, 10000), 1000)
            self.assertEqual(insertion_sort(test_arr), sorted(test_arr))


if __name__ == '__main__':
    unittest.main()
