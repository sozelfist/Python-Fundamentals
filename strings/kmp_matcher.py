import unittest


def kmp_matcher(text: str, pattern: str) -> list[int]:
    lps = compute_lps(pattern)
    text_len = len(text)
    pattern_len = len(pattern)
    i = 0
    j = 0
    matches = []
    while i < text_len:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == pattern_len:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < text_len and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches


def compute_lps(pattern: str) -> list[int]:
    pattern_len = len(pattern)
    lps = [0] * pattern_len
    length = 0
    i = 1
    while i < pattern_len:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


class TestKMPMatcher(unittest.TestCase):
    def test_given_text_and_pattern(self):
        text = "ABABDABACDABABCABAB"
        pattern = "ABABCABAB"
        expected_output = [10]
        self.assertEqual(kmp_matcher(text, pattern), expected_output)

    def test_no_occurrence_of_pattern_in_text(self):
        text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pattern = "ZZZZZ"
        expected_output = []
        self.assertEqual(kmp_matcher(text, pattern), expected_output)

    def test_pattern_occurs_multiple_times_in_text(self):
        text = "AABAACAADAABAABA"
        pattern = "AABA"
        expected_output = [0, 9, 12]
        self.assertEqual(kmp_matcher(text, pattern), expected_output)

    def test_pattern_is_a_substring_of_text(self):
        text = "abcdefghijklmnopqrstuvwxyz"
        pattern = "def"
        expected_output = [3]
        self.assertEqual(kmp_matcher(text, pattern), expected_output)

    def test_pattern_is_equal_to_text(self):
        text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pattern = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        expected_output = [0]
        self.assertEqual(kmp_matcher(text, pattern), expected_output)


if __name__ == "__main__":
    unittest.main()
