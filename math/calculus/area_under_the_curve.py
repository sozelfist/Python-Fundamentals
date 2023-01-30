import unittest
import numpy as np


def f(x):
    return x**2


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    area = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return area


def simpsons_rule(f, a, b, n):
    h = (b - a) / (2 * n)
    x = np.linspace(a, b, 2 * n + 1)
    y = f(x)
    area = (h / 3) * (y[0] + 4 * np.sum(y[1::2]) + 2 * np.sum(y[2:-1:2]) + y[-1])
    return area


def midpoint_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)[:-1] + h / 2
    y = f(x)
    area = h * np.sum(y)
    return area


class TestIntegrationMethods(unittest.TestCase):
    def test_trapezoidal_rule(self):
        a = 0
        b = 1
        n = 200
        expected = 0.3333
        result = trapezoidal_rule(f, a, b, n)
        self.assertAlmostEqual(result, expected, places=4)

    def test_simpsons_rule(self):
        a = 0
        b = 1
        n = 100
        expected = 0.3333
        result = simpsons_rule(f, a, b, n)
        self.assertAlmostEqual(result, expected, places=4)

    def test_midpoint_rule(self):
        a = 0
        b = 1
        n = 100
        expected = 0.3333
        result = midpoint_rule(f, a, b, n)
        self.assertAlmostEqual(result, expected, places=4)


if __name__ == '__main__':
    unittest.main()
