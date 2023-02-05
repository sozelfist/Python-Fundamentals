import unittest
from typing import List


def determinant(A: List[List[int]]) -> int:
    """
    Calculate the determinant of a matrix A
    """
    n = len(A)
    if n != len(A[0]):
        raise ValueError("The matrix is not square, determinant not defined")

    if n == 2:
        return A[0][0] * A[1][1] - A[1][0] * A[0][1]

    cofactors = []
    for c in range(n):
        cofactorRow = []
        for r in range(n):
            minor = [row[:c] + row[c + 1:] for row in (A[:r] + A[r + 1:])]
            cofactorRow.append((-1)**(r + c) * determinant(minor))
        cofactors.append(cofactorRow)

    det = sum(A[i][0] * cofactors[i][0] for i in range(n))
    return det


class TestDeterminant(unittest.TestCase):
    def test_square_matrix(self):
        A = [[2, 1, 5], [1, 2, 7], [8, 9, 10]]
        result = determinant(A)
        self.assertEqual(result, -96)

    def test_not_square_matrix(self):
        A = [[2, 1, 5, 4], [1, 2, 7, 2]]
        with self.assertRaises(ValueError):
            determinant(A)


if __name__ == '__main__':
    unittest.main()
