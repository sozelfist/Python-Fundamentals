import unittest
from typing import Any, Callable, Dict, Tuple, Union


def check_permission(role: str) -> bool:
    return True if role.lower() in ['admin', 'user'] else False


def permission(role: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Union[Any, Tuple[Any, ...]], **kwargs: Dict[str, Any]) -> Any:
            if check_permission(role):
                return func(*args, **kwargs)
            else:
                raise PermissionError("you don't have the permission")
        return wrapper
    return decorator


@permission("admin")
def admin():
    print("Welcome admin")


@permission("user")
def user():
    print("Welcome user")


class TestMyFunction(unittest.TestCase):
    def test_permission_admin(self):
        self.assertEqual(admin(), None)

    def test_permission_user(self):
        self.assertEqual(user(), None)

    def test_permission_error(self):
        with self.assertRaises(PermissionError):
            @permission("guest")
            def restricted_function():
                pass

            restricted_function()


if __name__ == '__main__':
    unittest.main()
