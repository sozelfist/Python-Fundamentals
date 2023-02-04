from typing import Tuple
import unittest
import numpy as np


def linear_model(x: np.ndarray, w: float, b: float) -> np.ndarray:
    return w * x + b


def cost_function(x: np.ndarray, y: np.ndarray, w: float, b: float) -> float:
    predictions = linear_model(x, w, b)
    return ((predictions - y)**2).mean()


def adam(
        x: np.ndarray, y: np.ndarray, w: float, b: float,
        learning_rate: float, num_iterations: int,
        beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-8
) -> Tuple[float, float]:
    # initialize variables for momentum
    m_w = 0
    m_b = 0
    v_w = 0
    v_b = 0

    for i in range(num_iterations):
        # calculate gradients
        dw = (linear_model(x, w, b) - y).dot(x) / len(x)
        db = (linear_model(x, w, b) - y).mean()

        # update momentum
        m_w = beta1 * m_w + (1 - beta1) * dw
        m_b = beta1 * m_b + (1 - beta1) * db
        v_w = beta2 * v_w + (1 - beta2) * (dw**2)
        v_b = beta2 * v_b + (1 - beta2) * (db**2)

        # bias correction
        m_w_hat = m_w / (1 - beta1**(i + 1))
        m_b_hat = m_b / (1 - beta1**(i + 1))
        v_w_hat = v_w / (1 - beta2**(i + 1))
        v_b_hat = v_b / (1 - beta2**(i + 1))

        # update parameters
        w = w - learning_rate * m_w_hat / (np.sqrt(v_w_hat) + epsilon)
        b = b - learning_rate * m_b_hat / (np.sqrt(v_b_hat) + epsilon)

        # calculate cost
        cost = cost_function(x, y, w, b)
    return w, b


class TestAdam(unittest.TestCase):

    def test_adam(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([5, 7, 9, 11, 13])

        w = 1
        b = 1

        learning_rate = 0.01
        num_iterations = 3000
        final_w, final_b = adam(x, y, w, b, learning_rate, num_iterations)

        self.assertAlmostEqual(final_w, 2.0, delta=0.001)
        self.assertAlmostEqual(final_b, 3.0, delta=0.001)


if __name__ == '__main__':
    unittest.main()
