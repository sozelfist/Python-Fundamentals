import unittest
from typing import List, Union


def interpolation_search(arr: List[int], x: int) -> Union[int, str]:
    low = 0
    high = len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return "Not Found"


class TestInterpolationSearch(unittest.TestCase):
    def test_element_present(self):
        arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
        x = 18
        result = interpolation_search(arr, x)
        self.assertEqual(result, 4)

    def test_element_not_present(self):
        arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
        x = 15
        result = interpolation_search(arr, x)
        self.assertEqual(result, "Not Found")

    def test_empty_list(self):
        arr = []
        x = 15
        result = interpolation_search(arr, x)
        self.assertEqual(result, "Not Found")

    def test_duplicate_elements(self):
        arr = [1, 2, 3, 4, 4, 5, 6]
        x = 4
        result = interpolation_search(arr, x)
        self.assertIn(result, [3, 4], "Incorrect result with duplicate elements")


if __name__ == '__main__':
    unittest.main()
