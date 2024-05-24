import random
import unittest
from typing import TypeVar

T = TypeVar("T")


def insertion_sort(arr: list[T], left: int, right: int) -> None:
    """
    Sorts a portion of the array using insertion sort.
    Parameters:
    arr (list[T]): The list to sort.
    left (int): The starting index of the portion to sort.
    right (int): The ending index of the portion to sort.
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def partition(arr: list[T], low: int, high: int) -> int:
    """
    Partitions the array around a pivot.
    Parameters:
    arr (list[T]): The list to partition.
    low (int): The starting index of the portion to partition.
    high (int): The ending index of the portion to partition.
    Returns:
    int: The index of the pivot.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heapify(arr: list[T], n: int, i: int, low: int) -> None:
    """
    Converts a portion of the array into a heap.
    Parameters:
    arr (list[T]): The list to heapify.
    n (int): The size of the heap.
    i (int): The index of the current node.
    low (int): The starting index of the portion to heapify.
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[low + l] > arr[low + largest]:
        largest = l
    if r < n and arr[low + r] > arr[low + largest]:
        largest = r
    if largest != i:
        arr[low + i], arr[low + largest] = arr[low + largest], arr[low + i]
        heapify(arr, n, largest, low)


def heap_sort(arr: list[T], low: int, high: int) -> None:
    """
    Sorts a portion of the array using heap sort.
    Parameters:
    arr (list[T]): The list to sort.
    low (int): The starting index of the portion to sort.
    high (int): The ending index of the portion to sort.
    """
    n = high - low + 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, low)
    for i in range(n - 1, 0, -1):
        arr[low], arr[low + i] = arr[low + i], arr[low]
        heapify(arr, i, 0, low)


def pdqsort_recursive(arr: list[T], low: int, high: int, depth_limit: int) -> None:
    """
    Recursively sorts the array using PDQSort algorithm.
    Parameters:
    arr (list[T]): The list to sort.
    low (int): The starting index of the portion to sort.
    high (int): The ending index of the portion to sort.
    depth_limit (int): The maximum recursion depth.
    """
    while low < high:
        # Use insertion sort for small partitions
        if high - low <= 16:
            insertion_sort(arr, low, high)
            return

        if depth_limit == 0:
            # Switch to heapsort if depth limit is reached
            heap_sort(arr, low, high)
            return

        pivot_index = partition(arr, low, high)
        pdqsort_recursive(arr, low, pivot_index - 1, depth_limit - 1)
        # Tail recursion elimination
        low = pivot_index + 1


def pdqsort(arr: list[T]) -> None:
    """
    Sorts the entire array using the Pattern-Defeating Quicksort (PDQSort) algorithm.
    PDQSort is an optimized version of Quicksort that includes enhancements to deal with
    various patterns in the input data, such as already sorted or nearly sorted sequences.
    It dynamically switches between different sorting strategies based on the characteristics
    of the data and recursion depth to achieve better performance.
    PDQSort employs the following techniques:
    - Insertion Sort for small arrays to reduce overhead.
    - Partitioning around a pivot to divide the array into subarrays.
    - Heap Sort as a fallback when the recursion depth limit is reached, preventing worst-case
      scenarios that could degrade performance to O(n^2).
    - Tail call optimization to avoid excessive recursive calls and stack overflow.
    Parameters:
    arr (list[T]): The list of elements to sort. The list is sorted in place.
    """
    max_depth = (len(arr).bit_length() - 1) * 2
    pdqsort_recursive(arr, 0, len(arr) - 1, max_depth)


class TestPDQSort(unittest.TestCase):
    def test_empty_list(self):
        arr = []
        pdqsort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        pdqsort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        pdqsort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_list(self):
        arr = [5, 2, 8, 3, 1, 9, 4, 6, 7]
        pdqsort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_duplicates(self):
        arr = [3, 2, 1, 3, 1, 2]
        pdqsort(arr)
        self.assertEqual(arr, [1, 1, 2, 2, 3, 3])

    def test_large_random_list(self):
        arr = random.sample(range(1000000), 1000)
        sorted_arr = sorted(arr)
        pdqsort(arr)
        self.assertEqual(arr, sorted_arr)

    def test_string_list(self):
        arr = ["banana", "apple", "orange", "grape", "kiwi"]
        pdqsort(arr)
        self.assertEqual(arr, ["apple", "banana", "grape", "kiwi", "orange"])

    def test_empty_string_list(self):
        arr = ["", "apple", "banana", "", "orange", "", "grape", "kiwi", ""]
        pdqsort(arr)
        self.assertEqual(
            arr, ["", "", "", "", "apple", "banana", "grape", "kiwi", "orange"]
        )


if __name__ == "__main__":
    unittest.main()
