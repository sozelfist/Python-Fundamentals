import unittest


def AND(a, b):
    return a & b


def OR(a, b):
    return a | b


def NOT(a):
    return ~a & 0x1


def NAND(a, b):
    return NOT(a & b)


def NOR(a, b):
    return NOT(a | b)


def XOR(a, b):
    return a ^ b


def XNOR(a, b):
    return NOT(a ^ b)


class TestBooleanOperators(unittest.TestCase):
    def test_AND(self):
        self.assertEqual(AND(1, 1), 1)
        self.assertEqual(AND(1, 0), 0)
        self.assertEqual(AND(0, 1), 0)
        self.assertEqual(AND(0, 0), 0)

    def test_OR(self):
        self.assertEqual(OR(1, 1), 1)
        self.assertEqual(OR(1, 0), 1)
        self.assertEqual(OR(0, 1), 1)
        self.assertEqual(OR(0, 0), 0)

    def test_NOT(self):
        self.assertEqual(NOT(1), 0)
        self.assertEqual(NOT(0), 1)

    def test_NAND(self):
        self.assertEqual(NAND(1, 1), 0)
        self.assertEqual(NAND(1, 0), 1)
        self.assertEqual(NAND(0, 1), 1)
        self.assertEqual(NAND(0, 0), 1)

    def test_NOR(self):
        self.assertEqual(NOR(1, 1), 0)
        self.assertEqual(NOR(1, 0), 0)
        self.assertEqual(NOR(0, 1), 0)
        self.assertEqual(NOR(0, 0), 1)

    def test_XOR(self):
        self.assertEqual(XOR(1, 1), 0)
        self.assertEqual(XOR(1, 0), 1)
        self.assertEqual(XOR(0, 1), 1)
        self.assertEqual(XOR(0, 0), 0)

    def test_XNOR(self):
        self.assertEqual(XNOR(1, 1), 1)
        self.assertEqual(XNOR(1, 0), 0)
        self.assertEqual(XNOR(0, 1), 0)
        self.assertEqual(XNOR(0, 0), 1)


if __name__ == '__main__':
    unittest.main()
