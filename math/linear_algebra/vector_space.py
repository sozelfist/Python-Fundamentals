import numpy as np


class VectorSpace:
    def __init__(self, vectors):
        self.vectors = np.array(vectors)

    def add(self, v):
        return VectorSpace(np.vstack((self.vectors, v)))

    def scalar_mult(self, a):
        return VectorSpace(a * self.vectors)


class SubSpace(VectorSpace):
    def __init__(self, vectors):
        super().__init__(vectors)


if __name__ == '__main__':
    # Define a vector space of 2-dimensional vectors
    vector_space = VectorSpace([[1, 2], [3, 4], [5, 6]])
    print(vector_space.vectors)

    # Define a subspace of the vector
    vector_subspace = SubSpace([[1, 2], [3, 4]])
    print(vector_subspace.vectors)
