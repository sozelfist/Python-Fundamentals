import math
import random
import unittest


def monte_carlo_pi(num_points: int) -> float:
    """
    Calculates an approximation of pi using the Monte Carlo method.
    :param num_points: The number of points to be generated.
    :return: An approximation of pi.
    """
    if num_points <= 0:
        raise ValueError("Number of points must be positive")

    random.seed(0)
    inside = 0
    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if math.sqrt(x ** 2 + y ** 2) <= 1:
            inside += 1
    return 4 * inside / num_points


class TestMonteCarloPi(unittest.TestCase):
    def test_positive_number_of_points(self):
        result = monte_carlo_pi(10000)
        self.assertAlmostEqual(result, 3.1416, delta=0.01)

    def test_zero_number_of_points(self):
        with self.assertRaises(ValueError):
            monte_carlo_pi(0)


if __name__ == '__main__':
    unittest.main()
