import unittest
from typing import List


def exponential_search(arr: List[int], x: int) -> int:
    if arr[0] == x:
        return 0
    i = 1
    n = len(arr)
    while i < n and i < len(arr) and arr[i] <= x:
        i = i * 2
    return binary_search(arr, i // 2, min(i, n - 1), x)


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
    def test_valid_input(self):
        arr = [2, 3, 4, 10, 40]
        x = 10
        result = exponential_search(arr, x)
        self.assertEqual(result, 3)

    def test_element_not_present(self):
        arr = [2, 3, 4, 10, 40]
        x = 50
        result = exponential_search(arr, x)
        self.assertEqual(result, -1)

    def test_small_array(self):
        arr = [2, 3]
        x = 2
        result = exponential_search(arr, x)
        self.assertEqual(result, 0)

    def test_array_of_length_one(self):
        arr = [2]
        x = 2
        result = exponential_search(arr, x)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
