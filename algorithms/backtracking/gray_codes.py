import unittest


def generate_gray_codes(n: int) -> list[int]:
    def backtrack(gray_code: int, bit_pos: int, direction: str) -> None:
        if bit_pos == n:
            gray_codes.append(gray_code)
        else:
            if direction == "up":
                backtrack(gray_code | (1 << bit_pos), bit_pos + 1, "up")
                backtrack(gray_code & ~(1 << bit_pos), bit_pos + 1, "down")
            else:
                backtrack(gray_code & ~(1 << bit_pos), bit_pos + 1, "up")
                backtrack(gray_code | (1 << bit_pos), bit_pos + 1, "down")

    gray_codes = []
    backtrack(0, 0, "up")
    return gray_codes


class GrayCodeTestCase(unittest.TestCase):
    def test_generate_gray_codes_with_zero_bits(self):
        n = 0
        expected_gray_codes = [0]
        self.assertEqual(generate_gray_codes(n), expected_gray_codes)

    def test_generate_gray_codes_with_one_bit(self):
        n = 1
        expected_gray_codes = [1, 0]
        self.assertEqual(generate_gray_codes(n), expected_gray_codes)

    def test_generate_gray_codes_with_two_bits(self):
        # Test case with two bits
        n = 2
        expected_gray_codes = [3, 1, 0, 2]
        self.assertEqual(generate_gray_codes(n), expected_gray_codes)

    def test_generate_gray_codes_with_three_bits(self):
        n = 3
        expected_gray_codes = [7, 3, 1, 5, 4, 0, 2, 6]
        self.assertEqual(generate_gray_codes(n), expected_gray_codes)


if __name__ == "__main__":
    unittest.main()
