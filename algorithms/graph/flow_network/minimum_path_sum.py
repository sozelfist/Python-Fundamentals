import unittest


def minPathSum(grid: list[list[int]]) -> tuple[int, list[tuple[int, int]]]:
    # Check if the grid is empty
    if not grid:
        return 0, []

    # Check that all rows have the same length
    row_length = len(grid[0])
    if any(len(row) != row_length for row in grid):
        raise ValueError("Input grid must be rectangular")

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    path = [[(0, 0)] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    # fill the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
        path[0][j] = (0, j - 1)

    # fill the first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
        path[i][0] = (i - 1, 0)

    # fill the rest of the table
    for i in range(1, m):
        for j in range(1, n):
            if dp[i - 1][j] < dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
                path[i][j] = (i - 1, j)
            else:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
                path[i][j] = (i, j - 1)

    # trace back the path
    i, j = m - 1, n - 1
    res_path = [(i, j)]
    while i > 0 or j > 0:
        i, j = path[i][j]
        res_path.append((i, j))
    res_path.reverse()

    return dp[-1][-1], res_path


class TestMinPathSum(unittest.TestCase):
    def test_example_1(self):
        grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        min_sum, path = minPathSum(grid)
        self.assertEqual(min_sum, 7)
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])

    def test_example_2(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        min_sum, path = minPathSum(grid)
        self.assertEqual(min_sum, 21)
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])

    def test_empty_grid(self):
        grid = []
        min_sum, path = minPathSum(grid)
        self.assertEqual(min_sum, 0)
        self.assertEqual(path, [])

    def test_single_cell(self):
        grid = [[1]]
        min_sum, path = minPathSum(grid)
        self.assertEqual(min_sum, 1)
        self.assertEqual(path, [(0, 0)])

    def test_one_row(self):
        grid = [[1, 2, 3, 4, 5]]
        min_sum, path = minPathSum(grid)
        self.assertEqual(min_sum, 15)
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])

    def test_one_column(self):
        grid = [[1], [2], [3], [4], [5]]
        min_sum, path = minPathSum(grid)
        self.assertEqual(min_sum, 15)
        self.assertEqual(path, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])

    def test_irregular_grid(self):
        grid = [[1, 3, 2], [4, 5], [7, 6, 8, 9]]
        with self.assertRaises(ValueError):
            minPathSum(grid)


if __name__ == "__main__":
    unittest.main()
