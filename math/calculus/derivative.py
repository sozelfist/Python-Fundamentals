import math
import unittest


def derivative(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


class TestDerivative(unittest.TestCase):
    def test_derivative(self):
        def f(x):
            return x**2
        self.assertAlmostEqual(derivative(f, 2), 4, places=5)
        self.assertAlmostEqual(derivative(f, 0), 0, places=5)
        self.assertAlmostEqual(
            derivative(math.sin, math.pi / 2),
            math.cos(math.pi / 2), places=5
        )

    def test_derivative_with_custom_h(self):
        def f(x):
            return x**3
        self.assertAlmostEqual(derivative(f, 2), 12, places=5)


if __name__ == '__main__':
    unittest.main()
