import unittest


def decimal_to_binary(decimal: int) -> str:
    if decimal == 0:
        return "0"
    binary = []
    while decimal > 0:
        binary.append(str(decimal % 2))
        decimal = decimal // 2
    return "".join(reversed(binary))


class TestDecimalToBinary(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(0), "0")
        self.assertEqual(decimal_to_binary(1), "1")
        self.assertEqual(decimal_to_binary(2), "10")
        self.assertEqual(decimal_to_binary(3), "11")
        self.assertEqual(decimal_to_binary(15), "1111")
        self.assertEqual(decimal_to_binary(16), "10000")


if __name__ == "__main__":
    unittest.main()
