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
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = shell_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorted_arr = shell_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_random_unsorted(self):
        arr = [3, 5, 2, 1, 4]
        sorted_arr = shell_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_duplicates(self):
        arr = [3, 5, 3, 1, 4]
        sorted_arr = shell_sort(arr)
        self.assertEqual(sorted_arr, [1, 3, 3, 4, 5])

    def test_negative_elements(self):
        arr = [3, -5, 2, -1, 4]
        sorted_arr = shell_sort(arr)
        self.assertEqual(sorted_arr, [-5, -1, 2, 3, 4])

    def test_empty_list(self):
        arr = []
        sorted_arr = shell_sort(arr)
        self.assertEqual(sorted_arr, [])


if __name__ == '__main__':
    unittest.main()
