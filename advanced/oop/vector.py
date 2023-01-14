import unittest
import numpy as np
import cmath


class Vector:
    """ Represent a vector in the multidimensional space """

    def __init__(self, dimensions):
        """ Create d-dimensional vector of zeroes """
        self._coords = np.zeros(dimensions)

    def __len__(self):
        """ Return the dimension of the vector """
        return len(self._coords)

    def __getitem__(self, index):
        """ Return j-th coordinate of vector """
        return self._coords[index]

    def __setitem__(self, index, value):
        """ Set j-th coordinate of vector to given value """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric type")
        self._coords[index] = value

    def __add__(self, other):
        """ Return sum of two vectors """
        if len(self) != len(other):
            raise ValueError("Dimensions must be agree")
        return Vector(self._coords + other._coords)

    def __sub__(self, other):
        """ Return subtraction of two vectors """
        if len(self) != len(other):
            raise ValueError("Dimensions must be agree")
        return Vector(self._coords - other._coords)

    def __mul__(self, scalar):
        """ Return the result of multiplying the vector by a scalar """
        return Vector(self._coords * scalar)

    def __truediv__(self, scalar):
        """ Return the result of dividing the vector by a scalar """
        return Vector(self._coords / scalar)

    def __eq__(self, other):
        """ Return true if vectors have same coordinates as other """
        return np.array_equal(self._coords, other._coords)

    def __ne__(self, other):
        """ Return true if vector differ from other """
        return not self == other

    def __str__(self):
        """ Procedure string representation of vector """
        return "<" + str(self._coords)[1:-1] + ">"

    def __repr__(self):
        """ Return a string representation of the object that can be used to recreate the object. """
        return f'Vector({self._coords.tolist()})'

    def setVector(self, compLists):
        """ Assign values for vector's components from given list """
        if len(self) != len(compLists):
            raise ValueError("Dimensions must be agree")
        if all(isinstance(i, (int, float)) for i in compLists):
            self._coords = np.array(compLists)
        else:
            raise ValueError("compLists must contains only numeric values")

    def norm(self):
        """ Return length of vector """
        return cmath.sqrt(np.dot(self._coords, self._coords))

    def scalarProduct(self, other):
        """ Return scalar product of two vector """
        if len(self) != len(other):
            raise ValueError("Dimensions must be agree")
        return np.dot(self._coords, other._coords)

    def angleWith(self, other):
        """ Return angle between self and other in radian (from 0 to pi)"""
        return cmath.acos(np.clip(np.dot(self._coords, other._coords) / (self.norm() * other.norm()), -1.0, 1.0))

    def unit_vector(self):
        """ Return the unit vector of the vector """
        return self / self.norm()


class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(3)
        self.v2 = Vector(3)
        self.v1.setVector([1, 2, 3])
        self.v2.setVector([2, 3, 4])
        self.v3 = Vector(3)
        self.v3.setVector([3, 4, 5])
        self.v4 = Vector(2)
        self.v4.setVector([1, 2])

    def test_init(self):
        v = Vector(3)
        self.assertEqual(len(v), 3)
        self.assertEqual(v._coords.tolist(), [0, 0, 0])

    def test_setVector(self):
        v = Vector(3)
        v.setVector([1, 2, 3])
        self.assertEqual(v._coords.tolist(), [1, 2, 3])

    def test_setVector_with_non_numeric_values(self):
        v = Vector(3)
        with self.assertRaises(ValueError) as context:
            v.setVector([1, 2, "a"])
        self.assertEqual(str(context.exception),
                         "compLists must contains only numeric values")

    def test_setVector_with_different_dimension(self):
        v = Vector(2)
        with self.assertRaises(ValueError) as context:
            v.setVector([1, 2, 3])
        self.assertEqual(str(context.exception), "Dimensions must be agree")

    def test_add(self):
        v = self.v1 + self.v2
        self.assertEqual(v._coords.tolist(), [3, 5, 7])

    def test_add_with_different_dimension(self):
        with self.assertRaises(ValueError) as context:
            v = self.v1 + self.v4
        self.assertEqual(str(context.exception), "Dimensions must be agree")

    def test_sub(self):
        v = self.v1 - self.v2
        self.assertEqual(v._coords.tolist(), [-1, -1, -1])

    def test_mul(self):
        v = self.v1 * 2
        self.assertEqual(v._coords.tolist(), [2, 4, 6])

    def test_truediv(self):
        v = self.v1 / 2
        self.assertEqual(v._coords.tolist(), [0.5, 1.0, 1.5])

    def test_eq(self):
        self.assertTrue(self.v1 == self.v1)
        self.assertFalse(self.v1 == self.v2)

    def test_ne(self):
        self.assertFalse(self.v1 != self.v1)
        self.assertTrue(self.v1 != self.v2)

    def test_norm(self):
        v1 = Vector([3, 4])
        self.assertEqual(v1.norm(), 5)
        v2 = Vector([0, 0, 0])
        self.assertEqual(v2.norm(), 0)
        v3 = Vector([1, 2, 3, 4, 5])
        self.assertEqual(v3.norm(), cmath.sqrt(55))
        v4 = Vector([-1, -2, -3, -4, -5])
        self.assertEqual(v4.norm(), cmath.sqrt(55))

    def test_scalar_product(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertTrue(v1.scalarProduct(v2) == 32)
        v1 = Vector([-1, -2, -3])
        v2 = Vector([4, 5, 6])
        self.assertTrue(v1.scalarProduct(v2) == -32)
        v1 = Vector([1, 2, 3])
        v2 = Vector([-4, -5, -6])
        self.assertTrue(v1.scalarProduct(v2) == -32)

    def test_angle_with(self):
        v1 = Vector([1, 0])
        v2 = Vector([0, 1])
        self.assertTrue(v1.angleWith(v2) == cmath.acos(0))
        v1 = Vector([1, 1])
        v2 = Vector([1, 1])
        self.assertTrue(v1.angleWith(v2) == cmath.acos(1))
        v1 = Vector([-1, -1])
        v2 = Vector([1, 1])
        self.assertTrue(v1.angleWith(v2) == cmath.acos(-1))

    def test_unit_vector(self):
        v = Vector([4, 0])
        self.assertTrue(v.unit_vector() == Vector([1, 0]))
        v = Vector([0, 5])
        self.assertTrue(v.unit_vector() == Vector([0, 1]))
        v = Vector([3, 4])
        self.assertTrue(v.unit_vector().norm() == 1)
        v = Vector([-3, -4])
        self.assertTrue(v.unit_vector().norm() == 1)


if __name__ == '__main__':
    unittest.main()
