import unittest
from collections import OrderedDict


class ARC:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: OrderedDict[str, tuple[int, bool]] = OrderedDict()
        self.t1: OrderedDict[str, None] = OrderedDict()
        self.t2: OrderedDict[str, None] = OrderedDict()
        self.b1: OrderedDict[str, None] = OrderedDict()
        self.b2: OrderedDict[str, None] = OrderedDict()

    def __getitem__(self, key: str) -> str:
        value, is_ghost = self.cache[key]
        if not is_ghost:
            del self.cache[key]
            self.t2[key] = None
            self._adjust()
            self.cache[key] = (value, True)
        return value

    def __setitem__(self, key: str, value: str) -> None:
        if key in self.cache:
            self.cache[key] = (value, False)
            self._adjust()
        else:
            if len(self.cache) >= self.capacity:
                if self.b1:
                    key_to_remove, _ = self.b1.popitem(last=False)
                else:
                    key_to_remove, _ = self.t1.popitem(last=False)
                del self.cache[key_to_remove]
            self.cache[key] = (value, False)
            self.t1[key] = None
            self._adjust()

    def __delitem__(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]
            if key in self.t1:
                del self.t1[key]
            elif key in self.t2:
                del self.t2[key]
            elif key in self.b1:
                del self.b1[key]
            elif key in self.b2:
                del self.b2[key]

    def __len__(self) -> int:
        return len(self.cache)

    def _adjust(self) -> None:
        while len(self.t1) + len(self.b1) > self.capacity:
            if len(self.b1) > 0:
                key_to_remove, _ = self.b1.popitem(last=True)
            else:
                key_to_remove, _ = self.t1.popitem(last=True)
            del self.cache[key_to_remove]
        while len(self.t1) < min(self.capacity, len(self.cache)):
            if len(self.t2) > 0:
                key_to_move, _ = self.t2.popitem(last=False)
                self.t1[key_to_move] = None
            else:
                break
        while len(self.b1) < len(self.cache) - self.capacity:
            if len(self.b2) > 0:
                key_to_move, _ = self.b2.popitem(last=False)
                self.b1[key_to_move] = None
            else:
                break
        while len(self.t2) > 0 and len(self.t1) + len(self.b1) < self.capacity:
            key_to_move, _ = self.t2.popitem(last=True)
            self.b2[key_to_move] = None
        while len(self.b2) > 0 and len(self.t1) + len(self.b1) < self.capacity:
            key_to_move, _ = self.b2.popitem(last=True)
            self.t2[key_to_move] = None


class TestARCCache(unittest.TestCase):
    def setUp(self):
        self.cache = ARC(3)

    def test_add_and_retrieve_items(self):
        self.cache["a"] = "1"
        self.cache["b"] = "2"
        self.cache["c"] = "3"
        self.assertEqual(self.cache["a"], "1")
        self.assertEqual(self.cache["b"], "2")
        self.assertEqual(self.cache["c"], "3")

    def test_eviction(self):
        self.cache["a"] = "1"
        self.cache["b"] = "2"
        self.cache["c"] = "3"
        self.cache["d"] = "4"
        with self.assertRaises(KeyError):
            self.cache["a"]
        self.assertEqual(self.cache["b"], "2")
        self.assertEqual(self.cache["c"], "3")
        self.assertEqual(self.cache["d"], "4")

    def test_ghost_items(self):
        self.cache["a"] = "1"
        self.cache["b"] = "2"
        self.cache["c"] = "3"
        self.cache["a"] = "-1"
        self.cache["d"] = "4"
        with self.assertRaises(KeyError):
            self.cache["a"]
        self.assertEqual(self.cache["c"], "3")
        self.assertEqual(self.cache["d"], "4")

    def test_overwrite_existing_item(self):
        self.cache["a"] = "1"
        self.cache["b"] = "2"
        self.cache["a"] = "3"
        self.assertEqual(self.cache["a"], "3")
        self.assertEqual(self.cache["b"], "2")

    def test_remove_item(self):
        self.cache["a"] = "1"
        self.cache["b"] = "2"
        del self.cache["a"]
        with self.assertRaises(KeyError):
            self.cache["a"]
        self.assertEqual(self.cache["b"], "2")

    def test_cache_size(self):
        self.assertEqual(len(self.cache), 0)
        self.cache["a"] = "1"
        self.assertEqual(len(self.cache), 1)
        self.cache["b"] = "2"
        self.assertEqual(len(self.cache), 2)
        self.cache["c"] = "3"
        self.assertEqual(len(self.cache), 3)
        self.cache["d"] = "4"
        self.assertEqual(len(self.cache), 3)
        del self.cache["d"]
        self.assertEqual(len(self.cache), 2)
        del self.cache["c"]
        self.assertEqual(len(self.cache), 1)
        del self.cache["b"]
        self.assertEqual(len(self.cache), 0)


if __name__ == "__main__":
    unittest.main()
