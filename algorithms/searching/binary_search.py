import unittest
from typing import List, Union


def binary_search(arr: List[int], x: int) -> Union[int, str]:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return "Not Found"


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_basic(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 4), 3)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(binary_search([-1, 2, -3], -1), 0)
        self.assertEqual(binary_search([1], 1), 0)

    def test_binary_search_edge_cases(self):
        self.assertEqual(binary_search([], 5), "Not Found")
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 7), "Not Found")
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 8), "Not Found")
        self.assertEqual(binary_search([1, 3, 5, 7, 9, 11], 6), "Not Found")
        self.assertEqual(binary_search([1, 1, 1, 1, 1, 1], 1), 0)
        self.assertEqual(binary_search([-1, -1, -1, -1, -1], -1), 0)
        self.assertEqual(binary_search([-1, 1, -1, 1, -1], 1), 1)


if __name__ == '__main__':
    unittest.main()
