import unittest


class Generator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def generate_numbers(self):
        for i in range(self.start, self.end):
            yield i


class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = Generator(5, 10)

    def test_generate_numbers(self):
        # Test that the generator returns the correct numbers
        numbers = list(self.gen.generate_numbers())
        self.assertEqual(numbers, [5, 6, 7, 8, 9])

    def test_generate_numbers_with_step(self):
        # Test that the generator can return numbers with a given step
        self.gen.step = 2
        numbers = list(self.gen.generate_numbers())
        self.assertEqual(numbers, [5, 7, 9])

    def test_generate_numbers_with_negative_step(self):
        # Test that the generator can return numbers with a negative step
        self.gen.step = -1
        numbers = list(self.gen.generate_numbers())
        self.assertEqual(numbers, [])

    def test_generate_numbers_with_start_greater_than_end(self):
        # Test that the generator returns an empty list if start is greater than end
        self.gen.start = 10
        self.gen.end = 5
        numbers = list(self.gen.generate_numbers())
        self.assertEqual(numbers, [])


if __name__ == '__main__':
    unittest.main()
