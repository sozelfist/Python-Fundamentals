import unittest
from typing import Any


def namedtuple(classname: str, fieldnames: str) -> Any:
    class _NamedTuple:
        __slots__ = fieldnames.split()

        def __init__(self, *args: tuple) -> None:
            if len(args) != len(self.__slots__):
                raise TypeError(f"{len(self.__slots__)} arguments required")
            for name, value in zip(self.__slots__, args):
                setattr(self, name, value)

        def __repr__(self) -> str:
            values = ", ".join(f"{name}={getattr(self, name)}" for name in self.__slots__)
            return f"{self.__class__.__name__}({values})"

        def __eq__(self, other: Any) -> bool:
            if not isinstance(other, self.__class__):
                return False
            return all(getattr(self, name) == getattr(other, name) for name in self.__slots__)

        def __iter__(self):
            return iter(getattr(self, name) for name in self.__slots__)

        def __getitem__(self, index: int) -> Any:
            return getattr(self, self.__slots__[index])

        def __len__(self) -> int:
            return len(self.__slots__)

    return type(classname, (_NamedTuple,), {"__doc__": f"{classname}({fieldnames})"})


class TestNamedtuple(unittest.TestCase):
    def test_create_namedtuple(self):
        Person = namedtuple("Person", "name age")
        p1 = Person("Alice", 25)
        self.assertEqual(p1.name, "Alice")
        self.assertEqual(p1.age, 25)

    def test_repr(self):
        Person = namedtuple("Person", "name age")
        p1 = Person("Alice", 25)
        self.assertEqual(repr(p1), "Person(name=Alice, age=25)")

    def test_eq(self):
        Person = namedtuple("Person", "name age")
        p1 = Person("Alice", 25)
        p2 = Person("Bob", 30)
        self.assertEqual(p1 == p2, False)
        self.assertEqual(p1 == Person("Alice", 25), True)

    def test_iter(self):
        Person = namedtuple("Person", "name age")
        p1 = Person("Alice", 25)
        values = [value for value in p1]
        self.assertEqual(values, ["Alice", 25])

    def test_getitem(self):
        Person = namedtuple("Person", "name age")
        p1 = Person("Alice", 25)
        self.assertEqual(p1[0], "Alice")
        self.assertEqual(p1[1], 25)

    def test_len(self):
        Person = namedtuple("Person", "name age")
        p1 = Person("Alice", 25)
        self.assertEqual(len(p1), 2)

    def test_create_with_wrong_number_of_arguments(self):
        Person = namedtuple("Person", "name age")
        with self.assertRaises(TypeError):
            Person("Alice")  # Should raise TypeError
        with self.assertRaises(TypeError):
            Person("Alice", 25, "female")  # Should raise TypeError


if __name__ == '__main__':
    unittest.main()
