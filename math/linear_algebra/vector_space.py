import numpy as np
import unittest


class VectorSpace:
    def __init__(self, vectors: np.ndarray):
        self.vectors = np.array(vectors)

    def add(self, v: np.ndarray):
        return VectorSpace(np.vstack((self.vectors, v)))

    def scalar_mult(self, a: float):
        return VectorSpace(a * self.vectors)


class SubSpace(VectorSpace):
    def __init__(self, vectors: np.ndarray):
        super().__init__(vectors)


class TestVectorSpace(unittest.TestCase):
    def test_init(self):
        vectors = np.array([[1, 2], [3, 4], [5, 6]])
        vector_space = VectorSpace(vectors)
        np.testing.assert_array_equal(vectors, vector_space.vectors)

    def test_add(self):
        vectors = np.array([[1, 2], [3, 4], [5, 6]])
        v = np.array([[7, 8]])
        expected = np.vstack((vectors, v))
        vector_space = VectorSpace(vectors)
        result = vector_space.add(v).vectors
        np.testing.assert_array_equal(expected, result)

    def test_scalar_mult(self):
        vectors = np.array([[1, 2], [3, 4], [5, 6]])
        a = 2
        expected = 2 * vectors
        vector_space = VectorSpace(vectors)
        result = vector_space.scalar_mult(a).vectors
        np.testing.assert_array_equal(expected, result)


class TestSubSpace(unittest.TestCase):
    def test_init(self):
        vectors = np.array([[1, 2], [3, 4]])
        vector_subspace = SubSpace(vectors)
        np.testing.assert_array_equal(vectors, vector_subspace.vectors)


if __name__ == '__main__':
    unittest.main()
