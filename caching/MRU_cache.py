import unittest
from typing import TypeVar

K = TypeVar("K")
V = TypeVar("V")


class MRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[K, tuple[V, int]] = {}
        self.accessed: list[K] = []

    def get(self, key: K) -> V:
        if key in self.cache:
            value, timestamp = self.cache[key]
            self.accessed.remove(key)
            self.accessed.insert(0, key)
            self.cache[key] = (value, timestamp + 1)
            return value
        else:
            raise KeyError("Key not found in cache")

    def put(self, key: K, value: V) -> None:
        if key in self.cache:
            self.accessed.remove(key)
            self.accessed.insert(0, key)
            self.cache[key] = (value, 0)
        else:
            if len(self.cache) >= self.capacity:
                lru_key = self.accessed.pop()
                del self.cache[lru_key]
            self.accessed.insert(0, key)
            self.cache[key] = (value, 0)


class TestMRUCache(unittest.TestCase):
    def test_get_and_put(self):
        cache = MRUCache(3)
        cache.put("key1", "value1")
        cache.put("key2", "value2")
        cache.put("key3", "value3")
        self.assertEqual(cache.get("key1"), "value1")
        cache.put("key4", "value4")
        self.assertRaises(KeyError, cache.get, "key2")

    def test_capacity(self):
        cache = MRUCache(3)
        cache.put("key1", "value1")
        cache.put("key2", "value2")
        cache.put("key3", "value3")
        cache.put("key4", "value4")
        self.assertRaises(KeyError, cache.get, "key1")

    def test_timestamp(self):
        cache = MRUCache(3)
        cache.put("key1", "value1")
        cache.put("key2", "value2")
        cache.put("key3", "value3")
        cache.get("key1")
        cache.put("key4", "value4")
        self.assertRaises(KeyError, cache.get, "key2")
        self.assertEqual(cache.get("key1"), "value1")
        self.assertEqual(cache.get("key4"), "value4")


if __name__ == "__main__":
    unittest.main()
