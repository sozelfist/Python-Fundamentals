import unittest
from typing import List, Union


def linear_search(arr: List[int], x: int) -> Union[int, str]:
    for i, value in enumerate(arr):
        if value == x:
            return i
    return "Not Found"


class TestLinearSearch(unittest.TestCase):
    def test_linear_search_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 5
        result = linear_search(arr, x)
        self.assertEqual(result, 4)

    def test_linear_search_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 11
        result = linear_search(arr, x)
        self.assertEqual(result, "Not Found")

    def test_linear_search_empty_list(self):
        arr = []
        x = 11
        result = linear_search(arr, x)
        self.assertEqual(result, "Not Found")

    def test_duplicate_elements(self):
        arr = [1, 2, 3, 4, 4, 5, 6]
        x = 4
        result = linear_search(arr, x)
        self.assertIn(result, [3, 4], "Incorrect result with duplicate elements")


if __name__ == '__main__':
    unittest.main()
