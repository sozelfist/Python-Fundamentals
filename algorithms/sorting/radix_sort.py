import unittest
from typing import List


def radix_sort(arr: List[int]) -> List[int]:
    max_val = max(arr)
    exp = 1
    while max_val / exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


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


class TestRadixSort(unittest.TestCase):
    def test_radix_sort_basic(self):
        self.assertEqual(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]), [2, 24, 45, 66, 75, 90, 170, 802])
        self.assertEqual(radix_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(radix_sort([-1, 2, -3]), [-3, -1, 2])
        self.assertEqual(radix_sort([1]), [1])
        self.assertEqual(radix_sort([]), [])


if __name__ == '__main__':
    unittest.main()
