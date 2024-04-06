import unittest
from typing import Generic, TypeVar

T = TypeVar("T")


class Bag(Generic[T]):
    def __init__(self):
        self.items: dict[T, int] = {}

    def add(self, item: T) -> None:
        self.items[item] = self.items.get(item, 0) + 1

    def count(self, item: T) -> int:
        return self.items.get(item, 0)

    def __contains__(self, item: T) -> bool:
        return item in self.items

    def __len__(self) -> int:
        return sum(self.items.values())

    def __iter__(self):
        for item, count in self.items.items():
            for _i in range(count):
                yield item


class TestBag(unittest.TestCase):
    def test_add(self):
        bag = Bag[int]()
        bag.add(1)
        bag.add(2)
        bag.add(3)
        self.assertEqual(len(bag), 3)

    def test_count(self):
        bag = Bag[int]()
        bag.add(1)
        bag.add(2)
        bag.add(3)
        bag.add(2)
        bag.add(1)
        self.assertEqual(bag.count(1), 2)
        self.assertEqual(bag.count(2), 2)
        self.assertEqual(bag.count(3), 1)
        self.assertEqual(bag.count(4), 0)

    def test_contains(self):
        bag = Bag[int]()
        bag.add(1)
        bag.add(2)
        bag.add(3)
        self.assertTrue(2 in bag)
        self.assertFalse(4 in bag)

    def test_iter(self):
        bag = Bag[int]()
        bag.add(1)
        bag.add(2)
        bag.add(3)
        bag.add(2)
        bag.add(1)
        self.assertEqual(list(bag), [1, 1, 2, 2, 3])


if __name__ == "__main__":
    unittest.main()
