import unittest


def find_knights_tour(
        board_size: tuple[int, int], start_pos: tuple[int, int]
) -> tuple[list[tuple[int, int]], list[list[int]]]:
    moves = []
    board = [[-1 for _ in range(board_size[0])] for _ in range(board_size[1])]
    row, col = start_pos
    move_count = 0
    board[row][col] = move_count

    def get_legal_moves(board, row, col):
        moves = []
        for r, c in [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]:
            if 0 <= r < board_size[0] \
                    and 0 <= c < board_size[1]\
                    and board[r][c] == -1:
                moves.append((r, c))
        return moves

    def knight_tour_recursive(row, col, move_count):
        nonlocal moves
        nonlocal board

        if move_count == board_size[0] * board_size[1] - 1:
            moves.append((row, col))
            return True

        legal_moves = get_legal_moves(board, row, col)
        if not legal_moves:
            return False

        legal_moves = sorted(legal_moves, key=lambda x: len(
            get_legal_moves(board, x[0], x[1])))

        for move in legal_moves:
            r, c = move
            board[r][c] = move_count + 1
            if knight_tour_recursive(r, c, move_count + 1):
                moves.append((row, col))
                return True
            board[r][c] = -1

        return False

    knight_tour_recursive(row, col, move_count)
    moves.append(start_pos)
    moves.reverse()

    return moves, board


class TestKnightTour(unittest.TestCase):

    def test_5x5_board(self):
        board_size = (5, 5)
        start_pos = (2, 2)
        expected_board = [
            [24, 9, 14, 3, 18],
            [15, 4, 17, 8, 13],
            [10, 23, 0, 19, 2],
            [5, 16, 21, 12, 7],
            [22, 11, 6, 1, 20]
        ]
        _, board = find_knights_tour(board_size, start_pos)
        self.assertEqual(board, expected_board)

    def test_6x6_board(self):
        board_size = (6, 6)
        start_pos = (2, 2)
        expected_board = [
            [32, 1, 34, 15, 18, 7],
            [35, 14, 31, 8, 29, 16],
            [2, 33, 0, 17, 6, 19],
            [13, 24, 21, 30, 9, 28],
            [22, 3, 26, 11, 20, 5],
            [25, 12, 23, 4, 27, 10]
        ]
        _, board = find_knights_tour(board_size, start_pos)
        self.assertEqual(board, expected_board)

    def test_8x8_board(self):
        board_size = (8, 8)
        start_pos = (0, 0)
        expected_board = [
            [0, 49, 14, 31, 60, 27, 12, 29],
            [15, 32, 63, 54, 13, 30, 59, 26],
            [50, 1, 48, 43, 56, 61, 28, 11],
            [33, 16, 55, 62, 53, 46, 25, 58],
            [2, 51, 44, 47, 42, 57, 10, 39],
            [17, 34, 19, 52, 45, 40, 7, 24],
            [20, 3, 36, 41, 22, 5, 38, 9],
            [35, 18, 21, 4, 37, 8, 23, 6]
        ]
        _, board = find_knights_tour(board_size, start_pos)
        self.assertEqual(board, expected_board)


if __name__ == '__main__':
    unittest.main()
