import unittest


def find_subsets(nums: list[int]) -> list:
    n = len(nums)
    subsets = []

    for i in range(2**n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(nums[j])
        subsets.append(subset)

    return subsets


class TestFindSubsets(unittest.TestCase):
    def test_find_subsets_empty_set(self):
        nums = []
        expected = [[]]
        result = find_subsets(nums)
        self.assertEqual(result, expected)

    def test_find_subsets_single_element_set(self):
        nums = [1]
        expected = [[], [1]]
        result = find_subsets(nums)
        self.assertEqual(result, expected)

    def test_find_subsets_multiple_element_set(self):
        nums = [1, 2, 3]
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        result = find_subsets(nums)
        self.assertEqual(result, expected)

    def test_find_subsets_duplicate_elements(self):
        nums = [1, 2, 2]
        expected = [[], [1], [2], [1, 2], [2], [1, 2], [2, 2], [1, 2, 2]]
        result = find_subsets(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
