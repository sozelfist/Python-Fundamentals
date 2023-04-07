import unittest

import numpy as np


def svd(A: np.ndarray) -> tuple:
    # Compute the transpose of A
    A_transpose = np.transpose(A)
    # Compute the matrix B = A * A_transpose
    B = np.matmul(A, A_transpose)
    # Compute the eigenvectors and eigenvalues of B
    eigenvalues, eigenvectors = np.linalg.eig(B)
    # Compute the matrix S^2 as a diagonal matrix with the eigenvalues as entries
    S_squared = np.diag(eigenvalues)
    # Compute the matrix S as the square root of S^2
    S = np.sqrt(S_squared)
    # Compute the matrix U as the matrix of eigenvectors of B
    U = eigenvectors
    # Compute the matrix V as the matrix of eigenvectors of A_transpose * A with the eigenvalues of S^2
    V = np.matmul(np.matmul(A_transpose, U), np.linalg.inv(S))
    # Return the matrices U, S, and V
    return U, S, V


class TestSVD(unittest.TestCase):
    def test_svd(self):
        A = np.array([[3, 2, 2], [2, 3, -2]])
        U, S, V = svd(A)
        np.testing.assert_allclose(A, U @ S @ np.transpose(V), rtol=1e-6, atol=1e-6)


if __name__ == '__main__':
    unittest.main()
