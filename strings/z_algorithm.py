import unittest


def z_algorithm(text: str, pattern: str) -> list[int]:
    concat = pattern + "$" + text
    Z = [0] * len(concat)
    Z[0] = len(concat)
    l, r = 0, 0
    for i in range(1, len(concat)):
        if i > r:
            l, r = i, i
            while r < len(concat) and concat[r - l] == concat[r]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            k = i - l
            if Z[k] < r - i + 1:
                Z[i] = Z[k]
            else:
                l = i
                while r < len(concat) and concat[r - l] == concat[r]:
                    r += 1
                Z[i] = r - l
                r -= 1
    result = []
    for i in range(len(pattern) + 1, len(concat)):
        if Z[i] == len(pattern):
            result.append(i - len(pattern) - 1)
    return result


class TestZAlgorithm(unittest.TestCase):
    def test_text_contains_pattern_at_multiple_positions(self):
        text = "the quick brown fox jumps over the lazy dog."
        pattern = "the"
        expected_result = [0, 31]
        self.assertEqual(z_algorithm(text, pattern), expected_result)

    def test_text_does_not_contain_pattern(self):
        text = "the quick brown fox jumps over the lazy dog."
        pattern = "abc"
        expected_result = []
        self.assertEqual(z_algorithm(text, pattern), expected_result)

    def test_text_and_pattern_are_identical(self):
        text = "the quick brown fox jumps over the lazy dog."
        pattern = "the quick brown fox jumps over the lazy dog."
        expected_result = [0]
        self.assertEqual(z_algorithm(text, pattern), expected_result)


if __name__ == '__main__':
    unittest.main()
