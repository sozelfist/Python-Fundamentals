import unittest


def find_subsets(nums: list[int]) -> list[list[int]]:
    subsets = []

    def dfs(start, path):
        subsets.append(path)
        for i in range(start, len(nums)):
            dfs(i + 1, path + [nums[i]])
    dfs(0, [])
    return subsets


class TestFindSubsets(unittest.TestCase):
    def test_find_subsets(self):
        nums = [1, 2, 3]
        expected_output = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        self.assertEqual(find_subsets(nums), expected_output)

    def test_find_subsets_with_duplicates(self):
        nums = [1, 2, 2]
        expected_output = [[], [1], [1, 2], [1, 2, 2], [1, 2], [2], [2, 2], [2]]
        self.assertEqual(find_subsets(nums), expected_output)

    def test_find_subsets_with_empty_input(self):
        nums = []
        expected_output = [[]]
        self.assertEqual(find_subsets(nums), expected_output)


if __name__ == '__main__':
    unittest.main()
