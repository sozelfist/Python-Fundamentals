import unittest


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    result = []

    def backtrack(start: int, path: list[int], current_sum: int):
        if current_sum == target:
            result.append(path[:])
            return
        if current_sum > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, current_sum + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result


class TestCombinationSum(unittest.TestCase):
    def test_combination_sum_with_small_target(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected_output = [[2, 2, 3], [7]]
        self.assertCountEqual(combination_sum(
            candidates, target), expected_output)

    def test_combination_sum_with_normal_target(self):
        candidates = [2, 4, 6, 8]
        target = 10
        expected_output = [[2, 2, 2, 2, 2], [2, 2, 2, 4],
                           [2, 2, 6], [2, 4, 4], [2, 8], [4, 6]]
        self.assertCountEqual(combination_sum(
            candidates, target), expected_output)

    def test_combination_sum_with_large_target(self):
        candidates = [3, 5, 7, 9]
        target = 12
        expected_output = [[3, 3, 3, 3], [3, 9], [5, 7]]
        self.assertCountEqual(combination_sum(
            candidates, target), expected_output)


if __name__ == '__main__':
    unittest.main()
