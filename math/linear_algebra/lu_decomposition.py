import numpy as np
import unittest


def lower_upper_decomposition(table: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    rows, columns = np.shape(table)
    if rows != columns:
        raise ValueError(f"'table' has to be a square shaped array but got a {rows}x{columns} array.")

    lower = np.zeros((rows, columns))
    upper = np.zeros((rows, columns))

    for i in range(columns):
        for j in range(i):
            temp = 0
            for k in range(j):
                temp += lower[i][k] * upper[k][j]
            lower[i][j] = (table[i][j] - temp) / upper[j][j]
        lower[i][i] = 1
        for j in range(i, columns):
            temp = 0
            for k in range(i):
                temp += lower[i][k] * upper[k][j]
            upper[i][j] = table[i][j] - temp

    return lower, upper


class TestLowerUpperDecomposition(unittest.TestCase):
    def test_decomposition(self):
        matrix = np.array([[2, -2, 1], [0, 1, 2], [5, 3, 1]])
        lower, upper = lower_upper_decomposition(matrix)

        np.testing.assert_array_almost_equal(lower, np.array([[1., 0., 0.], [0., 1., 0.], [2.5, 8., 1.]]))
        np.testing.assert_array_almost_equal(upper, np.array([[2., -2., 1.], [0., 1., 2.], [0., 0., -17.5]]))

    def test_shape_error(self):
        matrix = np.array([[2, -2, 1], [0, 1, 2]])
        with self.assertRaises(ValueError):
            lower_upper_decomposition(matrix)


if __name__ == '__main__':
    unittest.main()
