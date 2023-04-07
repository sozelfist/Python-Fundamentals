import unittest

from sympy import Limit, Symbol


def limit(function, x, a):
    """
    function : function f(x)
    x : independent variable
    a : value that x approaches
    """
    x = Symbol(x)
    limit = Limit(function, x, a)
    return limit.doit()


class TestLimit(unittest.TestCase):
    def test_limit(self):
        result = limit("x**2", "x", 0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
