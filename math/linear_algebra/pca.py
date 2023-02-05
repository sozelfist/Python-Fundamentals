import numpy as np
from typing import Tuple
import unittest


def pca(X: np.ndarray, n_components: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Perform PCA on the input data X and return the transformed data and the eigenvectors.
    """
    # Subtract the mean of the data from each feature
    X = X - np.mean(X, axis=0)

    # Compute the covariance matrix of the data
    cov = np.cov(X, rowvar=False)

    # Compute the eigenvalues and eigenvectors of the covariance matrix
    eigenvalues, eigenvectors = np.linalg.eig(cov)

    # Sort the eigenvalues and eigenvectors in descending order of eigenvalues
    eigenvalues_sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[eigenvalues_sorted_indices]
    eigenvectors = eigenvectors[:, eigenvalues_sorted_indices]

    # Select the first n_components eigenvectors
    eigenvectors = eigenvectors[:, :n_components]

    # Compute the transformed data
    X_pca = np.matmul(X, eigenvectors)

    # Return the transformed data and the eigenvectors
    return X_pca, eigenvectors


class TestPCA(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        self.X = np.random.rand(100, 5)

    def test_pca_output_shape(self):
        n_components = 2
        X_pca, eigenvectors = pca(self.X, n_components)
        self.assertEqual(X_pca.shape, (100, 2))
        self.assertEqual(eigenvectors.shape, (5, 2))

    def test_pca_transformed_data(self):
        n_components = 2
        X_pca_1, _ = pca(self.X, n_components)
        X_pca_2, _ = pca(self.X, n_components)
        self.assertTrue(np.allclose(X_pca_1, X_pca_2))


if __name__ == "__main__":
    unittest.main()
