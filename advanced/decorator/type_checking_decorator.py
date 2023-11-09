import unittest
from collections.abc import Callable
from typing import Any


def type_check(func: Callable) -> Callable:
    """
    Decorator that checks the types of arguments based on function annotations.

    Args:
        func (Callable): The function to be checked.

    Returns:
        Callable: The wrapper function that performs the type checking.
    """

    def wrapper(*args: tuple[Any, ...], **kwargs: Any) -> Any:
        for i, (arg, arg_type) in enumerate(zip(args, func.__annotations__.values())):
            if not isinstance(arg, arg_type):
                raise TypeError(
                    f"Argument {i+1} of {func.__name__} should be {arg_type},\
                         not {type(arg)}"
                )
        return func(*args, **kwargs)

    return wrapper


@type_check
def my_function(a: int, b: str) -> str:
    """
    A function that concatenates an integer and a string.

    Args:
        a (int): The first integer argument.
        b (str): The second string argument.

    Returns:
        str: The concatenated string of the integer and the string.
    """

    return f"{a} and {b}"


class TestTypeCheck(unittest.TestCase):
    def test_valid_arguments(self):
        """
        Tests the function with valid arguments.
        """
        result = my_function(1, "hello")
        self.assertEqual(result, "1 and hello")

    def test_invalid_arguments(self):
        """
        Tests the function with invalid arguments that raise TypeError.
        """
        with self.assertRaises(TypeError):
            my_function(1, 2)


if __name__ == "__main__":
    unittest.main()
