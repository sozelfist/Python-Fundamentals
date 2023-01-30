import unittest


class Progression:
    """ Iterator producing a generic progression
    Default iterator produces the whole numbers 0, 1, 2, ->...
    """
    iterator_name = 'generic progression'

    def __init__(self, start=0):
        """ Initialize current to the first value of the progression """
        self._current = start

    def _advance(self):
        """ Update self._current to a new value
        This should be overridden by a subclass to customize progression

        By convention, if current is set to None, this designate the
        end of a infinite progression
        """

        self._current += 1

    def __next__(self):
        """ Return the next element, or else raise StopIteration error. """
        if self._current is None:       # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current       # record current value to return
            self._advance()              # advance to prepare for next time
            return answer                # return the answer

    def __iter__(self):
        """ By convention an iterator must be return itself as an iterator """
        return self

    def printProgression(self, n):
        """ Print next n values of the progression """
        print(f'Printing the next {n} elements of {self.iterator_name}')
        print(' '.join(str(next(self)) for index in range(n)))

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        cls.iterator_name = kwargs.get('iterator_name', 'generic progression')


# inherit from class Progression


class ArithmeticProgression(Progression, iterator_name='arithmetic progression'):
    """ Iterator producing an arithmetic progression. """

    def __init__(self, increment=1, start=0):
        """ Create a new arithmetic progression

        increment   the fixed constant to add to each term (default 1)
        start       the first item of the progression (default 0)
         """
        if increment <= 0:
            raise ValueError("The increment must be a positive number")
        super().__init__(start)          # initialize from base class
        self._increment = increment

    def _advance(self):                  # overide inherited method
        """ Update current value by adding the fixed increment """
        self._current += self._increment

    def nth_element(self, n: int):
        """ Return the nth element of the progression """

        return self._current + (n - 1) * self._increment

# inherit from Progression class


class GeometricProgression(Progression, iterator_name='geometric progression'):
    """ Iterator producing a geometric progression. """

    def __init__(self, base=2, start=1):
        """ Create a new geometric progression

        base        the fixed constant multiplied to each term (default 2)
        start       the first item of the progression (default 1)
         """
        if base <= 0:
            raise ValueError("The base must be a positive number")
        super().__init__(start)
        self._base = base

    def _advance(self):
        """ Update current value by multiplying it by the base value """
        self._current *= self._base

    def nth_element(self, n: int):
        """ Return the nth element of the progression """
        return self._current * self._base ** (n - 1)

# inherit from Progression class


class FibonacciProgression(Progression, iterator_name='fibonacci progression'):
    """ Iterator producing a generalized Fibonacci progression. """

    def __init__(self, first=0, second=1):
        """ Create a new Fibonacci progression

        first        the first term of the progression (default 0)
        second       the second term of the progression (default 1)
         """

        super().__init__(first)          # start progeression at first
        self._prev = second - first      # fictitious value preceding the first

    def nth_element(self, n: int):
        """ Return the nth element of the progression """
        for i in range(n - 1):
            self._prev, self._current = self._current, self._prev + self._current
        return self._current

    def _advance(self):
        """ Update current value by taking sum of previous two """
        self._prev, self._current = self._current, self._prev + self._current


class TestProgression(unittest.TestCase):
    def test_generic_progression(self):
        progression = Progression()
        self.assertEqual(next(progression), 0)
        self.assertEqual(next(progression), 1)
        self.assertEqual(next(progression), 2)

    def test_arithmetic_progression(self):
        progression = ArithmeticProgression(increment=2, start=2)
        self.assertEqual(next(progression), 2)
        self.assertEqual(next(progression), 4)
        self.assertEqual(next(progression), 6)
        self.assertEqual(progression.nth_element(3), 12)
        self.assertEqual(progression.iterator_name, 'arithmetic progression')

    def test_geometric_progression(self):
        progression = GeometricProgression(base=2, start=2)
        self.assertEqual(next(progression), 2)
        self.assertEqual(next(progression), 4)
        self.assertEqual(next(progression), 8)
        self.assertEqual(progression.nth_element(4), 128)
        self.assertEqual(progression.iterator_name, 'geometric progression')

    def test_fibonacci_progression(self):
        progression = FibonacciProgression(first=1, second=2)
        self.assertEqual(next(progression), 1)
        self.assertEqual(next(progression), 2)
        self.assertEqual(next(progression), 3)
        self.assertEqual(progression.nth_element(4), 21)
        self.assertEqual(progression.iterator_name, 'fibonacci progression')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            progression = ArithmeticProgression(increment=-1, start=2)
        with self.assertRaises(ValueError):
            progression = GeometricProgression(base=-1, start=2)


if __name__ == '__main__':
    unittest.main()
