import unittest


def next_greater_elements(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n
    stack = []

    # Iterate through the array twice to handle circular case
    for i in range(n * 2):
        while stack and nums[stack[-1]] < nums[i % n]:
            index = stack.pop()
            result[index] = nums[i % n]
        stack.append(i % n)

    return result


class TestNextGreaterElements(unittest.TestCase):

    def test_next_greater_elements(self):
        nums = [-10, -5, 0, 5, 5.1, 11, 13, 21, 3, 4, -21, -10, -5, -1, 0]
        result = next_greater_elements(nums)
        expected = [-5, 0, 5, 5.1, 11, 13, 21, -1, 4, 5, -10, -5, -1, 0, 5]
        self.assertEqual(result, expected)

    def test_next_greater_elements_empty(self):
        nums = []
        result = next_greater_elements(nums)
        expected = []
        self.assertEqual(result, expected)

    def test_next_greater_elements_single_element(self):
        nums = [5]
        result = next_greater_elements(nums)
        expected = [-1]
        self.assertEqual(result, expected)

    def test_next_greater_elements_all_equal(self):
        nums = [5] * 5
        result = next_greater_elements(nums)
        expected = [-1] * 5
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
