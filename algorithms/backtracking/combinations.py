import unittest
from typing import List


def find_combinations(items: List[int], index: int, current: List[int], result: List[List[int]]) -> List[List[int]]:
    if index == len(items):
        result.append(current[:])
        return result
    find_combinations(items, index + 1, current, result)
    current.append(items[index])
    find_combinations(items, index + 1, current, result)
    current.pop()
    return result


def combinations(items: List[int]) -> List[List[int]]:
    result = []
    find_combinations(items, 0, [], result)
    return result


class TestCombinations(unittest.TestCase):
    def test_combinations(self):
        items = [1, 2, 3]
        result = combinations(items)
        self.assertEqual(result, [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]])

        items = [4, 5]
        result = combinations(items)
        self.assertEqual(result, [[], [5], [4], [4, 5]])


if __name__ == '__main__':
    unittest.main()
