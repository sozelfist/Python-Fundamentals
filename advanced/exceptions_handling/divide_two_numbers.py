import unittest


def divide(numerator: int, denominator: int) -> float | None:
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        result = None
    except TypeError:
        print("Both numerator and denominator should be numbers.")
        result = None
    return result


class TestDivideFunction(unittest.TestCase):
    def test_divide_valid_inputs(self):
        result = divide(10, 2)
        self.assertEqual(result, 5.0)

    def test_divide_denominator_zero(self):
        result = divide(10, 0)
        self.assertIsNone(result)

    def test_divide_non_numeric_inputs(self):
        result = divide(10, 'a')
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
