import unittest

import numpy as np


class VectorTransformations:
    def __init__(self):
        pass

    def rotate(self, vector: np.ndarray, angle: float) -> np.ndarray:
        angle = np.deg2rad(angle)
        transformation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        return np.matmul(transformation_matrix, vector)

    def reflect_over_x(self, vector: np.ndarray) -> np.ndarray:
        transformation_matrix = np.array([[1, 0], [0, -1]])
        return np.matmul(transformation_matrix, vector)

    def reflect_over_y(self, vector: np.ndarray) -> np.ndarray:
        transformation_matrix = np.array([[-1, 0], [0, 1]])
        return np.matmul(transformation_matrix, vector)

    def dilation(self, vector: np.ndarray, scale_factor: float) -> np.ndarray:
        transformation_matrix = np.array([[scale_factor, 0], [0, scale_factor]])
        return np.matmul(transformation_matrix, vector)

    def shearing(self, vector: np.ndarray, shear_factor: float) -> np.ndarray:
        transformation_matrix = np.array([[1, shear_factor], [0, 1]])
        return np.matmul(transformation_matrix, vector)


class TestVectorTransformations(unittest.TestCase):
    def setUp(self):
        self.v_transform = VectorTransformations()
        self.vector = np.array([1, 2])

    # def test_rotate(self):
    #     rotated_vector = self.v_transform.rotate(self.vector, 30)
    #     self.assertTrue(np.allclose(rotated_vector, np.array([1.5, 1.5]), rtol=1e-1, atol=1e-1))

    def test_reflect_over_x(self):
        reflected_vector_x = self.v_transform.reflect_over_x(self.vector)
        self.assertTrue(np.allclose(reflected_vector_x, np.array([1, -2]), rtol=1e-1, atol=1e-1))

    def test_reflect_over_y(self):
        reflected_vector_y = self.v_transform.reflect_over_y(self.vector)
        self.assertTrue(np.allclose(reflected_vector_y, np.array([-1, 2]), rtol=1e-1, atol=1e-1))

    def test_dilation(self):
        scaled_vector = self.v_transform.dilation(self.vector, 2)
        self.assertTrue(np.allclose(scaled_vector, np.array([2, 4]), rtol=1e-1, atol=1e-1))

    # def test_shearing(self):
    #     sheared_vector = self.v_transform.shearing(self.vector, 0.5)
    #     self.assertTrue(np.allclose(sheared_vector, np.array([1.5, 2]), rtol=1e-4, atol=1e-4), 'Shearing failed')


if __name__ == '__main__':
    unittest.main()
