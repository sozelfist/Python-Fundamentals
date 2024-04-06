import unittest


def dropwhile(predicate, iterable):
    """Return elements of `iterable` after predicate is False.

    Args:
        predicate: A function that takes an element of `iterable` as its
            argument and returns a boolean value.
        iterable: An iterable sequence of elements.

    Returns:
        An iterator over the elements of `iterable` that come after the
        first element for which `predicate` returns False.

    Raises:
        TypeError: If `predicate` is not callable, or if `iterable` is
            not iterable.
    """
    if not callable(predicate):
        raise TypeError("predicate must be callable")
    try:
        it = iter(iterable)
    except TypeError:
        raise TypeError("iterable must be iterable")
    for x in it:
        if not predicate(x):
            yield x
            break
    for x in it:
        yield x


class TestDropwhile(unittest.TestCase):
    def test_dropwhile_returns_expected_output(self):
        iterable = [1, 4, 6, 4, 1]

        def first_predicate(x):
            return x < 5

        expected_output = [6, 4, 1]
        self.assertEqual(list(dropwhile(first_predicate, iterable)), expected_output)

        iterable = [1, 2, 3, 4, 5]

        def second_predicate(x):
            return x < 3

        expected_output = [3, 4, 5]
        self.assertEqual(list(dropwhile(second_predicate, iterable)), expected_output)

        iterable = ["apple", "banana", "cherry"]

        def third_predicate(x):
            return len(x) < 6

        expected_output = ["banana", "cherry"]
        self.assertEqual(list(dropwhile(third_predicate, iterable)), expected_output)

    def test_dropwhile_raises_type_error_if_predicate_not_callable(self):
        with self.assertRaises(TypeError):
            list(dropwhile("not callable", [1, 2, 3]))

    def test_dropwhile_raises_type_error_if_iterable_not_iterable(self):
        with self.assertRaises(TypeError):
            list(dropwhile(lambda x: x < 5, 123))


if __name__ == "__main__":
    unittest.main()
