import unittest


class Vector:
    """
    A simple 2D vector class with basic operations.
    """

    def __init__(self, x: float, y: float):
        """
        Initializes a 2D vector with the provided x and y coordinates.

        Args:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns the string representation of the vector.
        """
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """
        Defines the addition operation between two vectors.

        Args:
            other (Vector): The other vector to be added.

        Returns:
            Vector: The resulting vector after addition.
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Defines the subtraction operation between two vectors.

        Args:
            other (Vector): The other vector to be subtracted.

        Returns:
            Vector: The resulting vector after subtraction.
        """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float):
        """
        Defines the scalar multiplication operation for a vector.

        Args:
            scalar (float): The scalar value to multiply the vector.

        Returns:
            Vector: The resulting vector after scalar multiplication.
        """
        return Vector(self.x * scalar, self.y * scalar)


class TestVector(unittest.TestCase):
    def test_addition(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        result = v1 + v2
        self.assertEqual(str(result), "(4, 6)")

    def test_subtraction(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        result = v1 - v2
        self.assertEqual(str(result), "(-2, -2)")

    def test_scalar_multiplication(self):
        v1 = Vector(1, 2)
        result = v1 * 2
        self.assertEqual(str(result), "(2, 4)")


if __name__ == "__main__":
    unittest.main()
