import unittest


def rabin_karp_matcher(text: str, pattern: str) -> list[int]:
    def hash_func(string: str, prime: int, multiplier: int) -> int:
        hash_value = 0
        for i in range(len(string)):
            hash_value = (hash_value * multiplier + ord(string[i])) % prime
        return hash_value

    def verify_match(text: str, start: int, end: int, pattern: str) -> bool:
        for i in range(len(pattern)):
            if text[start + i] != pattern[i]:
                return False
        return True

    prime = 101
    multiplier = 256
    pattern_hash = hash_func(pattern, prime, multiplier)
    text_hash = hash_func(text[: len(pattern)], prime, multiplier)
    result = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash:
            if verify_match(text, i, i + len(pattern), pattern):
                result.append(i)
        if i < len(text) - len(pattern):
            text_hash = (
                text_hash * multiplier
                - ord(text[i]) * (multiplier ** len(pattern)) % prime
                + ord(text[i + len(pattern)])
            ) % prime
    return result


class TestRabinKarp(unittest.TestCase):
    def test_matches(self):
        text = "The quick brown fox jumps over the lazy dog."
        pattern = "the"
        result = rabin_karp_matcher(text, pattern)
        self.assertEqual(result, [31])

    def test_no_matches(self):
        text = "The quick brown fox jumps over the lazy dog."
        pattern = "xyz"
        result = rabin_karp_matcher(text, pattern)
        self.assertEqual(result, [])

    def test_empty_pattern(self):
        text = "The quick brown fox jumps over the lazy dog."
        pattern = ""
        result = rabin_karp_matcher(text, pattern)
        self.assertEqual(
            result,
            [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36,
                37,
                38,
                39,
                40,
                41,
                42,
                43,
                44,
            ],
        )

    def test_empty_text(self):
        text = ""
        pattern = "the"
        result = rabin_karp_matcher(text, pattern)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
