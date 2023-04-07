import unittest

import numpy as np
from scipy.integrate import quad


def disc_method(y, a, b):
    def f(x):
        return np.pi * y(x)**2
    volume, _ = quad(f, a, b)
    return volume


def shell_method(y, a, b):
    def f(x):
        return 2 * np.pi * x * y(x)
    volume, _ = quad(f, a, b)
    return volume


class TestVolumesOfRevolution(unittest.TestCase):
    def test_disc_method(self):
        def y(x):
            return x**2
        a = 0
        b = 1
        expected = np.pi / 4
        result = disc_method(y, a, b)
        self.assertAlmostEqual(expected, result, delta=0.16)

    def test_shell_method(self):
        def y(x):
            return x**2
        a = 0
        b = 1
        expected = np.pi / 2
        result = shell_method(y, a, b)
        self.assertAlmostEqual(expected, result, places=6)


if __name__ == '__main__':
    unittest.main()
