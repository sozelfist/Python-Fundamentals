import unittest


def hamming_distance(s1: str, s2: str) -> tuple[int, list]:
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    distance = 0
    diff_indices = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
            diff_indices.append(i)
    return distance, diff_indices


class TestHammingDistance(unittest.TestCase):
    def test_identical_strings(self):
        s1 = "abcd"
        s2 = "abcd"
        distance, diff_indices = hamming_distance(s1, s2)
        self.assertEqual(distance, 0)
        self.assertEqual(diff_indices, [])

    def test_different_strings(self):
        s1 = "karolin"
        s2 = "kathrin"
        distance, diff_indices = hamming_distance(s1, s2)
        self.assertEqual(distance, 3)
        self.assertEqual(diff_indices, [2, 3, 4])

    def test_strings_with_whitespace(self):
        s1 = " abc def "
        s2 = " abc  def"
        distance, diff_indices = hamming_distance(s1, s2)
        self.assertEqual(distance, 4)
        self.assertEqual(diff_indices, [5, 6, 7, 8])

    def test_strings_with_different_lengths(self):
        s1 = "abcd"
        s2 = "abcde"
        with self.assertRaises(ValueError):
            hamming_distance(s1, s2)


if __name__ == "__main__":
    unittest.main()
