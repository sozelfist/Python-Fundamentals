import math
import unittest


def binomial_pmf(n: int, p: float, k: int) -> float:
    """
    Calculates the probability mass function (PMF) of a binomial distribution.

    Parameters:
    n (int): The number of trials.
    p (float): The probability of success in each trial.
    k (int): The number of successful outcomes.

    Returns:
    float: The PMF of the binomial distribution.
    """
    binomial_coefficient = math.comb(n, k)
    pmf = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))
    return pmf


def binomial_mean(n: int, p: float) -> float:
    """
    Calculates the mean of a binomial distribution.

    Parameters:
    n (int): The number of trials.
    p (float): The probability of success in each trial.

    Returns:
    float: The mean of the binomial distribution.
    """
    mean = n * p
    return mean


def binomial_variance(n: int, p: float) -> float:
    """
    Calculates the variance of a binomial distribution.

    Parameters:
    n (int): The number of trials.
    p (float): The probability of success in each trial.

    Returns:
    float: The variance of the binomial distribution.
    """
    variance = n * p * (1 - p)
    return variance


def binomial_probability_mass_function(
    n: int, p: float, k_values: list[int]
) -> list[float]:
    """
    Calculates the PMF for a set of values of k.

    Parameters:
    n (int): The number of trials.
    p (float): The probability of success in each trial.
    k_values (List[int]): The values of k for which the PMF should
    be calculated.

    Returns:
    List[float]: The PMF for each value of k.
    """
    pmf_values = [binomial_pmf(n, p, k) for k in k_values]
    return pmf_values


class TestBinomialDistribution(unittest.TestCase):
    def test_binomial_pmf(self):
        n = 10
        p = 0.5
        k = 5
        expected_pmf = 0.24609375
        self.assertAlmostEqual(binomial_pmf(n, p, k), expected_pmf, places=7)

    def test_binomial_mean(self):
        n = 10
        p = 0.5
        expected_mean = 5.0
        self.assertAlmostEqual(binomial_mean(n, p), expected_mean, places=7)

    def test_binomial_variance(self):
        n = 10
        p = 0.5
        expected_variance = 2.5
        self.assertAlmostEqual(binomial_variance(
            n, p), expected_variance, places=7)

    def test_binomial_probability_mass_function(self):
        n = 10
        p = 0.5
        k_values = [2, 4, 10]
        expected_pmf_values = [0.04395, 0.20508, 0.00098]
        pmf_values = binomial_probability_mass_function(n, p, k_values)
        for i, pmf_value in enumerate(pmf_values):
            self.assertAlmostEqual(pmf_value, expected_pmf_values[i], places=5)


if __name__ == '__main__':
    unittest.main()
