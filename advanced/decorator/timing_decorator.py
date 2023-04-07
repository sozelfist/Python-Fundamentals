import time
import unittest
from collections.abc import Callable
from typing import Any


def time_it(func: Callable) -> Callable:
    def wrapper(*args: tuple[Any, ...], **kwargs: dict[str, Any]):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} took {end_time - start_time:.2f} seconds')
        return result
    return wrapper


@time_it
def my_function():
    time.sleep(2)


class TestMyFunction(unittest.TestCase):
    def test_time_it(self):
        start_time = time.time()
        my_function()
        end_time = time.time()
        self.assertAlmostEqual(end_time - start_time, 2, delta=0.1)


if __name__ == '__main__':
    unittest.main()
