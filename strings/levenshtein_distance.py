import unittest


def levenshtein_distance(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[m][n]


class TestLevenshteinDistance(unittest.TestCase):

    def test_same_strings(self):
        s1 = "abc"
        s2 = "abc"
        distance = levenshtein_distance(s1, s2)
        self.assertEqual(distance, 0)

    def test_one_empty_string(self):
        s1 = "abc"
        s2 = ""
        distance = levenshtein_distance(s1, s2)
        self.assertEqual(distance, 3)

    def test_different_strings(self):
        s1 = "kitten"
        s2 = "sitting"
        distance = levenshtein_distance(s1, s2)
        self.assertEqual(distance, 3)


if __name__ == '__main__':
    unittest.main()
