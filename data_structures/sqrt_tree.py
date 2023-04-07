import unittest


class SqrtTree:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr
        self.block_size = int(len(self.arr)**0.5) + 1
        self.blocks = [0] * self.block_size
        for i in range(len(self.arr)):
            self.blocks[i // self.block_size] += self.arr[i]

    def update(self, i: int, val: int) -> None:
        block_idx = i // self.block_size
        self.blocks[block_idx] += val - self.arr[i]
        self.arr[i] = val

    def query(self, l: int, r: int) -> int:
        ans = 0
        l_block = l // self.block_size
        r_block = r // self.block_size
        if l_block == r_block:
            for i in range(l, r + 1):
                ans += self.arr[i]
        else:
            for i in range(l, (l_block + 1) * self.block_size):
                ans += self.arr[i]
            for i in range(l_block + 1, r_block):
                ans += self.blocks[i]
            for i in range(r_block * self.block_size, r + 1):
                ans += self.arr[i]
        return ans


class TestSqrtTree(unittest.TestCase):
    def test_query(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sqrt_tree = SqrtTree(arr)
        self.assertEqual(sqrt_tree.query(2, 5), 18)
        self.assertEqual(sqrt_tree.query(0, 4), 15)
        self.assertEqual(sqrt_tree.query(5, 9), 40)
        self.assertEqual(sqrt_tree.query(0, 9), 55)
        self.assertEqual(sqrt_tree.query(3, 3), 4)

    def test_update(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sqrt_tree = SqrtTree(arr)
        sqrt_tree.update(2, 5)
        self.assertEqual(sqrt_tree.query(2, 5), 20)
        sqrt_tree.update(0, 10)
        self.assertEqual(sqrt_tree.query(0, 4), 26)
        sqrt_tree.update(5, 0)
        self.assertEqual(sqrt_tree.query(5, 9), 34)
        sqrt_tree.update(9, 100)
        self.assertEqual(sqrt_tree.query(0, 9), 150)
        sqrt_tree.update(3, 1)
        self.assertEqual(sqrt_tree.query(3, 3), 1)


if __name__ == '__main__':
    unittest.main()
