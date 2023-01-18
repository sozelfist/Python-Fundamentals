from typing import List
import unittest


def counting_sort(arr: List[int], exp: int):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]


class TestCountingSort(unittest.TestCase):
    def test_counting_sort_basic(self):
        self.assertEqual(counting_sort([2, 5, 9, 8, 2, 8, 7, 10, 4, 3], 1), [2, 2, 3, 4, 5, 7, 8, 8, 9, 10])
        self.assertEqual(counting_sort([120, 400, 130, 100, 50], 100), [50, 100, 120, 130, 400])
        self.assertEqual(counting_sort([1, 2, 3], 1), [1, 2, 3])
        self.assertEqual(counting_sort([-1, 2, -3], 1), [-3, -1, 2])
        self.assertEqual(counting_sort([1], 1), [1])
        self.assertEqual(counting_sort([], 1), [])

    def test_counting_sort_performance(self):
        import random
        for i in range(0, 10):
            arr = random.sample(range(-10000, 10000), 10000)
            self.assertEqual(counting_sort(arr, 1), sorted(arr))

    def test_counting_sort_large_input(self):
        import random
        arr = random.sample(range(-1000000, 1000000), 100000)
        self.assertEqual(counting_sort(arr, 1), sorted(arr))


if __name__ == '__main__':
    unittest.main()
