import unittest
from typing import List


def exponential_search(arr: List[int], x: int) -> int:
    if arr[0] == x:
        return 0
    i = 1
    n = len(arr)
    while i < n and arr[i] <= x:
        i = i * 2
    return binary_search(arr, i // 2, min(i, n), x)


def binary_search(arr: List[int], left: int, right: int, x: int) -> int:
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


class TestExponentialSearch(unittest.TestCase):
    def test_exponential_search_basic(self):
        self.assertEqual(exponential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 4)
        self.assertEqual(exponential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8), 7)

    def test_exponential_search_not_found(self):
        self.assertEqual(exponential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)
        self.assertEqual(exponential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), -1)

    def test_exponential_search_edge_cases(self):
        self.assertEqual(exponential_search([], 11), -1)
        self.assertEqual(exponential_search([1], 1), 0)


if __name__ == '__main__':
    unittest.main()
