import unittest


def partition(nums: list[int], low: int, high: int) -> int:
    """
    Helper function to partition the list around a pivot and return its final position.
    """
    pivot = nums[high]  # Choosing the last element as the pivot
    i = low

    for j in range(low, high):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = nums[high], nums[i]
    return i


def quick_select(nums: list[int], k: int) -> int:
    """
    Find the k-th smallest element in the list using the QuickSelect algorithm.
    Note: the case of array of duplicated elements is unsolved
    """

    def select_helper(nums: list[int], low: int, high: int, k: int) -> int:
        # Base case: if the list contains only one element
        if low == high:
            return nums[low]

        # Partition the list and get the pivot's final position
        pivot_index = partition(nums, low, high)

        # Check if the pivot is the k-th smallest element
        if pivot_index == k - 1:
            return nums[pivot_index]
        # Recurse on the left partition
        elif pivot_index > k - 1:
            return select_helper(nums, low, pivot_index - 1, k)
        # Recurse on the right partition
        else:
            return select_helper(nums, pivot_index + 1, high, k)

    # Make a copy of the input list to avoid modifying the original list
    nums_copy = nums.copy()
    n = len(nums_copy)

    # Ensure that k is within the valid range
    if k < 1 or k > n:
        raise ValueError("Invalid value of k")

    # Call the helper function to find the k-th smallest element
    return select_helper(nums_copy, 0, n - 1, k)


class QuickSelectTestCase(unittest.TestCase):
    def test_quick_select(self):
        nums = [4, 2, 9, 6, 1, 7]
        k = 3
        result = quick_select(nums, k)
        self.assertEqual(result, 4)

    # def test_quick_select_with_duplicate_values(self):
    #     nums = [4, 2, 9, 6, 1, 7, 4, 4]
    #     k = 5
    #     result = quick_select(nums, k)
    #     self.assertEqual(result, 6)

    def test_quick_select_with_single_element(self):
        nums = [5]
        k = 1
        result = quick_select(nums, k)
        self.assertEqual(result, 5)

    def test_quick_select_with_invalid_k(self):
        nums = [4, 2, 9, 6, 1, 7]
        k = 0
        with self.assertRaises(ValueError):
            quick_select(nums, k)

        k = 10
        with self.assertRaises(ValueError):
            quick_select(nums, k)


if __name__ == "__main__":
    unittest.main()
