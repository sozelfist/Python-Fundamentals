import unittest


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, prev_node: Node, data: int) -> None:
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, key: int) -> None:
        if not self.head:
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != key:
            current = current.next

        if current.next:
            current.next = current.next.next

    def search(self, x: int) -> Node | None:
        current = self.head
        while current:
            if current.data == x:
                return current
            current = current.next
        return None

    def __getitem__(self, index: int) -> int:
        current = self.head
        for _i in range(index):
            if not current:
                raise IndexError("Index out of range")
            current = current.next

        if not current:
            raise IndexError("Index out of range")

        return current.data

    def __len__(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self) -> str:
        if not self.head:
            return ""

        res = []
        current = self.head
        while current:
            res.append(str(current.data))
            current = current.next
        return "->".join(res)

    def __repr__(self) -> str:
        return self.__str__()


class TestLinkedList(unittest.TestCase):
    def test_append(self):
        my_linked_list = LinkedList()
        my_linked_list.append(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        self.assertEqual(str(my_linked_list), "1->2->3")
        self.assertEqual(len(my_linked_list), 3)

    def test_insert(self):
        my_linked_list = LinkedList()
        my_linked_list.append(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.insert(my_linked_list.search(2), 4)
        self.assertEqual(str(my_linked_list), "1->2->4->3")
        self.assertEqual(len(my_linked_list), 4)

    def test_delete(self):
        my_linked_list = LinkedList()
        my_linked_list.append(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.delete(2)
        self.assertEqual(str(my_linked_list), "1->3")
        self.assertEqual(len(my_linked_list), 2)

    def test_search(self):
        my_linked_list = LinkedList()
        my_linked_list.append(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        self.assertEqual(my_linked_list.search(2).data, 2)
        self.assertEqual(my_linked_list.search(4), None)

    def test_indexing(self):
        my_linked_list = LinkedList()
        my_linked_list.append(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        self.assertEqual(my_linked_list[0], 1)
        self.assertEqual(my_linked_list[1], 2)
        self.assertEqual(my_linked_list[2], 3)
        with self.assertRaises(IndexError):
            my_linked_list[3]


if __name__ == "__main__":
    unittest.main()
