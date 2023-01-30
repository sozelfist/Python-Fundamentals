import unittest
from typing import List


def shell_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


class TestShellSort(unittest.TestCase):
    def test_shell_sort_basic(self):
        self.assertEqual(shell_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(shell_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(shell_sort([-1, 2, -3]), [-3, -1, 2])
        self.assertEqual(shell_sort([1]), [1])
        self.assertEqual(shell_sort([]), [])

    def test_shell_sort_performance(self):
        import random
        for i in range(0, 10):
            arr = random.sample(range(-10000, 10000), 10000)
            self.assertEqual(shell_sort(arr), sorted(arr))


if __name__ == '__main__':
    unittest.main()
