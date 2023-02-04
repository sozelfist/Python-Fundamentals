import unittest
from typing import List


def combinations(items: List[int]) -> List[List[int]]:
    def find_combinations(index: int, current: List[int], result: List[List[int]]):
        if index == len(items):
            result.append(current[:])
            return
        find_combinations(index + 1, current, result)
        current.append(items[index])
        find_combinations(index + 1, current, result)
        current.pop()

    result = []
    find_combinations(0, [], result)
    return result


class TestCombinations(unittest.TestCase):
    def test_combinations(self):
        items = [1, 2, 3]
        result = combinations(items)
        self.assertEqual(result, [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]])

        items = [4, 5]
        result = combinations(items)
        self.assertEqual(result, [[], [5], [4], [4, 5]])

        items = []
        result = combinations(items)
        self.assertEqual(result, [[]])


if __name__ == '__main__':
    unittest.main()
