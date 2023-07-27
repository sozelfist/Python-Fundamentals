import unittest


def shortest_common_supersequence(str1: str, str2: str) -> str:
    """
    Find the shortest common supersequence of two input strings.

    A supersequence is a string that contains both input strings as subsequences,
    maintaining their relative order while possibly including additional characters.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The shortest common supersequence.

    Example:
        >>> shortest_common_supersequence("ABCBDAB", "BDCAB")
        "ABCBDCAB"
    """
    m, n = len(str1), len(str2)

    # create a 2D table to store the lengths of the shortest common supersequences.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # fill the dp table using dynamic programming.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # reconstruct the shortest common supersequence using the dp table.
    supersequence = ""
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            supersequence = str1[i - 1] + supersequence
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            supersequence = str1[i - 1] + supersequence
            i -= 1
        else:
            supersequence = str2[j - 1] + supersequence
            j -= 1

    # append the remaining characters from both strings, if any.
    while i > 0:
        supersequence = str1[i - 1] + supersequence
        i -= 1
    while j > 0:
        supersequence = str2[j - 1] + supersequence
        j -= 1

    return supersequence


class TestShortestCommonSupersequence(unittest.TestCase):

    def test_no_common_characters(self):
        string1 = "ABCDEF"
        string2 = "XYZ"
        result = shortest_common_supersequence(string1, string2)
        self.assertEqual(result, "ABCDEFXYZ")

    def test_one_subsequence_of_other(self):
        string1 = "ABC"
        string2 = "BCD"
        result = shortest_common_supersequence(string1, string2)
        self.assertEqual(result, "ABCD")

    def test_overlapping_subsequences(self):
        string1 = "AGGTAB"
        string2 = "GXTXAYB"
        result = shortest_common_supersequence(string1, string2)
        self.assertEqual(result, "AGGXTXAYB")

    def test_identical_strings(self):
        string1 = "HELLO"
        string2 = "HELLO"
        result = shortest_common_supersequence(string1, string2)
        self.assertEqual(result, "HELLO")

    def test_one_empty_string(self):
        string1 = ""
        string2 = "XYZ"
        result = shortest_common_supersequence(string1, string2)
        self.assertEqual(result, "XYZ")

    def test_both_empty_strings(self):
        string1 = ""
        string2 = ""
        result = shortest_common_supersequence(string1, string2)
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
