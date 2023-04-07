import unittest


def trap(height: list[int]) -> int:
    """
    Trapping Rain Water: https://leetcode.com/problems/trapping-rain-water/.
    Helpful animation of this prompt: https://youtu.be/HmBbcDiJapY?t=51.
    Given n non-negative integers representing an elevation map where
    the width of each bar is 1, compute how much water it is able to trap
    after raining.

    VIEW ELEVATION MAP ON LEETCODE

    Example:

    Input: [0,1,0,2,1,0,1,3,2,1,2,1]

    Output: 6
    """
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    water_trapped = 0

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) - height[i]

    return water_trapped


class TestTrappingRainWater(unittest.TestCase):

    def test_trapping_rain_water_with_example_input(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected_output = 6
        self.assertEqual(trap(height), expected_output)

    def test_trapping_rain_water_with_all_zero_input(self):
        height = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected_output = 0
        self.assertEqual(trap(height), expected_output)

    def test_trapping_rain_water_with_increasing_height_input(self):
        height = [1, 2, 3, 4, 5]
        expected_output = 0
        self.assertEqual(trap(height), expected_output)

    def test_trapping_rain_water_with_decreasing_height_input(self):
        height = [5, 4, 3, 2, 1]
        expected_output = 0
        self.assertEqual(trap(height), expected_output)

    def test_trapping_rain_water_with_varying_height_input(self):
        height = [2, 1, 2]
        expected_output = 1
        self.assertEqual(trap(height), expected_output)


if __name__ == '__main__':
    unittest.main()
