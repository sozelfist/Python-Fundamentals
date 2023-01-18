import unittest
from typing import List


def ternary_search(arr: List[int], x: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        left_third = left + (right - left) // 3
        right_third = right - (right - left) // 3

        if arr[left_third] == x:
            return left_third
        if arr[right_third] == x:
            return right_third

        if x < arr[left_third]:
            right = left_third - 1
        elif x > arr[right_third]:
            left = right_third + 1
        else:
            left = left_third + 1
            right = right_third - 1

    return -1


class TestTernarySearch(unittest.TestCase):
    def test_ternary_search_basic(self):
        self.assertEqual(ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 4)
        self.assertEqual(ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8), 7)

    def test_ternary_search_not_found(self):
        self.assertEqual(ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)
        self.assertEqual(ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), -1)

    def test_ternary_search_edge_cases(self):
        self.assertEqual(ternary_search([], 11), -1)
        self.assertEqual(ternary_search([1], 1), 0)


if __name__ == '__main__':
    unittest.main()
