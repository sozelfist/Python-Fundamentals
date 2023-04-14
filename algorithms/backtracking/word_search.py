import unittest


def exist(board: list[list[str]], word: str) -> bool:
    if not board:
        return False

    def backtrack(i, j, word):
        if len(word) == 0:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0])\
                or board[i][j] != word[0]:
            return False

        temp, board[i][j] = board[i][j], "#"
        res = backtrack(i + 1, j, word[1:]) or \
            backtrack(i - 1, j, word[1:])\
            or backtrack(i, j + 1, word[1:]) or backtrack(i, j - 1, word[1:])
        board[i][j] = temp

        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, word):
                return True

    return False


class TestExist(unittest.TestCase):

    def test_exist_true(self):
        board = [['A', 'B', 'C', 'E'],
                 ['S', 'F', 'C', 'S'],
                 ['A', 'D', 'E', 'E']]
        self.assertTrue(exist(board, "ABCCED"))
        self.assertTrue(exist(board, "SEE"))
        self.assertFalse(exist(board, "ABCBDE"))
        self.assertFalse(exist(board, "ASAFESEEDA"))

    def test_exist_false(self):
        board = [['A', 'B', 'C', 'E'],
                 ['S', 'F', 'C', 'S'],
                 ['A', 'D', 'E', 'E']]
        self.assertFalse(exist(board, "ABCB"))
        self.assertFalse(exist(board, "ABCD"))
        self.assertFalse(exist(board, "FEBA"))
        self.assertFalse(exist(board, "SADEAFECB"))

    def test_exist_empty(self):
        board = []
        self.assertFalse(exist(board, "ABCB"))
        self.assertFalse(exist(board, ""))


if __name__ == '__main__':
    unittest.main()
