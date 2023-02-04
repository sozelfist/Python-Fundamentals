import unittest
from typing import List, Union
import math


def jump_search(arr: List[int], x: int) -> Union[int, str]:
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while True:
        if arr[min(step, n) - 1] >= x:
            break
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return "Not Found"
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i
    return "Not Found"


class TestJumpSearch(unittest.TestCase):
    def test_jump_search_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 5
        result = jump_search(arr, x)
        self.assertEqual(result, 4)

    def test_jump_search_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 11
        result = jump_search(arr, x)
        self.assertEqual(result, "Not Found")

    def test_jump_search_duplicate(self):
        arr = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
        x = 5
        result = jump_search(arr, x)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
