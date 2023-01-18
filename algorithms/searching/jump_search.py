import unittest
from typing import List, Union
import math


def jump_search(arr: List[int], x: int) -> Union[int, str]:
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return "Not Found"
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return "Not Found"
    if arr[prev] == x:
        return prev
    return "Not Found"


class TestJumpSearch(unittest.TestCase):
    def test_jump_search_basic(self):
        self.assertEqual(jump_search([1, 2, 3, 4, 5, 6], 4), 3)
        self.assertEqual(jump_search([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(jump_search([-1, 2, -3], -1), 0)
        self.assertEqual(jump_search([1], 1), 0)

    def test_jump_search_edge_cases(self):
        self.assertEqual(jump_search([], 5), "Not Found")
        self.assertEqual(jump_search([1, 2, 3, 4, 5, 6], 7), "Not Found")
        self.assertEqual(jump_search([1, 2, 3, 4, 5, 6], 8), "Not Found")
        self.assertEqual(jump_search([1, 3, 5, 7, 9, 11], 6), "Not Found")
        self.assertEqual(jump_search([1, 1, 1, 1, 1, 1], 1), 0)
        self.assertEqual(jump_search([-1, -1, -1, -1, -1], -1), 0)
        self.assertEqual(jump_search([-1, 1, -1, 1, -1], 1), 1)


if __name__ == '__main__':
    unittest.main()
