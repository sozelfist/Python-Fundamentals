import math
import unittest
from typing import Any

import numpy as np


class Vector:
    def __init__(self, coords: Any):
        self._coords = np.array(coords)

    def __len__(self) -> int:
        return len(self._coords)

    def __getitem__(self, index: int) -> int | float:
        return self._coords[index]

    def __setitem__(self, index: int, value: Any):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric")
        self._coords[index] = value

    def __repr__(self) -> str:
        return f'Vector({self._coords.tolist()})'

    def __str__(self) -> str:
        return f'<{self._coords}>'

    def __add__(self, other: 'Vector') -> 'Vector':
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(self._coords + other._coords)

    def __sub__(self, other: 'Vector') -> 'Vector':
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(self._coords - other._coords)

    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self._coords * scalar)

    def __truediv__(self, scalar: float) -> 'Vector':
        return Vector(self._coords * (1 / scalar))

    def __eq__(self, other: 'Vector') -> bool:
        return np.array_equal(self._coords, other._coords)

    def __ne__(self, other: 'Vector') -> bool:
        return not self == other

    def norm(self) -> float:
        return math.sqrt(np.dot(self._coords, self._coords.T))

    def dot(self, other: 'Vector') -> float:
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions")
        return np.dot(self._coords, other._coords)

    def angle_with(self, other: 'Vector') -> float:
        return np.arccos(
            np.clip(self.dot(other) / (self.norm() * other.norm()), -1.0, 1.0)
        )

    def unit(self) -> 'Vector':
        return self / self.norm()


class TestVector(unittest.TestCase):
    def test_create_vector(self):
        v = Vector([1, 2, 3])
        self.assertEqual(len(v), 3)
        self.assertEqual(v[0], 1)
        self.assertEqual(v[1], 2)
        self.assertEqual(v[2], 3)

    def test_access_out_of_bounds(self):
        v = Vector([1, 2, 3])
        with self.assertRaises(IndexError):
            v[3]

    def test_set_item(self):
        v = Vector([1, 2, 3])
        v[0] = 4
        self.assertEqual(v[0], 4)

    def test_set_item_with_invalid_value(self):
        v = Vector([1, 2, 3])
        with self.assertRaises(TypeError):
            v[0] = "invalid"

    def test_add_vectors(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v3 = v1 + v2
        self.assertEqual(len(v3), 3)
        self.assertEqual(v3[0], 5)
        self.assertEqual(v3[1], 7)
        self.assertEqual(v3[2], 9)

    def test_add_vectors_with_different_dimensions(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5])
        with self.assertRaises(ValueError):
            v1 + v2

    def test_subtract_vectors(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v3 = v1 - v2
        self.assertEqual(len(v3), 3)
        self.assertEqual(v3[0], -3)
        self.assertEqual(v3[1], -3)
        self.assertEqual(v3[2], -3)

    def test_subtract_vectors_with_different_dimensions(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5])
        with self.assertRaises(ValueError):
            v1 - v2

    def test_multiply_vector_by_scalar(self):
        v1 = Vector([1, 2, 3])
        v2 = v1 * 2
        self.assertEqual(len(v2), 3)
        self.assertEqual(v2[0], 2)
        self.assertEqual(v2[1], 4)
        self.assertEqual(v2[2], 6)

    def test_divide_vector_by_scalar(self):
        v1 = Vector([1, 2, 3])
        v2 = v1 / 2
        self.assertEqual(v2._coords.tolist(), [0.5, 1.0, 1.5])

    def test_vector_equality(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2, 3])
        v3 = Vector([1, 2, 4])
        self.assertEqual(v1, v2)
        self.assertNotEqual(v1, v3)

    def test_vector_norm(self):
        v = Vector([3, 4])
        self.assertEqual(v.norm(), 5.0)

    def test_vector_dot_product(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertEqual(v1.dot(v2), 32)

    def test_vector_angle_with(self):
        v1 = Vector([1, 0])
        v2 = Vector([0, 1])
        self.assertEqual(v1.angle_with(v2), math.pi / 2)

    def test_vector_unit(self):
        v = Vector([1, 2])
        self.assertEqual(v.unit(), Vector(
            [1 / math.sqrt(5), 2 / math.sqrt(5)]))


if __name__ == '__main__':
    unittest.main()
