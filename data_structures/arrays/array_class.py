import unittest


class Array:
    def __init__(self, capacity: int = 10):
        self.data = [0] * capacity
        self.size = 0
        self.capacity = capacity

    def append(self, value: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

    def insert(self, index: int, value: int) -> None:
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def delete(self, index: int) -> None:
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1

    def resize(self) -> None:
        self.capacity *= 2
        new_data = [0] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def __getitem__(self, index: int) -> int:
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        return self.data[index]

    def __setitem__(self, index: int, value: int) -> None:
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        self.data[index] = value

    def __len__(self) -> int:
        return self.size


class TestArray(unittest.TestCase):
    def test_append(self):
        my_array = Array()
        my_array.append(1)
        my_array.append(2)
        my_array.append(3)
        self.assertEqual(my_array[0], 1)
        self.assertEqual(my_array[1], 2)
        self.assertEqual(my_array[2], 3)
        self.assertEqual(len(my_array), 3)

    def test_insert(self):
        my_array = Array()
        my_array.append(1)
        my_array.append(2)
        my_array.append(3)
        my_array.insert(1, 4)
        self.assertEqual(my_array[0], 1)
        self.assertEqual(my_array[1], 4)
        self.assertEqual(my_array[2], 2)
        self.assertEqual(my_array[3], 3)
        self.assertEqual(len(my_array), 4)

    def test_delete(self):
        my_array = Array()
        my_array.append(1)
        my_array.append(2)
        my_array.append(3)
        my_array.delete(1)
        self.assertEqual(my_array[0], 1)
        self.assertEqual(my_array[1], 3)
        self.assertEqual(len(my_array), 2)

    def test_indexing(self):
        my_array = Array()
        my_array.append(1)
        my_array.append(2)
        my_array[0] = 3
        self.assertEqual(my_array[0], 3)
        self.assertEqual(my_array[1], 2)
        self.assertEqual(len(my_array), 2)

    def test_out_of_range(self):
        my_array = Array()
        my_array.append(1)
        my_array.append(2)
        with self.assertRaises(IndexError):
            my_array[2]
        with self.assertRaises(IndexError):
            my_array[-1]

    def test_resize(self):
        my_array = Array(2)
        my_array.append(1)
        my_array.append(2)
        my_array.append(3)
        self.assertEqual(my_array.capacity, 4)


if __name__ == "__main__":
    unittest.main()
