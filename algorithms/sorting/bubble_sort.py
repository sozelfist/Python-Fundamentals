import unittest
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        # check if the list is already sorted
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(bubble_sort([-1, 2, -3]), [-3, -1, 2])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([]), [])

    def test_bubble_sort_performance(self):
        import random
        for i in range(0, 10000):
            test_list = random.sample(range(-10000, 10000), 1000)
            self.assertEqual(bubble_sort(test_list), sorted(test_list))


if __name__ == '__main__':
    unittest.main()
