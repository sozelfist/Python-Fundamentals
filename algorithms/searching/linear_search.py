import unittest
from typing import List, Union


def linear_search(arr: List[int], x: int) -> Union[int, str]:
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return "Not Found"


class TestLinearSearch(unittest.TestCase):
    def test_linear_search_basic(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5, 6], 4), 3)
        self.assertEqual(linear_search([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(linear_search([-1, 2, -3], -1), 0)
        self.assertEqual(linear_search([1], 1), 0)
        self.assertEqual(linear_search([], 5), "Not Found")

    def test_linear_search_edge_cases(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5, 6], 7), "Not Found")
        self.assertEqual(linear_search([], None), "Not Found")
        self.assertEqual(linear_search([1, 2, 3, 4, 5, 6], '4'), "Not Found")


if __name__ == '__main__':
    unittest.main()
