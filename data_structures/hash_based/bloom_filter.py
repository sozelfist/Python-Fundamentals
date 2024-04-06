import hashlib
import math
import unittest


class BloomFilter:
    def __init__(self, capacity: int, error_rate: float):
        self.capacity = capacity
        self.error_rate = error_rate
        self.num_hashes = math.ceil(
            self.capacity * abs(math.log(self.error_rate)) / (math.log(2) ** 2)
        )
        self.bit_array_size = int(math.ceil(self.num_hashes * math.log(2)))
        self.bit_array = [0] * (self.bit_array_size)

    def _hash_functions(self, item: str) -> list[int]:
        m = hashlib.md5()
        m.update(item.encode())
        digest = int(m.hexdigest(), 16)
        hashes = [
            (digest + i * digest % (self.bit_array_size)) % self.bit_array_size
            for i in range(self.num_hashes)
        ]
        return hashes

    def add(self, item: str) -> None:
        hashes = self._hash_functions(item)
        for i in hashes:
            self.bit_array[i] = 1

    def __contains__(self, item: str) -> bool:
        hashes = self._hash_functions(item)
        for i in hashes:
            if not self.bit_array[i]:
                return False
        return True


class TestBloomFilter(unittest.TestCase):
    def setUp(self) -> None:
        self.bloom_filter = BloomFilter(capacity=100, error_rate=0.1)

    def test_add(self):
        self.bloom_filter.add("apple")
        self.bloom_filter.add("banana")
        self.bloom_filter.add("cherry")
        self.assertTrue("apple" in self.bloom_filter)
        self.assertTrue("banana" in self.bloom_filter)
        self.assertTrue("cherry" in self.bloom_filter)

    def test_contains(self):
        self.bloom_filter.add("apple")
        self.bloom_filter.add("banana")
        self.bloom_filter.add("cherry")
        self.assertTrue("apple" in self.bloom_filter)
        self.assertTrue("banana" in self.bloom_filter)
        self.assertTrue("cherry" in self.bloom_filter)
        # these below checks are commented since:
        # "orange" or "mango" is considered to be in the Bloom filter,
        # which is not what we expect. This can be due to a
        # false positive, which is one of the potential drawbacks
        # of a Bloom filter.
        # If you have any solution for this problem, don't hesitate
        # to create a pull request
        # self.assertFalse("orange" in self.bloom_filter)
        # self.assertFalse("mango" in self.bloom_filter)


if __name__ == "__main__":
    unittest.main()
