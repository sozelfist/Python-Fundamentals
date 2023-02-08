import unittest
from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    result = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result


class TestPascalTriangle(unittest.TestCase):
    def test_pascal_triangle(self):
        expected_output = '''
            [1]
            [1, 1]
            [1, 2, 1]
            [1, 3, 3, 1]
            [1, 4, 6, 4, 1]
            [1, 5, 10, 10, 5, 1]
        '''
        pascal_triangle(6)
        self.assertEqual(expected_output, expected_output)


if __name__ == '__main__':
    unittest.main()
