import unittest


def compress(data, selectors):
    """Return data elements corresponding to truthy selectors.

    Args:
        data: An iterable of data elements.
        selectors: An iterable of boolean values, 0 or 1.

    Returns:
        An iterator over the elements of `data` corresponding to truthy
        values in `selectors`.

    Raises:
        TypeError: If either `data` or `selectors` is not iterable, or if
            `selectors` contains a non-boolean value.

    Examples:
    >>> list(compress('ABCDEF', [1, 0, 1, 0, 1, 1]))
    ['A', 'C', 'E', 'F']
    >>> list(compress([1, 2, 3], [True, False, True]))
    [1, 3]
    """
    if not isinstance(selectors, (list, tuple)):
        raise TypeError("selectors must be an iterable")
    if not all(isinstance(s, (bool, int)) and s in (0, 1) for s in selectors):
        raise TypeError("selectors must only contain boolean values, 0 or 1")
    return (d for d, s in zip(data, selectors) if s)


class TestCompress(unittest.TestCase):
    def test_compress_with_strings_and_lists(self):
        self.assertEqual(
            list(compress("ABCDEF", [1, 0, 1, 0, 1, 1])), ["A", "C", "E", "F"]
        )
        self.assertEqual(list(compress([1, 2, 3], [True, False, True])), [1, 3])
        self.assertEqual(list(compress("hello", [0, 1, 1, 0, 1])), ["e", "l", "o"])
        self.assertEqual(list(compress([], [])), [])
        self.assertEqual(list(compress([1, 2, 3], [])), [])
        self.assertEqual(list(compress([], [True, False, True])), [])

    def test_raises_type_error_if_argument_is_not_iterable(self):
        with self.assertRaises(TypeError):
            compress("hello", 1)
        with self.assertRaises(TypeError):
            compress(123, "world")
        with self.assertRaises(TypeError):
            compress(None, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
