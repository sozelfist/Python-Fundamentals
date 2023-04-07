import math
import unittest

import scipy.integrate as spi


def average_value(f, a, b):
    """Calculates the average value of a function over an interval [a, b].

    Arguments:
        f {function} -- the function to calculate the average value of
        a {float} -- the lower bound of the interval
        b {float} -- the upper bound of the interval

    Returns:
        float -- the average value of the function over the interval
    """
    result, _ = spi.quad(f, a, b)
    return result / (b - a)


class TestAverageValue(unittest.TestCase):
    def test_average_value(self):
        def f(x):
            return x**2

        a = 0
        b = 1
        expected = 1 / 3
        result = average_value(f, a, b)
        self.assertAlmostEqual(result, expected, delta=1e-5)

        def g(x):
            return math.sin(x)

        a = 0
        b = math.pi
        expected = 2 / math.pi
        result = average_value(g, a, b)
        self.assertAlmostEqual(result, expected, delta=1e-5)


if __name__ == '__main__':
    unittest.main()
