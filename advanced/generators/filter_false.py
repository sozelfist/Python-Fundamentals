import unittest


def filterfalse(predicate, iterable):
    """Return those items of iterable for which function(item) is false.

    If predicate is None, return the items that are false.
    """
    if not callable(predicate) and predicate is not None:
        raise TypeError("predicate must be a callable object or None")
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x


class TestFilterFalse(unittest.TestCase):
    def test_filter_false(self):
        data = [0, 1, 2, 3, 4, 5]
        result = list(filterfalse(lambda x: x % 2 == 0, data))
        self.assertEqual(result, [1, 3, 5])

    def test_filter_false_with_none_predicate(self):
        data = [0, 1, 2, 3, 4, 5]
        result = list(filterfalse(None, data))
        self.assertEqual(result, [0])

    def test_filter_false_with_non_callable_predicate(self):
        data = [0, 1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            list(filterfalse(10, data))

    def test_filter_false_with_empty_iterable(self):
        data = []
        result = list(filterfalse(lambda x: x > 0, data))
        self.assertEqual(result, [])

    def test_filter_false_with_non_list_iterable(self):
        data = (0, 1, 2, 3, 4, 5)
        result = list(filterfalse(lambda x: x % 2 == 0, data))
        self.assertEqual(result, [1, 3, 5])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
