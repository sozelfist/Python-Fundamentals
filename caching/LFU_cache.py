from typing import Dict, List, Tuple, Optional
import unittest


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: Dict[int, Tuple[int, int, int]] = {}
        self.frequency: Dict[int, List[int]] = {}
        self.min_frequency = 0

    def get(self, key: int) -> Optional[int]:
        if key in self.cache:
            frequency, value, index = self.cache[key]
            self.frequency[frequency].remove(key)
            if not self.frequency[frequency]:
                del self.frequency[frequency]
                if frequency == self.min_frequency:
                    self.min_frequency += 1
            frequency += 1
            self.frequency.setdefault(frequency, []).append(key)
            self.cache[key] = (frequency, value, index)
            return value
        else:
            return None

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            self.get(key)
            self.cache[key] = (self.cache[key][0], value, self.cache[key][2])
        else:
            if len(self.cache) == self.capacity:
                least_frequent = self.frequency[self.min_frequency][0]
                del self.cache[least_frequent]
                self.frequency[self.min_frequency].remove(least_frequent)
                if not self.frequency[self.min_frequency]:
                    del self.frequency[self.min_frequency]
                self.min_frequency = 1
            self.cache[key] = (1, value, len(self.frequency.setdefault(1, [])))
            self.frequency[1].append(key)
            self.min_frequency = 1


class TestLFUCache(unittest.TestCase):
    def test_put_get(self):
        cache = LFUCache(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)

    def test_eviction(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(3, 3)
        self.assertIsNone(cache.get(2))
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(3), 3)

    def test_repeated_access(self):
        cache = LFUCache(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.get(2)
        cache.put(3, 3)
        cache.get(3)
        cache.put(4, 4)
        self.assertIsNone(cache.get(1))
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_capacity_zero(self):
        cache = LFUCache(0)
        cache.put(1, 1)
        self.assertIsNone(cache.get(1))


if __name__ == '__main__':
    unittest.main()
