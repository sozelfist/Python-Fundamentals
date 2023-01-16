from typing import Type, Union, List
import unittest


class HashTable:
    def __init__(self, size: int) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.load_factor = 0

    def _hash_function(self, key: Union[str, int]) -> int:
        """Hash function to map a key to an index in the array"""
        if isinstance(key, int):
            return key % self.size
        else:
            return sum([ord(char) for char in key]) % self.size

    def insert(self, key: Union[str, int], value: Type) -> None:
        """Insert a key-value pair into the hash table"""
        index = self._hash_function(key)
        self.table[index].append((key, value))
        self.load_factor += 1
        if self.load_factor / self.size > 0.75:
            self._resize()

    def _resize(self):
        self.size = self.size * 2
        temp = self.table
        self.table = [[] for _ in range(self.size)]
        self.load_factor = 0
        for bucket in temp:
            for k, v in bucket:
                self.insert(k, v)

    def search(self, key: Union[str, int]) -> Type:
        """Search for a value associated with a key in the hash table"""
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key: Union[str, int]) -> None:
        """Delete a key-value pair from the hash table"""
        index = self._hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.load_factor -= 1
            return

    def get(self, key: Union[str, int]) -> Type:
        """Get the value associated with a key in the hash table, raise an exception if the key is not found"""
        value = self.search(key)
        if value:
            return value
        else:
            raise KeyError(f"Key {key} not found in the Hash Table")

    def keys(self) -> List[Union[str, int]]:
        """Return all the keys in the hash table"""
        keys = []
        for bucket in self.table:
            for k, v in bucket:
                keys.append(k)
        return keys

    def values(self) -> List[Type]:
        """Return all the values in the hash table"""
        values = []
        for bucket in self.table:
            for k, v in bucket:
                values.append(v)
        return values


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(10)

    def test_insert(self):
        self.ht.insert(5, "apple")
        self.ht.insert(14, "banana")
        self.ht.insert(23, "cherry")
        self.ht.insert(32, "date")
        self.assertEqual(self.ht.table[5], [(5, "apple")])
        self.assertEqual(self.ht.table[4], [(14, "banana")])
        self.assertEqual(self.ht.table[3], [(23, "cherry")])
        self.assertEqual(self.ht.table[2], [(32, "date")])

    def test_search(self):
        self.ht.insert(5, "apple")
        self.ht.insert(14, "banana")
        self.ht.insert(23, "cherry")
        self.ht.insert(32, "date")
        self.assertEqual(self.ht.search(5), "apple")
        self.assertEqual(self.ht.search(14), "banana")
        self.assertEqual(self.ht.search(23), "cherry")
        self.assertEqual(self.ht.search(32), "date")
        self.assertIsNone(self.ht.search(31))

    def test_delete(self):
        self.ht.insert(5, "apple")
        self.ht.insert(14, "banana")
        self.ht.insert(23, "cherry")
        self.ht.insert(32, "date")
        self.ht.delete(14)
        self.assertEqual(self.ht.table[5], [(5, "apple")])
        self.assertEqual(self.ht.table[4], [])
        self.assertEqual(self.ht.table[3], [(23, "cherry")])
        self.assertEqual(self.ht.table[2], [(32, "date")])

    def test_get(self):
        self.ht.insert(5, "apple")
        self.ht.insert(14, "banana")
        self.ht.insert(23, "cherry")
        self.ht.insert(32, "date")
        self.assertEqual(self.ht.get(5), "apple")
        self.assertEqual(self.ht.get(14), "banana")
        self.assertEqual(self.ht.get(23), "cherry")
        self.assertEqual(self.ht.get(32), "date")
        with self.assertRaises(KeyError):
            self.ht.get(31)

    def test_keys(self):
        self.ht.insert(5, "apple")
        self.ht.insert(14, "banana")
        self.ht.insert(23, "cherry")
        self.ht.insert(32, "date")
        self.assertEqual(self.ht.keys(), [32, 23, 14, 5])

    def test_values(self):
        self.ht.insert(5, "apple")
        self.ht.insert(14, "banana")
        self.ht.insert(23, "cherry")
        self.ht.insert(32, "date")
        self.assertEqual(self.ht.values(), ['date', 'cherry', 'banana', 'apple'])


if __name__ == '__main__':
    unittest.main()
