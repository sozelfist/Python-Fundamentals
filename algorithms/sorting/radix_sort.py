import unittest


def radix_sort(arr: list[int]) -> list[int]:
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


def counting_sort(arr: list[int], exp: int):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        if arr[i] >= 0:
            index = arr[i] // exp
        else:
            index = -((-arr[i]) // exp)
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        if arr[i] >= 0:
            index = arr[i] // exp
        else:
            index = -((-arr[i]) // exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]


class TestRadixSort(unittest.TestCase):
    def test_positive_elements(self):
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        expected_result = [2, 24, 45, 66, 75, 90, 170, 802]
        self.assertEqual(radix_sort(arr), expected_result)

    # def test_negative_elements(self):
    #     arr = [-170, -45, -75, -90, -802, -24, -2, -66]
    #     expected_result = [-802, -170, -90, -75, -66, -45, -24, -2]
    #     self.assertEqual(radix_sort(arr), expected_result)

    def test_duplicate_elements(self):
        arr = [170, 45, 75, 90, 802, 24, 2, 66, 170, 45, 90]
        expected_result = [2, 24, 45, 45, 66, 75, 90, 90, 170, 170, 802]
        self.assertEqual(radix_sort(arr), expected_result)

    def test_empty_list(self):
        arr = []
        expected_result = []
        self.assertEqual(radix_sort(arr), expected_result)


if __name__ == "__main__":
    unittest.main()
