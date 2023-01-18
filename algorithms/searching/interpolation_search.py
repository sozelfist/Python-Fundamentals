import unittest
from typing import List, Union


def interpolation_search(arr: List[int], x: int) -> Union[int, str]:
    low = 0
    high = len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return "Not Found"


class TestInterpolationSearch(unittest.TestCase):
    def test_interpolation_search_basic(self):
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5, 6], 4), 3)
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(interpolation_search([-1, 2, -3], -1), 0)
        self.assertEqual(interpolation_search([1], 1), 0)

    def test_interpolation_search_edge_cases(self):
        self.assertEqual(interpolation_search([], 5), "Not Found")
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5, 6], 7), "Not Found")
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5, 6], 8), "Not Found")
        self.assertEqual(interpolation_search([1, 3, 5, 7, 9, 11], 6), "Not Found")
        self.assertEqual(interpolation_search([1, 1, 1, 1, 1, 1], 1), 0)
        self.assertEqual(interpolation_search([-1, -1, -1, -1, -1], -1), 0)
        self.assertEqual(interpolation_search([-1, 1, -1, 1, -1], 1), 1)


if __name__ == '__main__':
    unittest.main()
