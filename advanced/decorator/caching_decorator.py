import unittest
from collections.abc import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    """
    A decorator that caches the results of the decorated function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The wrapper function that handles caching.
    """

    def wrapper(*args: tuple[Any, ...]) -> Any:
        if args not in wrapper.cache:
            wrapper.cache[tuple(args)] = func(*args)
        return wrapper.cache[tuple(args)]

    wrapper.cache: dict[tuple, Any] = {}
    return wrapper


@cache
def my_function(x: int) -> int:
    """
    Computes the square of the input.

    Args:
        x (int): The input integer.

    Returns:
        int: The square of the input.
    """

    print("computing")
    return x * x


class TestMyFunction(unittest.TestCase):
    def test_cache(self):
        # First call to my_function should print
        # "computing" and add the result to the cache
        self.assertEqual(my_function(2), 4)
        self.assertEqual(my_function.cache, {(2,): 4})

        # Second call to my_function with the same argument
        # should return the cached result without computing again
        self.assertEqual(my_function(2), 4)
        self.assertEqual(my_function.cache, {(2,): 4})

        # Call to my_function with a different argument should
        # add a new entry to the cache
        self.assertEqual(my_function(3), 9)
        self.assertEqual(my_function.cache, {(2,): 4, (3,): 9})


if __name__ == "__main__":
    unittest.main()
