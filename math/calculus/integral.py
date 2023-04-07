import unittest

import numpy as np


def integrate(func, a, b, method="trapezoidal", **kwargs):
    if method == "trapezoidal":
        return trapezoidal_rule(func, a, b, **kwargs)
    elif method == "midpoint":
        return midpoint_rule(func, a, b, **kwargs)
    elif method == "gaussian":
        return gaussian_quadrature(func, a, b, **kwargs)
    elif method == "monte_carlo":
        return monte_carlo(func, a, b, **kwargs)
    else:
        raise ValueError("Invalid integration method")


def trapezoidal_rule(func, a, b, n=1000):
    x = np.linspace(a, b, n)

    y = func(x)
    return (b - a) * (np.sum(y) - 0.5 * (y[0] + y[-1])) / n


def midpoint_rule(func, a, b, n=1000):
    x = np.linspace(a, b, n)

    dx = (b - a) / n
    return dx * np.sum(func((x[:-1] + x[1:]) / 2))


def gaussian_quadrature(func, a, b, n=1000):

    x, w = np.polynomial.legendre.leggauss(n)
    x = 0.5 * (b - a) * x + 0.5 * (b + a)
    return 0.5 * (b - a) * np.dot(func(x), w)


def monte_carlo(func, a, b, n=1000):
    x = np.random.uniform(a, b, n)
    y = func(x)
    return (b - a) * (np.sum(y) / n)


class TestIntegrationMethods(unittest.TestCase):
    def test_trapezoidal_rule(self):
        self.assertAlmostEqual(integrate(lambda x: x**2, 0, 1, method="trapezoidal", n=2000), 1 / 3, delta=0.0003)

    def test_midpoint_rule(self):
        self.assertAlmostEqual(integrate(lambda x: x**2, 0, 1, method="midpoint", n=2000), 1 / 3, delta=0.0003)

    def test_gaussian_quadrature(self):
        self.assertAlmostEqual(integrate(lambda x: x**2, 0, 1, method="gaussian"), 1 / 3, places=5)

    def test_monte_carlo(self):
        self.assertAlmostEqual(integrate(lambda x: x**2, 0, 1, method="monte_carlo"), 1 / 3, places=1)


if __name__ == '__main__':
    unittest.main()
