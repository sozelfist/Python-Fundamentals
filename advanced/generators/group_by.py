import unittest


class GroupBy:
    """
    Group an iterable by key function.

    Arguments:
    - iterable: The iterable to group.
    - key: A function used to determine the key for each element. If None,
      the identity function is used.

    Examples:
    - [k for k, g in GroupBy('AAAABBBCCDAABBB')] --> A B C D A B
    - [list(g) for k, g in GroupBy('AAAABBBCCD')] --> AAAA BBB CC D
    """

    def __init__(self, iterable, key=None):  # type: ignore
        if key is None:

            def key(x):
                return x

        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()

    def __iter__(self):
        return self

    def __next__(self):
        self.id = object()
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)  # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey, self.id))

    def _grouper(self, tgtkey, id):
        while self.id is id and self.currkey == tgtkey:
            yield self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)


class TestGroupby(unittest.TestCase):
    def test_groupby_empty(self):
        self.assertListEqual([x for x in GroupBy("")], [])

    def test_groupby_single_group(self):
        self.assertListEqual(
            [
                (1, [1, 1, 1]),
            ],
            [(k, list(g)) for k, g in GroupBy([1, 1, 1])],
        )

    def test_groupby_multiple_groups(self):
        self.assertListEqual(
            [(0, [0]), (1, [1, 1]), (0, [0, 0]), (1, [1])],
            [(k, list(g)) for k, g in GroupBy([0, 1, 1, 0, 0, 1])],
        )

    def test_groupby_custom_key(self):
        data = ["Apple", "Banana", "Cherry", "Durian", "Elderberry"]
        expected = [
            ("A", ["Apple"]),
            ("B", ["Banana"]),
            ("C", ["Cherry"]),
            ("D", ["Durian"]),
            ("E", ["Elderberry"]),
        ]
        self.assertListEqual(
            expected, [(k, list(g)) for k, g in GroupBy(data, key=lambda x: x[0])]
        )

    def test_groupby_generator_input(self):
        data = (i for i in range(1, 8))
        expected = [(0, [1]), (1, [2, 3]), (2, [4, 5]), (3, [6, 7])]
        self.assertListEqual(
            expected, [(k, list(g)) for k, g in GroupBy(data, key=lambda x: x // 2)]
        )

    def test_groupby_filter_empty_groups(self):
        data = ["", "A", "", "B", "", "", "C"]
        expected = [("A", ["A"]), ("B", ["B"]), ("C", ["C"])]
        self.assertListEqual(expected, [(k, list(g)) for k, g in GroupBy(data) if k])


if __name__ == "__main__":
    unittest.main()
