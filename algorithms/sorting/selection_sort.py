import unittest


def selection_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


class TestSelectionSort(unittest.TestCase):
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = selection_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorted_arr = selection_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_random_unsorted(self):
        arr = [3, 5, 2, 1, 4]
        sorted_arr = selection_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_duplicates(self):
        arr = [3, 5, 3, 1, 4]
        sorted_arr = selection_sort(arr)
        self.assertEqual(sorted_arr, [1, 3, 3, 4, 5])

    def test_negative_elements(self):
        arr = [3, -5, 2, -1, 4]
        sorted_arr = selection_sort(arr)
        self.assertEqual(sorted_arr, [-5, -1, 2, 3, 4])

    def test_empty_list(self):
        arr = []
        sorted_arr = selection_sort(arr)
        self.assertEqual(sorted_arr, [])


if __name__ == "__main__":
    unittest.main()
