import unittest

import numpy as np


def linear_model(x: np.ndarray, w: float, b: float) -> np.ndarray:
    return w * x + b


def cost_function(x: np.ndarray, y: np.ndarray, w: float, b: float) -> float:
    predictions = linear_model(x, w, b)
    return ((predictions - y) ** 2).mean()


def momentum_gradient_descent(
    x: np.ndarray,
    y: np.ndarray,
    w: float,
    b: float,
    learning_rate: float,
    num_iterations: int,
    momentum: float = 0.9,
) -> tuple[float, float]:
    v_dw = 0
    v_db = 0

    for _i in range(num_iterations):
        # calculate gradients
        dw = (linear_model(x, w, b) - y).dot(x) / len(x)
        db = (linear_model(x, w, b) - y).mean()

        # update parameters with momentum
        v_dw = momentum * v_dw + (1 - momentum) * dw
        v_db = momentum * v_db + (1 - momentum) * db
        w = w - learning_rate * v_dw
        b = b - learning_rate * v_db

        # calculate cost
        cost_function(x, y, w, b)
    return w, b


class TestMomentumGradientDescent(unittest.TestCase):
    def test_momentum_gradient_descent(self):
        # sample data
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([5, 7, 9, 11, 13])

        # initial values for parameters
        w = 1
        b = 1

        # run gradient descent
        learning_rate = 0.01
        num_iterations = 3000
        final_w, final_b = momentum_gradient_descent(
            x, y, w, b, learning_rate, num_iterations
        )

        self.assertAlmostEqual(final_w, 2.000, delta=1e-2)
        self.assertAlmostEqual(final_b, 3.000, delta=1e-2)


if __name__ == "__main__":
    unittest.main()
