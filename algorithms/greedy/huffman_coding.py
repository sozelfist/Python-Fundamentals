import heapq
import unittest
from typing import Any


def build_tree(freq: dict[str, int]) -> Any:
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]


def huffman_coding(freq: dict[str, int]) -> dict[str, str]:
    tree = build_tree(freq)
    return {char: code for char, code in tree[1:]}


class TestHuffmanCoding(unittest.TestCase):
    def test_huffman_coding(self):
        freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
        result = huffman_coding(freq)
        self.assertDictEqual(
            result,
            {'a': '1100', 'b': '1101', 'c': '100',
                'd': '101', 'e': '111', 'f': '0'}
        )

        freq = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}
        result = huffman_coding(freq)
        self.assertDictEqual(
            result,
            {
                'a': '100', 'b': '101', 'c': '110',
                'd': '111', 'e': '00', 'f': '01'
            }
        )

        freq = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
        result = huffman_coding(freq)
        self.assertDictEqual(
            result,
            {
                'a': '1000', 'b': '1001', 'c': '101',
                'd': '00', 'e': '01', 'f': '11'
            }
        )


if __name__ == '__main__':
    unittest.main()
