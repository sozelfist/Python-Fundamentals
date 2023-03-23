import unittest
from typing import List, Tuple


def isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_map = {}
    used_chars = set()

    for i in range(len(s)):
        if s[i] in char_map:
            if char_map[s[i]] != t[i]:
                return False
        else:
            if t[i] in used_chars:
                return False
            char_map[s[i]] = t[i]
            used_chars.add(t[i])

    return True


class TestIsomorphic(unittest.TestCase):

    def test_isomorphic(self):
        test_cases: List[Tuple[str, str, bool]] = [
            ("egg", "add", True),
            ("foo", "bar", False),
            ("paper", "title", True),
            ("ab", "aa", False),
            ("ab", "cd", True)
        ]

        for s, t, expected in test_cases:
            with self.subTest(s=s, t=t):
                result = isomorphic(s, t)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
