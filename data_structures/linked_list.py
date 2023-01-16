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
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, prev_node: Node, data: int) -> None:
        if prev_node is None:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, key: int) -> None:
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def search(self, x: int) -> Node:
        current = self.head
        while current is not None:
            if current.data == x:
                return current
            current = current.next
        return None

    def __getitem__(self, index: int) -> int:
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
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
        res = []
        current = self.head
        while current:
            res.append(str(current.data))
            current = current.next
        return '->'.join(res)

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


if __name__ == '__main__':
    unittest.main()
