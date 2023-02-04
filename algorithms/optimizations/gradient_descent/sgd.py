from typing import Tuple
import unittest
import numpy as np


def linear_model(x: np.ndarray, w: float, b: float) -> np.ndarray:
    return w * x + b


def cost_function(x: np.ndarray, y: np.ndarray, w: float, b: float) -> float:
    predictions = linear_model(x, w, b)

    return ((predictions - y)**2).mean()


def stochastic_gradient_descent(
        x: np.ndarray, y: np.ndarray, w: float, b: float, learning_rate: float, num_iterations: int
) -> Tuple[float, float]:
    for i in range(num_iterations):
        # shuffle data
        indices = np.random.permutation(len(x))
        x = x[indices]
        y = y[indices]

        for j in range(len(x)):
            x_data = x[j]
            y_data = y[j]

            # calculate gradients
            dw = (linear_model(x_data, w, b) - y_data) * x_data
            db = (linear_model(x_data, w, b) - y_data)

            # update parameters
            w = w - learning_rate * dw
            b = b - learning_rate * db

        # calculate cost
        cost = cost_function(x, y, w, b)

        # print progress
        if (i + 1) % 100 == 0:
            print(f'Iteration: {i+1}, cost = {cost}, w = {w}, b = {b}')
    return w, b


class TestStochasticGradientDescent(unittest.TestCase):
    def test_stochastic_gradient_descent(self):
        # sample data
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([5, 7, 9, 11, 13])

        # initial values for parameters
        w = 1
        b = 1

        # run gradient descent
        learning_rate = 0.01
        num_iterations = 500
        final_w, final_b = stochastic_gradient_descent(x, y, w, b, learning_rate, num_iterations)

        # Check final values are as expected
        self.assertAlmostEqual(final_w, 2.0, delta=0.1)
        self.assertAlmostEqual(final_b, 3.0, delta=0.1)


if __name__ == '__main__':
    unittest.main()
