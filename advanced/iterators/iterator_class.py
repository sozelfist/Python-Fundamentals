import unittest


class Iterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            self.start += 1
            return self.start - 1
        else:
            raise StopIteration


class TestIterator(unittest.TestCase):
    def test_iterator_next(self):
        it = Iterator(1, 5)
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), 3)
        self.assertEqual(next(it), 4)

    def test_iterator_stop_iteration(self):
        it = Iterator(1, 5)
        for i in range(5):
            next(it)
        self.assertRaises(StopIteration, next, it)

    def test_iterator_iteration(self):
        it = Iterator(1, 5)
        result = [x for x in it]
        self.assertEqual(result, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
