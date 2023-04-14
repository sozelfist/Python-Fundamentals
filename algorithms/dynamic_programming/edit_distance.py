import unittest


def edit_distance(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]
                )

    return dp[m][n]


class TestEditDistance(unittest.TestCase):
    def test_edit_distance(self):
        self.assertEqual(edit_distance('kitten', 'sitting'), 3)
        self.assertEqual(edit_distance('', 'sitting'), 7)
        self.assertEqual(edit_distance('kitten', ''), 6)
        self.assertEqual(edit_distance('', ''), 0)
        self.assertEqual(edit_distance('hello', 'hello'), 0)
        self.assertEqual(edit_distance('abc', 'abc'), 0)


if __name__ == '__main__':
    unittest.main()
