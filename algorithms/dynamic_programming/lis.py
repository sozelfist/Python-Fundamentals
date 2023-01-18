import unittest
from typing import List


def lis(arr: List[int]) -> int:
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


class TestLIS(unittest.TestCase):
    def test_lis(self):
        self.assertEqual(lis([10, 22, 9, 33, 21, 50, 41, 60]), 5)
        self.assertEqual(lis([1, 2, 3, 4, 5]), 5)
        self.assertEqual(lis([5, 4, 3, 2, 1]), 1)
        self.assertEqual(lis([5, 6, 7, 8, 1, 2, 3]), 4)
        self.assertEqual(lis([5]), 1)
        self.assertEqual(lis([]), 0)


if __name__ == '__main__':
    unittest.main()
