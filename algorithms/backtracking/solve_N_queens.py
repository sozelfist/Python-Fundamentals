import unittest


def is_safe(board: list[list[int]], row: int, col: int) -> bool:
    """
    Checks whether placing a queen at a specific position (row, col) on the board is safe or not.

    Args:
        board (list[list[int]]): The current state of the chessboard.
        row (int): The row index for the queen.
        col (int): The column index for the queen.

    Returns:
        bool: True if the placement is safe, False otherwise.
    """
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
    """
    Recursively solves the N-Queens problem by backtracking.

    Args:
        board (list[list[int]]): The current state of the chessboard.
        row (int): The current row to place the queen.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
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
    """
    Finds a valid solution to the N-Queens problem for an NxN chessboard.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list[list[int]]: A list representing the arrangement of queens on the chessboard.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0):
        return []
    return board


class TestNQueens(unittest.TestCase):
    def test_n_queens(self):
        """
        Tests the n_queens function for valid solutions on different board sizes.
        """
        n = 4
        result = n_queens(n)
        self.assertEqual(result, [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]])

        n = 5
        result = n_queens(n)
        self.assertEqual(result, [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]])


if __name__ == "__main__":
    unittest.main()
