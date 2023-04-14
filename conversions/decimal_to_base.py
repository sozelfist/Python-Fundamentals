import unittest


def decimal_to_base(decimal: int, base: int) -> str:
    if decimal == 0:
        return "0"
    elif decimal < 0 or base < 2:
        raise ValueError(
            "Invalid input: decimal must be a positive integer\
             and base must be 2 or greater"
        )

    digits = "0123456789ABCDEF"
    result = ""
    while decimal > 0:
        result = digits[decimal % base] + result
        decimal = decimal // base
    return result


class TestDecimalToBase(unittest.TestCase):
    def test_binary(self):
        self.assertEqual(decimal_to_base(30, 2), "11110")

    def test_octal(self):
        self.assertEqual(decimal_to_base(30, 8), "36")

    def test_hexadecimal(self):
        self.assertEqual(decimal_to_base(30, 16), "1E")

    def test_zero_decimal(self):
        self.assertEqual(decimal_to_base(0, 2), "0")

    def test_negative_decimal(self):
        with self.assertRaises(ValueError):
            decimal_to_base(-30, 2)

    def test_base_less_than_2(self):
        with self.assertRaises(ValueError):
            decimal_to_base(30, 1)


if __name__ == '__main__':
    unittest.main()
