import unittest


def lcs(
    X: list[int], Y: list[int], m: int, n: int,
    memo: dict[tuple[int, int], int]
) -> int:
    if m == 0 or n == 0:
        return 0
    if (m, n) in memo:
        return memo[(m, n)]
    if X[m - 1] == Y[n - 1]:
        memo[(m, n)] = 1 + lcs(X, Y, m - 1, n - 1, memo)
    else:
        memo[(m, n)] = max(
            lcs(X, Y, m, n - 1, memo),
            lcs(X, Y, m - 1, n, memo)
        )
    return memo[(m, n)]


def lcs_length(X: list[int], Y: list[int]) -> int:
    m = len(X)
    n = len(Y)
    memo = {}
    return lcs(X, Y, m, n, memo)


class TestLCS(unittest.TestCase):
    def test_lcs_length(self):
        self.assertEqual(lcs_length([1, 2, 3, 4, 1], [3, 4, 1, 2, 1, 3]), 3)
        self.assertEqual(lcs_length([1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(lcs_length([1, 2, 3], [4, 5, 6]), 0)
        self.assertEqual(lcs_length([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 5)
        self.assertEqual(lcs_length([1, 2, 3, 4, 5], []), 0)
        self.assertEqual(lcs_length([], [1, 2, 3, 4, 5]), 0)
        # Edge case when both lists are empty
        self.assertEqual(lcs_length([], []), 0)
        # Edge case when one of the lists is shorter than the other
        self.assertEqual(lcs_length([1, 2, 3, 4, 5], [2, 3]), 2)
        # Edge case when one of the lists is longer than the other
        self.assertEqual(lcs_length([1, 2, 3, 4, 5], [
                         1, 2, 3, 4, 5, 6, 7, 8]), 5)


if __name__ == '__main__':
    unittest.main()
