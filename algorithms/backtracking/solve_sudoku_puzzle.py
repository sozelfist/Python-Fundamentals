import unittest


def is_safe(grid: list[list[int]], row: int, col: int, num: int) -> bool:
    # check the same row
    for x in range(9):
        if grid[row][x] == num:
            return False
    # check the same column
    for x in range(9):
        if grid[x][col] == num:
            return False
    # check the same 3x3 subgrid
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def solve_sudoku(grid: list[list[int]], row: int, col: int) -> bool:
    if row == 9:
        return True
    if col == 9:
        return solve_sudoku(grid, row + 1, 0)
    if grid[row][col] != 0:
        return solve_sudoku(grid, row, col + 1)
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True
            grid[row][col] = 0

    return False


def sudoku(grid: list[list[int]]) -> list[list[int]]:
    if not solve_sudoku(grid, 0, 0):
        return []
    return grid


class TestSudoku(unittest.TestCase):
    def test_sudoku(self):
        grid = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
                [6, 8, 0, 0, 7, 0, 0, 9, 0],
                [1, 9, 0, 0, 0, 4, 5, 0, 0],
                [8, 2, 0, 1, 0, 0, 0, 4, 0],
                [0, 0, 4, 6, 0, 2, 9, 0, 0],
                [0, 5, 0, 0, 0, 3, 0, 2, 8],
                [0, 0, 9, 3, 0, 0, 0, 7, 4],
                [0, 4, 0, 0, 5, 0, 0, 3, 6],
                [7, 0, 3, 0, 1, 8, 0, 0, 0]]
        result = sudoku(grid)
        self.assertEqual(result, [[4, 3, 5, 2, 6, 9, 7, 8, 1],
                                  [6, 8, 2, 5, 7, 1, 4, 9, 3],
                                  [1, 9, 7, 8, 3, 4, 5, 6, 2],
                                  [8, 2, 6, 1, 9, 5, 3, 4, 7],
                                  [3, 7, 4, 6, 8, 2, 9, 1, 5],
                                  [9, 5, 1, 7, 4, 3, 6, 2, 8],
                                  [5, 1, 9, 3, 2, 6, 8, 7, 4],
                                  [2, 4, 8, 9, 5, 7, 1, 3, 6],
                                  [7, 6, 3, 4, 1, 8, 2, 5, 9]])


if __name__ == '__main__':
    unittest.main()
