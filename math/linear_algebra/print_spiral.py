import unittest
from typing import List


def print_spiral(matrix: List[List[int]], direction: str) -> List[int]:
    # check empty matrix
    if not matrix:
        return []

    # make 4 matrix sentinels: left, right, top, bottom
    rows = len(matrix)
    cols = len(matrix[0])
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    spiral = []

    while top <= bottom and left <= right:
        # Traverse right
        for col in range(left, right + 1):
            spiral.append(matrix[top][col])
        top += 1

        # Traverse down
        for row in range(top, bottom + 1):
            spiral.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # Traverse left
            for col in range(right, left - 1, -1):
                spiral.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # Traverse up
            for row in range(bottom, top - 1, -1):
                spiral.append(matrix[row][left])
            left += 1

    # Reverse the spiral if counterclockwise direction is given
    if direction == "counterclockwise":
        spiral = spiral[::-1]

    return spiral


class TestPrintSpiral(unittest.TestCase):

    def test_print_spiral_clockwise(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected_output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        result = print_spiral(matrix, "clockwise")
        self.assertEqual(result, expected_output)

    def test_print_spiral_counterclockwise(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected_output = [5, 4, 7, 8, 9, 6, 3, 2, 1]
        result = print_spiral(matrix, "counterclockwise")
        self.assertEqual(result, expected_output)

    def test_print_spiral_single_element_matrix(self):
        matrix = [[1]]
        expected_output = [1]
        result = print_spiral(matrix, "clockwise")
        self.assertEqual(result, expected_output)

    def test_print_spiral_empty_matrix(self):
        matrix = []
        expected_output = []
        result = print_spiral(matrix, "clockwise")
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
