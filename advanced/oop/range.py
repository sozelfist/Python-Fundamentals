import unittest


class Range:
    """ A class that mimic's the built-in range class """

    def __init__(self, start: int, stop: int | None = None, step: int = 1):
        """ Initialize a Range instance
        Semantics is similar to built-in range class """

        if not isinstance(start, int) or not isinstance(step, int):
            raise TypeError("Range arguments must be of type int")
        if step == 0:
            raise ValueError("Step cannot be 0")

        if stop is None:  # special case of range(n)
            start, stop = 0, start  # should be treated as if range(0, n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self) -> int:
        """ Return number of entries in the range """
        return self._length

    def __getitem__(self, index: int) -> int:
        """ Return entry at given index (using standard interpretation if negative) """
        if index < 0:
            index += len(self)  # attemp to convert negative index

        if not 0 <= index < self._length:
            raise IndexError("Index out of range")

        return self._start + index * self._step

    def __repr__(self) -> str:
        return "Range({}, {}, {})".format(self._start, self._start + self._length * self._step, self._step)

    def __contains__(self, value: int) -> bool:
        """ Return True if value is in the range, False otherwise """
        for i in self:
            if i == value:
                return True
        return False

    def __iter__(self):
        """ Return an iterator for the range """
        self._current = self._start
        return self

    def __next__(self) -> int:
        """ Return the next value in the range """
        if self._current >= self._start + self._length * self._step:
            raise StopIteration
        current = self._current
        self._current += self._step
        return current

    def __eq__(self, other: object) -> bool:
        """ Return True if other range is the same as this range, False otherwise """
        if not isinstance(other, Range):
            return False
        return self._start == other._start and self._step == other._step and self._length == other._length


class TestRange(unittest.TestCase):
    def test_init(self):
        r1 = Range(10)
        self.assertEqual(len(r1), 10)
        self.assertEqual(r1[0], 0)
        self.assertEqual(r1[9], 9)
        self.assertEqual(r1[-1], 9)

        r2 = Range(2, 8)
        self.assertEqual(len(r2), 6)
        self.assertEqual(r2[0], 2)
        self.assertEqual(r2[5], 7)
        self.assertEqual(r2[-1], 7)

        r3 = Range(2, 14, 3)
        self.assertEqual(len(r3), 4)
        self.assertEqual(r3[0], 2)
        self.assertEqual(r3[3], 11)
        self.assertEqual(r3[-1], 11)

    def test_getitem(self):
        r1 = Range(10)
        self.assertEqual(r1[0], 0)
        self.assertEqual(r1[9], 9)
        self.assertEqual(r1[-1], 9)
        with self.assertRaises(IndexError):
            r1[10]
        with self.assertRaises(IndexError):
            r1[-11]

    def test_repr(self):
        r1 = Range(10)
        self.assertEqual(repr(r1), "Range(0, 10, 1)")
        r2 = Range(2, 8)
        self.assertEqual(repr(r2), "Range(2, 8, 1)")
        r3 = Range(2, 14, 3)
        self.assertEqual(repr(r3), "Range(2, 14, 3)")

    def test_contains(self):
        r1 = Range(10)
        self.assertTrue(5 in r1)
        self.assertFalse(10 in r1)
        r2 = Range(2, 8)
        self.assertTrue(5 in r2)
        self.assertFalse(8 in r2)
        r3 = Range(2, 14, 3)
        self.assertTrue(5 in r3)
        self.assertFalse(14 in r3)

    def test_iter(self):
        r1 = Range(10)
        self.assertEqual([i for i in r1], [i for i in range(10)])
        r2 = Range(2, 8)
        self.assertEqual([i for i in r2], [i for i in range(2, 8)])
        r3 = Range(2, 14, 3)
        self.assertEqual([i for i in r3], [i for i in range(2, 14, 3)])

    def test_eq(self):
        r1 = Range(10)
        r2 = Range(10)
        r3 = Range(2, 8)
        r4 = Range(2, 8)
        r5 = Range(2, 14, 3)
        r6 = Range(2, 14, 3)
        self.assertEqual(r1, r2)
        self.assertEqual(r3, r4)
        self.assertEqual(r5, r6)

    def test_input_validation(self):
        with self.assertRaises(TypeError):
            Range("10")
        with self.assertRaises(ValueError):
            Range(10, step=0)


if __name__ == '__main__':
    unittest.main()
