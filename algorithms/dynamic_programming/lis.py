import unittest
from typing import Any


def lis(arr: Any) -> int:
    if not arr:
        return 0
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    return max(lis)


class TestLIS(unittest.TestCase):
    def test_lis(self):
        self.assertEqual(lis([10, 22, 9, 33, 21, 50, 41, 60]), 5)
        self.assertEqual(lis([1, 2, 3, 4, 5]), 5)
        self.assertEqual(lis([5, 4, 3, 2, 1]), 1)
        self.assertEqual(lis([5, 6, 7, 8, 1, 2, 3]), 4)
        self.assertEqual(lis([5]), 1)
        self.assertEqual(lis([]), 0)


if __name__ == "__main__":
    unittest.main()
