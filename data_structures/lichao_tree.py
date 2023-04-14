import unittest


class Line:
    def __init__(self, slope: int, intercept: int):
        self.slope = slope
        self.intercept = intercept

    def eval(self, x: int) -> int:
        return self.slope * x + self.intercept


class LiChaoTree:
    def __init__(self, xmin: int, xmax: int):
        self.xmin = xmin
        self.xmax = xmax
        self.tree = [None] * (4 * (xmax - xmin + 1))

    def add_line(
            self, line: Line, node: int = 0,
            xmin: int | None = None, xmax: int | None = None
    ):
        if xmin is None:
            xmin = self.xmin
        if xmax is None:
            xmax = self.xmax
        if not self.tree[node]:
            self.tree[node] = line  # type: ignore
            return
        xm = (xmin + xmax) // 2
        if line.eval(xm) > self.tree[node].eval(xm):  # type: ignore
            self.tree[node], line = line, self.tree[node]  # type: ignore
        if xmin == xmax:
            return
        if line.slope > self.tree[node].slope:  # type: ignore
            self.add_line(line, 2 * node + 1, xm + 1, xmax)
        else:
            self.add_line(line, 2 * node, xmin, xm)

    def query(
        self, x: int, node: int = 0, xmin: int | None = None,
        xmax: int | None = None
    ) -> int | None:
        if xmin is None:
            xmin = self.xmin
        if xmax is None:
            xmax = self.xmax
        if not self.tree[node]:
            return None
        if xmin == xmax:
            return self.tree[node].eval(x)  # type: ignore
        xm = (xmin + xmax) // 2
        left_val = self.query(x, 2 * node, xmin, xm)
        right_val = self.query(x, 2 * node + 1, xm + 1, xmax)
        if left_val is None:
            return right_val
        elif right_val is None:
            return left_val
        else:
            # type: ignore
            return max(left_val, right_val, self.tree[node].eval(x))


class TestLiChaoTree(unittest.TestCase):
    def test_query_single_line(self):
        tree = LiChaoTree(-10, 10)
        tree.add_line(Line(2, 3))
        self.assertEqual(tree.query(5), 13)
        self.assertEqual(tree.query(0), 3)
        self.assertEqual(tree.query(-5), -7)

    def test_query_multiple_lines(self):
        tree = LiChaoTree(-10, 10)
        tree.add_line(Line(2, 3))
        tree.add_line(Line(-1, 10))
        tree.add_line(Line(-3, 15))
        self.assertEqual(tree.query(5), 13)
        self.assertEqual(tree.query(0), 15)
        self.assertEqual(tree.query(-5), 30)

    def test_query_out_of_range(self):
        tree = LiChaoTree(-10, 10)
        tree.add_line(Line(2, 3))
        self.assertEqual(tree.query(-20), -37)
        self.assertEqual(tree.query(20), 43)

    def test_query_empty_tree(self):
        tree = LiChaoTree(-10, 10)
        self.assertEqual(tree.query(5), None)

    def test_query_same_x_range(self):
        tree = LiChaoTree(-5, -5)
        tree.add_line(Line(2, 3))
        self.assertEqual(tree.query(-5), -7)

    def test_query_same_x_range_multiple_lines(self):
        tree = LiChaoTree(-5, -5)
        tree.add_line(Line(2, 3))
        tree.add_line(Line(-1, 10))
        tree.add_line(Line(-3, 15))
        self.assertEqual(tree.query(-5), 30)


if __name__ == '__main__':
    unittest.main()
