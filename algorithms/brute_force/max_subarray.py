import unittest


def max_subarray(arr: list[int]) -> tuple[int, int, float | int]:
    if not arr:
        return 0, 0, 0

    def max_subarray_crossing(
        arr: list[int], low: int, mid: int, high: int
    ) -> tuple[int, int, float | int]:
        left_sum = float("-inf")
        left_max = 0
        current_sum = 0
        for i in range(mid, low - 1, -1):
            current_sum += arr[i]
            if current_sum > left_sum:
                left_sum = current_sum
                left_max = i

        right_sum = float("-inf")
        right_max = 0
        current_sum = 0
        for j in range(mid + 1, high + 1):
            current_sum += arr[j]
            if current_sum > right_sum:
                right_sum = current_sum
                right_max = j

        return left_max, right_max, left_sum + right_sum

    def max_subarray_helper(
        arr: list[int], low: int, high: int
    ) -> tuple[int, int, float | int]:
        if low == high:
            return low, high, arr[low]
        mid = (low + high) // 2
        left_low, left_high, left_sum = max_subarray_helper(arr, low, mid)
        right_low, right_high, right_sum = max_subarray_helper(
            arr, mid + 1, high)
        cross_low, cross_high, cross_sum = max_subarray_crossing(
            arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

    return max_subarray_helper(arr, 0, len(arr) - 1)


class MaxSubarrayTests(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(max_subarray([]), (0, 0, 0))

    def test_single_element_array(self):
        self.assertEqual(max_subarray([5]), (0, 0, 5))

    def test_array_with_all_positive_elements(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(max_subarray(arr), (0, 4, 15))

    def test_array_with_mixed_positive_and_negative_elements(self):
        arr = [1, -2, 3, -4, 5]
        self.assertEqual(max_subarray(arr), (4, 4, 5))

    def test_array_with_all_negative_elements(self):
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(max_subarray(arr), (0, 0, -1))


if __name__ == "__main__":
    unittest.main()
