import unittest


def chain(*iterables):
    """
    Return a new iterator that concatenates the elements
    of each input iterable.

    The input iterables are not required to have the same
    length or element type. The output iterator returns
    the elements from the first iterable, followed by
    the elements from the second iterable, and so on,
    until all the input iterables have been exhausted.

    If any of the input iterables is empty, it is skipped
    and the next iterable is processed.

    If all the input iterables are empty, an empty iterator is returned.

    If only one iterable is provided, its elements are returned as-is.

    Examples:
    ----------
    >>> list(chain('ABC', 'DEF'))
    ['A', 'B', 'C', 'D', 'E', 'F']

    >>> list(chain(range(3), ['a', 'b', 'c'], [1.0, 2.0, 3.0]))
    [0, 1, 2, 'a', 'b', 'c', 1.0, 2.0, 3.0]

    >>> list(chain([], [1, 2, 3], ['a', 'b'], [4.0, 5.0]))
    [1, 2, 3, 'a', 'b', 4.0, 5.0]

    >>> list(chain())
    []

    >>> list(chain('ABC'))
    ['A', 'B', 'C']

    >>> list(chain(['A'], 'BC', ('D', 'E')))
    ['A', 'B', 'C', 'D', 'E']
    """
    for it in iterables:
        if not hasattr(it, '__iter__'):
            raise TypeError(f"{type(it).__name__} object is not iterable")
        yield from it


class TestChain(unittest.TestCase):
    def test_concatenates_elements_from_multiple_iterables(self):
        self.assertEqual(
            list(chain('ABC', 'DEF')),
            ['A', 'B', 'C', 'D', 'E', 'F']
        )
        self.assertEqual(
            list(chain(range(3), ['a', 'b', 'c'], [1.0, 2.0, 3.0])),
            [0, 1, 2, 'a', 'b', 'c', 1.0, 2.0, 3.0]
        )
        self.assertEqual(
            list(chain([], [1, 2, 3], ['a', 'b'], [4.0, 5.0])),
            [1, 2, 3, 'a', 'b', 4.0, 5.0]
        )
        self.assertEqual(list(chain(['A'], 'BC', ('D', 'E'))), [
                         'A', 'B', 'C', 'D', 'E'])

    def test_skips_empty_iterables(self):
        self.assertEqual(
            list(chain([], 'ABC', [], 'DEF')),
            ['A', 'B', 'C', 'D', 'E', 'F']
        )
        self.assertEqual(list(chain([], [], [], [])), [])
        self.assertEqual(
            list(chain('ABC', [], [], 'DEF')),
            ['A', 'B', 'C', 'D', 'E', 'F']
        )

    def test_returns_single_iterable_as_is(self):
        self.assertEqual(list(chain('ABC')), ['A', 'B', 'C'])
        self.assertEqual(list(chain([])), [])
        self.assertEqual(list(chain(range(3))), [0, 1, 2])

    def test_raises_type_error_if_argument_is_not_iterable(self):
        with self.assertRaises(TypeError):
            list(chain('ABC', None))
        with self.assertRaises(TypeError):
            list(chain('ABC', 1 + 2j))
        with self.assertRaises(TypeError):
            list(chain('ABC', True))


if __name__ == '__main__':
    unittest.main()
