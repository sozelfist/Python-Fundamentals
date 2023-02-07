import unittest


def binary_to_decimal(binary: str) -> int:
    decimal = 0
    for i, digit in enumerate(binary):
        decimal += int(digit) * (2 ** (len(binary) - i - 1))
    return decimal


class TestBinaryToDecimal(unittest.TestCase):
    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal("0"), 0)
        self.assertEqual(binary_to_decimal("1"), 1)
        self.assertEqual(binary_to_decimal("10"), 2)
        self.assertEqual(binary_to_decimal("11"), 3)
        self.assertEqual(binary_to_decimal("1111"), 15)
        self.assertEqual(binary_to_decimal("10000"), 16)


if __name__ == '__main__':
    unittest.main()
