import unittest

import numpy as np
from scipy.optimize import minimize


def linear_model(x: np.ndarray, w: float, b: float) -> np.ndarray:
    return w * x + b


def cost_function(
        params: list[float], x: np.ndarray, y: np.ndarray
) -> float:
    w, b = params
    predictions = linear_model(x, w, b)
    return ((predictions - y)**2).mean()


def grad_cost_function(
    params: list[float], x: np.ndarray, y: np.ndarray
) -> np.ndarray:
    w, b = params
    dw = (linear_model(x, w, b) - y).dot(x) / len(x)
    db = (linear_model(x, w, b) - y).mean()
    return np.array([dw, db])


class TestLinearModel(unittest.TestCase):

    def test_lbfgs(self):
        # sample data
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([5, 7, 9, 11, 13])

        # initial values for parameters
        params = [1, 1]

        # run L-BFGS
        res = minimize(
            cost_function, params, args=(x, y),
            method='L-BFGS-B', jac=grad_cost_function
        )

        final_w, final_b = res.x
        expected_w, expected_b = (2, 3)

        self.assertAlmostEqual(final_w, expected_w, delta=1e-6)
        self.assertAlmostEqual(final_b, expected_b, delta=1e-6)


if __name__ == '__main__':
    unittest.main()
