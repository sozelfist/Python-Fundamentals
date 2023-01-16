import unittest
import random
from typing import Union


class Node:
    def __init__(self, key: int, value: int, level: int):
        self.key = key
        self.value = value
        self.next = [None] * level


class SkipList:
    def __init__(self, max_level: int = 16):
        self.max_level = max_level
        self.level = 0
        self.head = Node(float('-inf'), None, max_level)

    def _random_level(self) -> int:
        level = 0
        while random.random() < 0.5 and level < self.max_level - 1:
            level += 1
        return level

    def search(self, key: int) -> Union[int, None]:
        curr = self.head
        for i in range(self.level, -1, -1):
            while curr.next[i] and curr.next[i].key < key:
                curr = curr.next[i]
        if curr.next[0] and curr.next[0].key == key:
            return curr.next[0].value
        return None

    def insert(self, key: int, value: int) -> None:
        update = [self.head] * (self.max_level)
        curr = self.head
        for i in range(self.level, -1, -1):
            while curr.next[i] and curr.next[i].key < key:
                curr = curr.next[i]
            update[i] = curr
        curr = curr.next[0]
        if curr and curr.key == key:
            curr.value = value
        else:
            new_level = self._random_level()
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.head
                self.level = new_level
            curr = Node(key, value, new_level + 1)
            for i in range(new_level + 1):
                curr.next[i] = update[i].next[i]
                update[i].next[i] = curr

    def delete(self, key: int) -> None:
        update = [self.head] * (self.max_level)
        curr = self.head
        for i in range(self.level, -1, -1):
            while curr.next[i] and curr.next[i].key < key:
                curr = curr.next[i]
            update[i] = curr
        curr = curr.next[0]
        if curr and curr.key == key:
            for i in range(self.level + 1):
                if update[i].next[i] != curr:
                    break
                update[i].next[i] = curr.next[i]
            while self.level > 0 and self.head.next[self.level] is None:
                self.level -= 1

    def __str__(self) -> str:
        res = []
        curr = self.head.next[0]
        while curr:
            res.append(f"({curr.key}, {curr.value})")
            curr = curr.next[0]
        return ' -> '.join(res)


class TestSkipList(unittest.TestCase):
    def setUp(self) -> None:
        self.skip_list = SkipList()

    def test_insert(self):
        self.skip_list.insert(2, 20)
        self.skip_list.insert(3, 30)
        self.skip_list.insert(1, 10)
        self.assertEqual(str(self.skip_list), "(1, 10) -> (2, 20) -> (3, 30)")

    def test_search(self):
        self.skip_list.insert(2, 20)
        self.skip_list.insert(3, 30)
        self.skip_list.insert(1, 10)
        self.assertEqual(self.skip_list.search(2), 20)
        self.assertEqual(self.skip_list.search(3), 30)
        self.assertEqual(self.skip_list.search(1), 10)
        self.assertEqual(self.skip_list.search(4), None)

    def test_delete(self):
        self.skip_list.insert(2, 20)
        self.skip_list.insert(3, 30)
        self.skip_list.insert(1, 10)
        self.skip_list.delete(2)
        self.assertEqual(str(self.skip_list), "(1, 10) -> (3, 30)")
        self.skip_list.delete(3)
        self.assertEqual(str(self.skip_list), "(1, 10)")
        self.skip_list.delete(1)
        self.assertEqual(str(self.skip_list), "")


if __name__ == '__main__':
    unittest.main()
