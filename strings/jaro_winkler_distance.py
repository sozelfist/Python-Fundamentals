import unittest


def jaro_winkler_distance(s1: str, s2: str, p: float = 0.1) -> float:
    """
    Calculates the Jaro-Winkler distance between two strings.

    Args:
        s1: The first string.
        s2: The second string.
        p: The scaling factor for the prefix length. Defaults to 0.1.

    Returns:
        The Jaro-Winkler distance between the two strings.
    """
    # Calculate the Jaro distance
    m = 0
    t = 0
    len_s1 = len(s1)
    len_s2 = len(s2)
    max_len = max(len_s1, len_s2)
    match_distance = (max_len // 2) - 1
    s1_matches = [-1] * len_s1
    s2_matches = [-1] * len_s2

    for i in range(len_s1):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, len_s2)
        for j in range(start, end):
            if s2_matches[j] != -1:
                continue
            if s1[i] != s2[j]:
                continue
            s1_matches[i] = j
            s2_matches[j] = i
            m += 1
            break

    if m == 0:
        return 0.0

    # Calculate the number of transpositions
    k = 0
    for i in range(len_s1):
        if s1_matches[i] == -1:
            continue
        j = s1_matches[i]
        if s2_matches[j] != i:
            k += 1

    t = k // 2

    # Calculate the Jaro distance
    jaro_distance = (m / len_s1 + m / len_s2 + (m - t) / m) / 3

    # Calculate the common prefix length
    l = 0
    for i in range(min(4, min(len_s1, len_s2))):
        if s1[i] == s2[i]:
            l += 1
        else:
            break

    # Calculate the Jaro-Winkler distance
    jaro_winkler_distance = jaro_distance + l * p * (1 - jaro_distance)

    return jaro_winkler_distance


class TestJaroWinklerDistance(unittest.TestCase):

    def test_same_strings(self):
        s1 = "Hello world"
        s2 = "Hello world"
        distance = jaro_winkler_distance(s1, s2)
        self.assertEqual(distance, 1.0)

    def test_case_difference(self):
        s1 = "Hello world"
        s2 = "Hello World"
        distance = jaro_winkler_distance(s1, s2)
        self.assertAlmostEqual(distance, 00.9636363636363636, places=10)

    def test_different_strings(self):
        s1 = "Hello world"
        s2 = "Goodbye world"
        distance = jaro_winkler_distance(s1, s2)
        self.assertAlmostEqual(distance, 0.7808857808857809, places=10)

    def test_unicode_strings(self):
        s1 = "こんにちは世界"
        s2 = "你好世界"
        distance = jaro_winkler_distance(s1, s2)
        self.assertAlmostEqual(distance, 0.0, places=10)

    def test_custom_scaling_factor(self):
        s1 = "Hello world"
        s2 = "Hello World"
        distance = jaro_winkler_distance(s1, s2, p=0.2)
        self.assertAlmostEqual(distance, 00.9878787878787879, places=10)


if __name__ == '__main__':
    unittest.main()
