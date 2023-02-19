from typing import List
import unittest


class SparseTable:
    def __init__(self, arr: List[int]) -> None:
        n = len(arr)
        k = (n).bit_length()  # The smallest power of 2 that is greater than or equal to n
        self.st = [[0] * k for _ in range(n)]
        self.log = [0] * (n + 1)

        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

        for i in range(n):
            self.st[i][0] = arr[i]

        for j in range(1, k):
            for i in range(n - (1 << j) + 1):
                self.st[i][j] = min(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])

    def query(self, l: int, r: int) -> int:
        """
        Returns the minimum value in the range [l, r] of the original array.
        """
        j = self.log[r - l + 1]
        return min(self.st[l][j], self.st[r - (1 << j) + 1][j])

    def get_table(self) -> List[List[int]]:
        """
        Returns the Sparse Table.
        """
        return self.st

    def get_log(self) -> List[int]:
        """
        Returns the logarithm table used for precomputing the Sparse Table.
        """
        return self.log

    def get_length(self) -> int:
        """
        Returns the length of the original array.
        """
        return len(self.st)

    def get_element(self, i: int, j: int) -> int:
        """
        Returns the element at row i and column j of the Sparse Table.
        """
        return self.st[i][j]


class TestSparseTable(unittest.TestCase):
    def test_query(self):
        arr = [4, 1, 3, 5, 2, 6, 7, 8]
        st = SparseTable(arr)

        self.assertEqual(st.query(1, 3), 1)
        self.assertEqual(st.query(2, 5), 2)
        self.assertEqual(st.query(0, 7), 1)
        self.assertEqual(st.query(4, 7), 2)
        self.assertEqual(st.query(3, 3), 5)

    def test_get_table(self):
        arr = [4, 1, 3, 5, 2, 6, 7, 8]
        st = SparseTable(arr)

        self.assertEqual(st.get_table(),
                         [[4, 1, 1, 1], [1, 1, 1, 0], [3, 3, 2, 0], [5, 2, 2, 0],
                          [2, 2, 2, 0], [6, 6, 0, 0], [7, 7, 0, 0], [8, 0, 0, 0]])

    def test_get_length(self):
        arr = [4, 1, 3, 5, 2, 6, 7, 8]
        st = SparseTable(arr)

        self.assertEqual(st.get_length(), 8)

    def test_get_element(self):
        arr = [4, 1, 3, 5, 2, 6, 7, 8]
        st = SparseTable(arr)

        self.assertEqual(st.get_element(0, 0), 4)
        self.assertEqual(st.get_element(2, 2), 2)
        self.assertEqual(st.get_element(5, 1), 6)
        self.assertEqual(st.get_element(7, 3), 0)


if __name__ == '__main__':
    unittest.main()
