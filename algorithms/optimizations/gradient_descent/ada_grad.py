import unittest

import numpy as np


def linear_model(x: np.ndarray, w: float, b: float) -> np.ndarray:
    return w * x + b


def cost_function(x: np.ndarray, y: np.ndarray, w: float, b: float) -> float:
    predictions = linear_model(x, w, b)
    return ((predictions - y) ** 2).mean()


def adaptive_gradient_descent(
    x: np.ndarray,
    y: np.ndarray,
    w: float,
    b: float,
    learning_rate: float,
    num_iterations: int,
) -> tuple[float, float]:
    sum_dw = 0
    sum_db = 0

    for i in range(num_iterations):
        dw = (linear_model(x, w, b) - y).dot(x) / len(x)
        db = (linear_model(x, w, b) - y).mean()

        sum_dw += dw**2
        sum_db += db**2

        w = w - learning_rate * dw / (np.sqrt(sum_dw) + 1e-8)
        b = b - learning_rate * db / (np.sqrt(sum_db) + 1e-8)

        cost = cost_function(x, y, w, b)

        if (i + 1) % 1000 == 0:
            print(f"Iteration: {i+1}, cost = {cost}, w = {w}, b = {b}")
    return w, b


class TestAdaGrad(unittest.TestCase):
    def test_adagrad(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([5, 7, 9, 11, 13])
        w = 1
        b = 1
        learning_rate = 0.01
        num_iterations = 5000
        final_w, final_b = adaptive_gradient_descent(
            x, y, w, b, learning_rate, num_iterations
        )
        self.assertAlmostEqual(final_w, 2.0121, delta=0.001)
        self.assertAlmostEqual(final_b, 2.0325, delta=0.001)


if __name__ == "__main__":
    unittest.main()
