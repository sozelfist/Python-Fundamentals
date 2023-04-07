import unittest

import numpy as np


def cholesky_decomposition(A: np.ndarray) -> tuple[np.ndarray, bool]:
    n = A.shape[0]
    if n != A.shape[1]:
        raise ValueError('Input matrix must be square')
    if not np.allclose(A, A.T):
        raise ValueError('Input matrix must be symmetric')

    positive_definite = np.all(np.linalg.eigvals(A) > 0)
    if not positive_definite:
        return (np.zeros_like(A), False)

    L = np.zeros_like(A)
    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i, k] * L[j, k] for k in range(j))
            L[i, j] = np.sqrt(A[i, i] - s) if (i == j) else (1.0 / L[j, j] * (A[i, j] - s))

    return (L, True)


class CholeskyDecompositionTestCase(unittest.TestCase):
    def test_positive_definite(self):
        A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
        L, positive_definite = cholesky_decomposition(A)
        self.assertTrue(positive_definite)
        self.assertTrue(np.allclose(A, L @ L.T))

    def test_not_positive_definite(self):
        A = np.array([[1, 2], [2, 1]])
        L, positive_definite = cholesky_decomposition(A)
        self.assertFalse(positive_definite)

    def test_not_symmetric(self):
        A = np.array([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError):
            cholesky_decomposition(A)


if __name__ == '__main__':
    unittest.main()
