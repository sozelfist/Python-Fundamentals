import unittest

import numpy as np


def linear_model(x: np.ndarray, w: float, b: float) -> np.ndarray:
    return w * x + b


def cost_function(x: np.ndarray, y: np.ndarray, w: float, b: float) -> float:
    predictions = linear_model(x, w, b)
    return ((predictions - y) ** 2).mean()


def batch_gradient_descent(
    x: np.ndarray,
    y: np.ndarray,
    w: float,
    b: float,
    learning_rate: float,
    num_iterations: int,
) -> tuple[float, float]:
    for i in range(num_iterations):
        # calculate gradients
        dw = ((linear_model(x, w, b) - y) * x).mean()
        db = (linear_model(x, w, b) - y).mean()

        # update parameters
        w = w - learning_rate * dw
        b = b - learning_rate * db

        # calculate cost
        cost = cost_function(x, y, w, b)

        # print progress
        if (i + 1) % 100 == 0:
            print(f"Iteration: {i+1}, cost = {cost}, w = {w}, b = {b}")
    return w, b


class TestBatchGradientDescent(unittest.TestCase):
    def test_batch_gradient_descent(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([5, 7, 9, 11, 13])
        w = 1
        b = 1
        learning_rate = 0.01
        num_iterations = 5000
        final_w, final_b = batch_gradient_descent(
            x, y, w, b, learning_rate, num_iterations
        )
        self.assertAlmostEqual(final_w, 2.0003, delta=0.001)
        self.assertAlmostEqual(final_b, 2.9992, delta=0.001)


if __name__ == "__main__":
    unittest.main()
