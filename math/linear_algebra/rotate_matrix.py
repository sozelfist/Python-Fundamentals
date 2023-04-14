import unittest


def rotate_matrix(matrix, angle, direction):
    # Ensure that the angle is valid
    assert angle in [90, 180, 270], "Invalid angle"

    # Determine the number of rotations to perform
    num_rotations = angle // 90

    # Perform the rotations
    for _i in range(num_rotations):
        # Transpose the matrix
        for j in range(len(matrix)):
            for k in range(j, len(matrix)):
                matrix[j][k], matrix[k][j] = matrix[k][j], matrix[j][k]

        # Reverse the rows or columns, depending on the direction
        if direction == "clockwise":
            matrix = [row[::-1] for row in matrix]
        elif direction == "counterclockwise":
            matrix = matrix[::-1]

    return matrix


class TestRotateMatrix(unittest.TestCase):

    def test_rotate_clockwise_90(self):
        # Define the input and expected output matrices
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected_output = [[7, 4, 1],
                           [8, 5, 2],
                           [9, 6, 3]]

        # Rotate the matrix clockwise by 90 degrees and check the output
        output = rotate_matrix(matrix, 90, "clockwise")
        self.assertEqual(output, expected_output)

    def test_rotate_clockwise_180(self):
        # Define the input and expected output matrices
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected_output = [[9, 8, 7],
                           [6, 5, 4],
                           [3, 2, 1]]

        # Rotate the matrix clockwise by 180 degrees and check the output
        output = rotate_matrix(matrix, 180, "clockwise")
        self.assertEqual(output, expected_output)

    def test_rotate_counterclockwise_270(self):
        # Define the input and expected output matrices
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected_output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

        # Rotate the matrix counterclockwise by 270 degrees
        # and check the output
        output = rotate_matrix(matrix, 270, "counterclockwise")
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
