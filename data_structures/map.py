from typing import TypeVar, Generic, Tuple, Optional, List, Hashable
import unittest


K = TypeVar('K')  # Key type
V = TypeVar('V')  # Value type


class Map(Generic[K, V]):
    def __init__(self):
        self._map: List[Tuple[K, V]] = []

    def __getitem__(self, key: K) -> Optional[V]:
        for k, v in self._map:
            if k == key:
                return v
        return None

    def __setitem__(self, key: K, value: V) -> None:
        if not isinstance(key, Hashable):
            raise TypeError(f"Key must be hashable: {key!r}")
        for i, (k, v) in enumerate(self._map):
            if k == key:
                self._map[i] = (key, value)
                return
        self._map.append((key, value))

    def __delitem__(self, key: K) -> None:
        for i, (k, v) in enumerate(self._map):
            if k == key:
                del self._map[i]
                return
        raise KeyError(key)

    def __len__(self) -> int:
        return len(self._map)

    def __iter__(self):
        for item in self._map:
            yield item

    def __str__(self) -> str:
        return "{" + ", ".join([f"{k}: {v}" for k, v in self._map]) + "}"

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        """
        Return the value for key if key is in the dictionary, else default.
        """
        for k, v in self._map:
            if k == key:
                return v
        return default

    def keys(self) -> List[K]:
        """
        Return a list of all the keys in the dictionary.
        """
        return [k for k, _ in self._map]

    def values(self) -> List[V]:
        """
        Return a list of all the values in the dictionary.
        """
        return [v for _, v in self._map]

    def items(self) -> List[Tuple[K, V]]:
        """
        Return a list of all the key-value pairs in the dictionary.
        """
        return list(self._map)

    def clear(self) -> None:
        """
        Remove all items from the dictionary.
        """
        self._map.clear()


class MapTestCase(unittest.TestCase):
    def setUp(self):
        self.m = Map()
        self.m['a'] = 1
        self.m['b'] = 2
        self.m['c'] = 3

    def test_get_item(self):
        self.assertEqual(self.m['a'], 1)
        self.assertEqual(self.m['b'], 2)
        self.assertEqual(self.m['c'], 3)
        self.assertIsNone(self.m.get('d'))

    def test_set_item(self):
        self.m['d'] = 4
        self.assertEqual(len(self.m), 4)
        self.assertEqual(self.m['d'], 4)
        self.m['a'] = 5
        self.assertEqual(len(self.m), 4)
        self.assertEqual(self.m['a'], 5)

    def test_del_item(self):
        del self.m['b']
        self.assertEqual(len(self.m), 2)
        self.assertIsNone(self.m.get('b'))
        with self.assertRaises(KeyError):
            del self.m['d']

    def test_len(self):
        self.assertEqual(len(self.m), 3)
        self.m.clear()
        self.assertEqual(len(self.m), 0)

    def test_iter(self):
        keys = set(['a', 'b', 'c'])
        for k, v in self.m:
            self.assertIn(k, keys)

    def test_str(self):
        self.assertEqual(str(self.m), '{a: 1, b: 2, c: 3}')

    def test_get(self):
        self.assertEqual(self.m.get('a'), 1)
        self.assertEqual(self.m.get('d'), None)
        self.assertEqual(self.m.get('d', 'default'), 'default')

    def test_keys(self):
        self.assertEqual(self.m.keys(), ['a', 'b', 'c'])

    def test_values(self):
        self.assertEqual(self.m.values(), [1, 2, 3])

    def test_items(self):
        self.assertEqual(self.m.items(), [('a', 1), ('b', 2), ('c', 3)])

    def test_clear(self):
        self.m.clear()
        self.assertEqual(len(self.m), 0)
        self.assertEqual(str(self.m), '{}')


if __name__ == '__main__':
    unittest.main()
