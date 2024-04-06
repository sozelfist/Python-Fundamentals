import operator
import unittest
from itertools import islice


def accumulate(iterable, func=operator.add, *, initial=None, start=None, stop=None):
    """
    Return an iterator that generates the running totals of elements
    in the input iterable. If the iterable is empty, an empty
    iterator is returned.

    The optional `func` argument specifies a binary function that
    is used to accumulate the elements. If not specified, the `+`
    operator is used by default.

    The optional `initial` argument specifies the initial value
    of the total. If not specified, the first element of the
    iterable is used as the initial value.

    The optional `start` and `stop` arguments specify the indices
    of the elements to accumulate. If not specified, all elements
    of the iterable  are accumulated.

    If any element in the iterable cannot be processed by the `func`
    function (e.g., due to being of a different type), a TypeError
    is raised.

    Examples:
    ----------
    >>> list(accumulate([1, 2, 3, 4, 5]))
    [1, 3, 6, 10, 15]

    >>> list(accumulate([1, 2, 3, 4, 5], initial=100))
    [100, 101, 103, 106, 110, 115]

    >>> list(accumulate([1, 2, 3, 4, 5], operator.mul))
    [1, 2, 6, 24, 120]

    >>> list(accumulate([], initial=100))
    []

    >>> list(accumulate([1, 2, 'a', 4, 5]))
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

    >>> list(accumulate([1, 2, 3, 4, 5, 6, 7], start=1, stop=6))
    [2, 5, 9, 14, 20]
    """
    it = islice(iterable, start, stop)
    if not it:
        return iter(())
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        try:
            total = func(total, element)
        except TypeError:
            raise TypeError(
                f"unsupported operand type(s) for {func.__name__}: \
                        '{type(total).__name__}' and '{type(element).__name__}'"
            )
        yield total


class TestAccumulate(unittest.TestCase):
    def test_empty_iterable(self):
        self.assertEqual(list(accumulate([])), [])

    def test_different_types(self):
        with self.assertRaises(TypeError):
            list(accumulate(["a", 1, {}]))

    def test_start_and_end_indices(self):
        self.assertEqual(list(accumulate([1, 2, 3, 4, 5], start=1, stop=3)), [2, 5])

    def test_addition(self):
        self.assertEqual(list(accumulate([1, 2, 3, 4, 5])), [1, 3, 6, 10, 15])

    def test_multiplication(self):
        self.assertEqual(
            list(accumulate([1, 2, 3, 4, 5], func=operator.mul)), [1, 2, 6, 24, 120]
        )

    def test_initial_value(self):
        self.assertEqual(
            list(accumulate([1, 2, 3, 4, 5], initial=100)),
            [100, 101, 103, 106, 110, 115],
        )


if __name__ == "__main__":
    unittest.main()
