import unittest


def permute(items: list[int]) -> list[list[int]]:
    if len(items) == 0:
        return [[]]
    result = []
    for i in range(len(items)):
        remaining_items = items[:i] + items[i + 1:]
        for permutation in permute(remaining_items):
            result.append([items[i]] + permutation)
    return result


class TestPermute(unittest.TestCase):
    def test_permute(self):
        items = [1, 2, 3]
        result = permute(items)
        self.assertEqual(result, [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

        items = [4, 5]
        result = permute(items)
        self.assertEqual(result, [[4, 5], [5, 4]])


if __name__ == '__main__':
    unittest.main()
