import unittest
from typing import Dict, Tuple
import heapq


def build_tree(freq: Dict[str, int]) -> Tuple:
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


def huffman_coding(freq: Dict[str, int]) -> Dict[str, str]:
    tree = build_tree(freq)
    return {char: code for char, code in tree[1:]}


class TestHuffmanCoding(unittest.TestCase):
    def test_huffman_coding(self):
        freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
        huff_codes = huffman_coding(freq)
        self.assertEqual(huff_codes['a'], '1100')
        self.assertEqual(huff_codes['b'], '1101')
        self.assertEqual(huff_codes['c'], '100')
        self.assertEqual(huff_codes['d'], '101')
        self.assertEqual(huff_codes['e'], '111')
        self.assertEqual(huff_codes['f'], '0')


if __name__ == '__main__':
    unittest.main()
