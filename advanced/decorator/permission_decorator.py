import unittest
from collections.abc import Callable
from typing import Any


def check_permission(role: str) -> bool:
    """
    Checks if the role has permission.

    Args:
        role (str): The role to be checked.

    Returns:
        bool: True if the role has permission, False otherwise.
    """
    return role.lower() in ["admin", "user"]


def permission(role: str) -> Callable:
    """
    Decorator that checks if the user has the required permission.

    Args:
        role (str): The required role for the permission.

    Returns:
        Callable: The wrapper function that handles the permission check.
    """

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if check_permission(role):
                return func(*args, **kwargs)
            else:
                raise PermissionError("You don't have the permission")

        return wrapper

    return decorator


@permission("admin")
def admin():
    """
    Greets the user with admin role.
    """
    print("Welcome admin")


@permission("user")
def user():
    """
    Greets the user with user role.
    """
    print("Welcome user")


class TestMyFunction(unittest.TestCase):
    def test_permission_admin(self):
        """
        Tests the function with admin permission.
        """
        self.assertEqual(admin(), None)

    def test_permission_user(self):
        """
        Tests the function with user permission.
        """
        self.assertEqual(user(), None)

    def test_permission_error(self):
        """
        Tests the function with an invalid role that raises PermissionError.
        """
        with self.assertRaises(PermissionError):

            @permission("guest")
            def restricted_function():
                pass

            restricted_function()


if __name__ == "__main__":
    unittest.main()
