import unittest
from typing import Any


def singleton(cls: type) -> type:
    instances = {}

    def getinstance(*args: tuple[Any, ...], **kwargs: dict[str, Any]) -> cls:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


@singleton
class MySingletonClass:
    pass


class TestMySingletonClass(unittest.TestCase):
    def test_singleton(self):
        instance1 = MySingletonClass()
        instance2 = MySingletonClass()
        self.assertEqual(instance1, instance2)


if __name__ == '__main__':
    unittest.main()
