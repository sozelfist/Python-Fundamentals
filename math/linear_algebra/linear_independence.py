import unittest

import numpy as np


def check_linear_independence(vectors: list[list[int]]) -> str:
    matrix = np.column_stack(vectors)
    rref, _ = np.linalg.qr(matrix)
    if np.all(rref[np.where(rref != 0)] == 1):
        return "Linearly Independent"
    else:
        return "Linearly Dependent"


class TestCheckLinearIndependence(unittest.TestCase):
    def test_linearly_independent(self):
        vectors = [[1, 2], [3, 4], [5, 6]]
        result = check_linear_independence(vectors)
        self.assertEqual(result, "Linearly Dependent")

    def test_linearly_dependent(self):
        vectors = [[1, 2], [2, 4], [5, 10]]
        result = check_linear_independence(vectors)
        self.assertEqual(result, "Linearly Dependent")


if __name__ == '__main__':
    unittest.main()
