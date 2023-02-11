import unittest
from typing import List


def boyer_moore(text: str, pattern: str) -> List[int]:
    n = len(text)
    m = len(pattern)
    if m == 0:
        return [0]
    if n == 0:
        return []
    last = {}
    for k in range(m):
        last[pattern[k]] = k
    i = m - 1
    k = m - 1
    indices = []
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                indices.append(i)
                i += m
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return indices


class TestBoyerMoore(unittest.TestCase):
    def test_empty_text(self):
        text = ""
        pattern = "abc"
        indices = boyer_moore(text, pattern)
        self.assertEqual(indices, [])

    def test_empty_pattern(self):
        text = "abc"
        pattern = ""
        indices = boyer_moore(text, pattern)
        self.assertEqual(indices, [0])

    def test_no_occurrences(self):
        text = "abcdefg"
        pattern = "xyz"
        indices = boyer_moore(text, pattern)
        self.assertEqual(indices, [])

    def test_single_occurrence(self):
        text = "abcdefg"
        pattern = "cde"
        indices = boyer_moore(text, pattern)
        self.assertEqual(indices, [2])

    def test_multiple_occurrences(self):
        text = "the quick brown fox jumps over the lazy dog"
        pattern = "the"
        indices = boyer_moore(text, pattern)
        self.assertEqual(indices, [0, 31])


if __name__ == "__main__":
    unittest.main()
