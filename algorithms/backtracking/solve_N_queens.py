import unittest


def is_safe(board: list[list[int]], row: int, col: int) -> bool:
    # check the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # check th e  top l e ft diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # check th e  top r i ght diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True


def solve_n_queens(board: list[list[int]], row: int) -> bool:
    if row == len(board):
        return True
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True

            board[row][col] = 0
    return False


def n_queens(n: int) -> list[list[int]]:
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0):
        return []
    return board


class TestNQueens(unittest.TestCase):
    def test_n_queens(self):
        n = 4
        result = n_queens(n)
        self.assertEqual(
            result,
            [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]]
        )

        n = 5
        result = n_queens(n)
        self.assertEqual(
            result,
            [
                [1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]
            ]
        )


if __name__ == '__main__':
    unittest.main()
