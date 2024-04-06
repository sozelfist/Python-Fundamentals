import unittest
from heapq import heappop, heappush


def partition(nums: list[int], low: int, high: int) -> int:
    """
    Helper function to partition the list around a pivot and return its final position.
    """
    pivot = nums[high]  # Choosing the last element as the pivot
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def insertion_sort(nums: list[int], low: int, high: int) -> None:
    """
    Sort the sublist within the given range using Insertion Sort.
    """
    for i in range(low + 1, high + 1):
        key = nums[i]
        j = i - 1
        while j >= low and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key


def introselect(nums: list[int], k: int) -> int:
    """
    Find the k-th smallest element in the list using the IntroSelect algorithm.
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

    # Perform QuickSelect
    return select_helper(nums_copy, 0, n - 1, k)


def introselect_sort(nums: list[int]) -> list[int]:
    """
    Sort the list using IntroSelect algorithm.
    """

    def introselect_helper(nums: list[int], low: int, high: int) -> None:
        # Base case: if the sublist contains at most 16 elements, use Insertion Sort
        if high - low <= 16:
            insertion_sort(nums, low, high)
        # Base case: if recursion depth exceeds a limit, switch to HeapSort
        elif depth_limit == 0:
            nums[low : high + 1] = heapsort(nums[low : high + 1])
        else:
            # Partition the list and get the pivot's final position
            pivot_index = partition(nums, low, high)
            # Recurse on the left partition
            introselect_helper(nums, low, pivot_index - 1)
            # Recurse on the right partition
            introselect_helper(nums, pivot_index + 1, high)

    # Make a copy of the input list to avoid modifying the original list
    nums_copy = nums.copy()

    # Set the initial depth limit based on the size of the list
    depth_limit = 2 * (len(nums_copy)).bit_length()

    # Perform IntroSelect
    introselect_helper(nums_copy, 0, len(nums_copy) - 1)
    return nums_copy


def heapsort(nums: list[int]) -> list[int]:
    """
    Sort the list using HeapSort algorithm.
    """
    heap = []
    for num in nums:
        heappush(heap, num)
    sorted_nums = []
    while heap:
        sorted_nums.append(heappop(heap))
    return sorted_nums


class IntroSelectTestCase(unittest.TestCase):
    def test_introselect(self):
        nums = [4, 2, 9, 6, 1, 7]
        k = 3
        result = introselect(nums, k)
        self.assertEqual(result, 4)

    def test_introselect_with_duplicate_values(self):
        nums = [4, 2, 9, 6, 1, 7, 4, 4]
        k = 5
        result = introselect(nums, k)
        self.assertEqual(result, 4)

    def test_introselect_with_single_element(self):
        nums = [5]
        k = 1
        result = introselect(nums, k)
        self.assertEqual(result, 5)

    def test_introselect_with_invalid_k(self):
        nums = [4, 2, 9, 6, 1, 7]
        k = 0
        with self.assertRaises(ValueError):
            introselect(nums, k)

        k = 10
        with self.assertRaises(ValueError):
            introselect(nums, k)

    def test_introselect_sort(self):
        nums = [4, 2, 9, 6, 1, 7]
        expected = [1, 2, 4, 6, 7, 9]
        result = introselect_sort(nums)
        self.assertEqual(result, expected)

    def test_introselect_sort_with_duplicate_values(self):
        nums = [4, 2, 9, 6, 1, 7, 4, 4]
        expected = [1, 2, 4, 4, 4, 6, 7, 9]
        result = introselect_sort(nums)
        self.assertEqual(result, expected)

    def test_introselect_sort_with_single_element(self):
        nums = [5]
        expected = [5]
        result = introselect_sort(nums)
        self.assertEqual(result, expected)

    def test_introselect_sort_with_empty_list(self):
        nums = []
        expected = []
        result = introselect_sort(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
