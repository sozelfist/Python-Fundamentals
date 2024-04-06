import unittest


def knuth_optimization(nums: list[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [[0] * n for _ in range(n)]

    for _ in range(n):
        for i in range(n - _):
            j = i + _
            if _ == 0:
                dp[i][j] = nums[i]
            elif _ == 1:
                dp[i][j] = max(nums[i], nums[j])
            else:
                dp[i][j] = max(
                    nums[i] + min(dp[i + 2][j], dp[i + 1][j - 1]),
                    nums[j] + min(dp[i + 1][j - 1], dp[i][j - 2]),
                )

    return dp[0][n - 1]


class TestKnuthOptimization(unittest.TestCase):
    def test_knuth_optimization_case1(self):
        nums1 = [3, 1, 5, 6, 2, 9]
        self.assertEqual(knuth_optimization(nums1), 16)

    def test_knuth_optimization_case2(self):
        nums2 = [4, 2, 10, 5, 6, 3]
        self.assertEqual(knuth_optimization(nums2), 20)

    def test_knuth_optimization_case3(self):
        nums3 = [1, 2, 3, 4, 5, 6]
        self.assertEqual(knuth_optimization(nums3), 12)

    def test_knuth_optimization_case4(self):
        nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(knuth_optimization(nums4), 25)

    def test_knuth_optimization_case5(self):
        nums5 = [9, 2, 7, 4, 8, 6]
        self.assertEqual(knuth_optimization(nums5), 24)

    def test_knuth_optimization_empty_list(self):
        nums6 = []
        self.assertEqual(knuth_optimization(nums6), 0)

    def test_knuth_optimization_non_int_list(self):
        nums7 = [1, 2, "3", 4, "five"]
        with self.assertRaises(TypeError):
            knuth_optimization(nums7)


if __name__ == "__main__":
    unittest.main()
