import unittest


def prefix_sum(
    nums: list[int], start: int | None = None, end: int | None = None
) -> list[int]:
    """
    Given an array of integers, return a new array where each element
    is the sum of all elements up to and including the current index.

    Args:
        nums: List of integers
        start: The starting index of the prefix sum array. Default is 0.
        end: The ending index of the prefix sum array. Default is None, which
             means it includes all elements up to the last index.

    Returns:
        A list of prefix sums starting from the start
        index up to the end index.
    """
    # Initialize default start and end indices
    if start is None:
        start = 0
    if end is None:
        end = len(nums) - 1
    # Check for invalid indices
    if start < 0 or start >= len(nums):
        raise ValueError("Invalid start index")
    if end > len(nums):
        raise ValueError("Invalid end index")

    prefix = [0] * (end - start + 1)
    prefix[0] = nums[start]

    for i in range(1, end - start + 1):
        prefix[i] = prefix[i - 1] + nums[start + i]

    return prefix


class TestPrefixSum(unittest.TestCase):
    def test_prefix_sum(self):
        arr = [1, 2, 3, 4, 5]
        result = prefix_sum(arr)
        expected = [1, 3, 6, 10, 15]
        self.assertEqual(result, expected)

    def test_prefix_sum_with_start_and_end(self):
        arr = [1, 2, 3, 4, 5]
        start, end = 1, 4
        result = prefix_sum(arr, start=start, end=end)
        expected = [2, 5, 9, 14]
        self.assertEqual(result, expected)

    def test_prefix_sum_with_invalid_start_and_end(self):
        arr = [1, 2, 3, 4, 5]
        start, end = -1, 6
        with self.assertRaises(ValueError):
            prefix_sum(arr, start=start, end=end)


if __name__ == "__main__":
    unittest.main()
