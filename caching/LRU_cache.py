import unittest


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: dict[int, tuple[int, int]] = {}
        self.queue: list[int] = []

    def get(self, key: int) -> int | None:
        if key not in self.cache:
            return None

        # Move key to front of queue
        self.queue.remove(key)
        self.queue.insert(0, key)

        # Return value associated with key
        return self.cache[key][1]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move key to front of queue
            self.cache[key] = (self.cache[key][0], value)
            self.queue.remove(key)
            self.queue.insert(0, key)
        else:
            # Add new key-value pair to cache and queue
            self.cache[key] = (len(self.queue), value)
            self.queue.insert(0, key)

            # Evict least recently used item if cache is full
            if len(self.queue) > self.capacity:
                lru_key = self.queue.pop()
                del self.cache[lru_key]


class TestLRUCache(unittest.TestCase):
    def test_capacity_zero(self):
        cache = LRUCache(0)
        self.assertIsNone(cache.get(1))
        cache.put(1, 1)
        self.assertIsNone(cache.get(1))

    def test_capacity_one(self):
        cache = LRUCache(1)
        cache.put(1, 1)
        self.assertEqual(cache.get(1), 1)
        cache.put(2, 2)
        self.assertIsNone(cache.get(1))
        self.assertEqual(cache.get(2), 2)

    def test_capacity_two(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertIsNone(cache.get(2))
        self.assertEqual(cache.get(1), 1)
        cache.put(4, 4)
        self.assertIsNone(cache.get(3))
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(4), 4)

    def test_cache_update(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(2, 3)
        self.assertEqual(cache.get(2), 3)
        cache.put(1, 4)
        self.assertEqual(cache.get(2), 3)
        self.assertEqual(cache.get(1), 4)


if __name__ == '__main__':
    unittest.main()
