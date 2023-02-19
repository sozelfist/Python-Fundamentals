import unittest
from typing import List


def wiggle_sort(nums: List[int]) -> None:
    """
    Sorts the input list in a "wiggle" pattern.
    Raises ValueError if the input list is empty
    or contains non-integer elements.
    """
    if not nums:
        raise ValueError("Input list is empty.")

    if not all(isinstance(num, int) for num in nums):
        raise ValueError("Input list contains non-integer elements.")

    nums.sort()  # Sort the list in ascending order.
    for i in range(1, len(nums) - 1, 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]  # Swap every other element with its adjacent element.


class TestWiggleSort(unittest.TestCase):
    def test_wiggle_sort_valid_input(self):
        # Test case with a list of integers.
        nums = [3, 5, 2, 1, 6, 4]
        expected_output = [1, 3, 2, 5, 4, 6]
        wiggle_sort(nums)
        self.assertEqual(nums, expected_output)

    def test_wiggle_sort_empty_list(self):
        # Test case with an empty list.
        nums = []
        with self.assertRaises(ValueError):
            wiggle_sort(nums)

    def test_wiggle_sort_non_integer_elements(self):
        # Test case with a list containing non-integer elements.
        nums = [3, 5, 'a', 1, 6, 4]
        with self.assertRaises(ValueError):
            wiggle_sort(nums)


if __name__ == '__main__':
    unittest.main()
