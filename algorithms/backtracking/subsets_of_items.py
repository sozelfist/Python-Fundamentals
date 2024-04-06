import unittest


def find_subsets(items: list[int]) -> list[list[int]]:
    subsets = []
    n = len(items)
    for i in range(2**n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(items[j])
        subsets.append(subset)
    return subsets


class TestFindSubsets(unittest.TestCase):
    def test_find_subsets(self):
        self.assertEqual(
            find_subsets([1, 2, 3]),
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
        )
        self.assertEqual(find_subsets([1, 2]), [[], [1], [2], [1, 2]])
        self.assertEqual(find_subsets([1]), [[], [1]])
        self.assertEqual(find_subsets([]), [[]])


if __name__ == "__main__":
    unittest.main()
