import unittest


def binary_search(arr: list[int], x: int) -> int | str:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid - 1] != x:
                return mid
            else:
                high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return "Not Found"


class TestBinarySearch(unittest.TestCase):
    def test_found_element(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        result = binary_search(arr, x)
        self.assertEqual(result, 2)

    def test_not_found_element(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        result = binary_search(arr, x)
        self.assertEqual(result, "Not Found")

    def test_empty_array(self):
        arr = []
        x = 1
        result = binary_search(arr, x)
        self.assertEqual(result, "Not Found")

    def test_duplicate_element(self):
        arr = [1, 2, 2, 3, 4, 5]
        x = 2
        result = binary_search(arr, x)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
