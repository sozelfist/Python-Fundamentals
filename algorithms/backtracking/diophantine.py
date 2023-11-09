import unittest


def extended_euclidean(a: int, b: int) -> tuple[int, int, int]:
    """
    Computes the extended Euclidean algorithm for finding the greatest common divisor (gcd) and
    Bezout coefficients x and y such that ax + by = gcd.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        tuple[int, int, int]: The tuple containing the gcd and the Bezout coefficients x and y.

    """
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extended_euclidean(b, a % b)
        return (gcd, y, x - (a // b) * y)


def diophantine(a: int, b: int, c: int) -> None | tuple[int, int]:
    """
    Solves the Diophantine equation ax + by = c using the extended Euclidean algorithm.

    Args:
        a (int): Coefficient of x.
        b (int): Coefficient of y.
        c (int): Constant term.

    Returns:
        None | tuple[int, int]: The solution (x, y) if it exists; None otherwise.

    """
    gcd, x, y = extended_euclidean(a, b)
    if c % gcd != 0:
        return None
    else:
        return (x * (c // gcd), y * (c // gcd))


class TestDiophantine(unittest.TestCase):
    def test_diophantine_with_solution(self):
        result = diophantine(5, 7, 1)
        self.assertEqual(result, (3, -2))

    def test_diophantine_without_solution(self):
        result = diophantine(4, 6, 7)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
