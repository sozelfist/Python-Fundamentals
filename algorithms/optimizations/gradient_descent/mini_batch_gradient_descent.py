import unittest

import numpy as np


def linear_model(x: np.ndarray, w: float, b: float) -> np.ndarray:
    return w * x + b


def cost_function(x: np.ndarray, y: np.ndarray, w: float, b: float) -> float:
    predictions = linear_model(x, w, b)
    return ((predictions - y) ** 2).mean()


def mini_batch_gradient_descent(
    x: np.ndarray,
    y: np.ndarray,
    w: float,
    b: float,
    learning_rate: float,
    num_iterations: int,
    batch_size: int,
):
    for _i in range(num_iterations):
        # shuffle data
        indices = np.random.permutation(len(x))
        x = x[indices]
        y = y[indices]

        # split data into mini-batches
        for j in range(0, len(x), batch_size):
            x_batch = x[j : j + batch_size]
            y_batch = y[j : j + batch_size]

            # calculate gradients
            dw = ((linear_model(x_batch, w, b) - y_batch) * x_batch).mean()
            db = (linear_model(x_batch, w, b) - y_batch).mean()

            # update parameters
            w = w - learning_rate * dw
            b = b - learning_rate * db

        # calculate cost
        cost_function(x, y, w, b)
    return w, b


class TestGradientDescent(unittest.TestCase):
    def setUp(self):
        # sample data
        self.x = np.array([1, 2, 3, 4, 5])
        self.y = np.array([5, 7, 9, 11, 13])

        # initial values for parameters
        self.w = 1
        self.b = 1

        # run gradient descent
        self.learning_rate = 0.01
        self.num_iterations = 1000
        self.batch_size = 2

    def test_mini_batch_gradient_descent(self):
        final_w, final_b = mini_batch_gradient_descent(
            self.x,
            self.y,
            self.w,
            self.b,
            self.learning_rate,
            self.num_iterations,
            self.batch_size,
        )
        self.assertAlmostEqual(final_w, 2.000, delta=1e-2)
        self.assertAlmostEqual(final_b, 3.000, delta=1e-2)


if __name__ == "__main__":
    unittest.main()
