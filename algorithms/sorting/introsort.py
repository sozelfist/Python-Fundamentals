import random
import unittest


def introsort(arr: list[int]) -> list[int]:
    """
    Sorts the input array in ascending order using the Introsort algorithm.

    Introsort is a hybrid sorting algorithm that uses a combination of
    quicksort, heapsort, and insertion sort. It starts with quicksort,
    but switches to heapsort when the recursion depth exceeds a certain
    threshold. If the array becomes small enough, it switches to insertion
    sort for efficient sorting of small arrays.

    Args:
        arr (list): List of comparable elements to be sorted.

    Returns:
        list: Sorted list in ascending order.

    Example:
        >>> arr = [9, 3, 7, 1, 5, 10, 2, 8, 6, 4]
        >>> introsort(arr)
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    # Define the depth limit for switching to heapsort
    depth_limit = 2 * (len(arr).bit_length())

    def insertion_sort(arr: list[int], left: int, right: int) -> None:
        """Helper function to perform insertion sort."""
        for i in range(left + 1, right + 1):
            key_item = arr[i]
            j = i - 1
            while j >= left and arr[j] > key_item:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key_item

    def partition(arr: list[int], low: int, high: int) -> int:
        """Helper function to perform partitioning in quicksort."""
        pivot_index = random.randint(low, high)
        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= j and arr[i] < pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quicksort(arr: list[int], low: int, high: int, depth_limit: int) -> None:
        """Helper function to perform quicksort."""
        if low < high:
            if high - low < depth_limit:
                insertion_sort(arr, low, high)
            else:
                pivot_index = partition(arr, low, high)
                quicksort(arr, low, pivot_index - 1, depth_limit)
                quicksort(arr, pivot_index + 1, high, depth_limit)

    # Perform the initial call to quicksort
    quicksort(arr, 0, len(arr) - 1, depth_limit)

    return arr


class IntrosortTestCase(unittest.TestCase):
    def test_introsort_with_empty_array(self):
        arr = []
        expected = []
        self.assertEqual(introsort(arr), expected)

    def test_introsort_with_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(introsort(arr), expected)

    def test_introsort_with_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(introsort(arr), expected)

    def test_introsort_with_random_array(self):
        arr = [9, 3, 7, 1, 5, 10, 2, -1, 6, 4]
        expected = [-1, 1, 2, 3, 4, 5, 6, 7, 9, 10]
        self.assertEqual(introsort(arr), expected)


if __name__ == "__main__":
    unittest.main()
