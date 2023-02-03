import unittest
from typing import Any, Tuple, Callable


def cache(func: Callable) -> Callable:
    def wrapper(*args: Tuple[Any, ...]):
        if args not in wrapper.cache:
            wrapper.cache[args] = func(*args)
        return wrapper.cache[args]
    wrapper.cache = {}
    return wrapper


@cache
def my_function(x: int) -> int:
    print("computing")
    return x * x


class TestMyFunction(unittest.TestCase):
    def test_cache(self):
        # First call to my_function should print "computing" and add the result to the cache
        self.assertEqual(my_function(2), 4)
        self.assertEqual(my_function.cache, {(2,): 4})

        # Second call to my_function with the same argument should return the cached result without computing again
        self.assertEqual(my_function(2), 4)
        self.assertEqual(my_function.cache, {(2,): 4})

        # Call to my_function with a different argument should add a new entry to the cache
        self.assertEqual(my_function(3), 9)
        self.assertEqual(my_function.cache, {(2,): 4, (3,): 9})


if __name__ == '__main__':
    unittest.main()
