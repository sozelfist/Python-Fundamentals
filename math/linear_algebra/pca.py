import numpy as np
import matplotlib.pyplot as plt


def pca(X, n_components):
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


if __name__ == "__main__":
    np.random.seed(0)
    X = np.random.rand(100, 5)

    # Perform PCA on the data
    n_components = 2
    X_pca, eigenvectors = pca(X, n_components)

    print("Original data shape: ", X.shape)
    print("Transformed data shape: ", X_pca.shape)
    print("Eigenvectors shape: ", eigenvectors.shape)

    # Plot the transformed data
    plt.scatter(X_pca[:, 0], X_pca[:, 1])
    plt.xlabel("First Principal Component")
    plt.ylabel("Second Principal Component")
    plt.show()
