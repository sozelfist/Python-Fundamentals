import unittest
from collections import Counter
from math import gcd


class PrimeFactorization:
    def __init__(self, n):
        self.root = self.n = n
        self.factors = Counter()
        self.factorize()

    def __str__(self):
        factors_str = " x ".join([f"{p}^{e}" for p, e in self.factors.items()])
        return f"{self.root} = {factors_str}"

    def factorize(self):
        if self.n < 2:
            return

        # Check for small factors up to sqrt(n)
        for p in range(2, int(self.n**0.5) + 1):
            if self.n % p == 0:
                e = 0
                while self.n % p == 0:
                    self.n //= p
                    e += 1
                self.factors[p] += e

        # If n is not fully factored yet, try Pollard's rho algorithm
        if self.n > 1:
            self.pollard_rho()

        # If n is still greater than 1, it is a prime factor
        if self.n > 1:
            self.factors[self.n] += 1

    def pollard_rho(self):
        x = 2
        y = 2
        d = 1

        while d == 1:
            x = (x * x + 1) % self.n
            y = (y * y + 1) % self.n
            y = (y * y + 1) % self.n
            d = gcd(abs(x - y), self.n)

        if d == self.n:
            return  # failure, try again with a different x
        else:
            self.factors[d] += 1
            self.n //= d
            self.factorize()


class TestPrimeFactorization(unittest.TestCase):
    def test_prime_number(self):
        pf = PrimeFactorization(13)
        self.assertEqual(pf.factors, Counter({13: 1}))

    def test_small_number(self):
        pf = PrimeFactorization(24)
        self.assertEqual(pf.factors, Counter({2: 3, 3: 1}))

    def test_large_number(self):
        pf = PrimeFactorization(1234567890)
        self.assertEqual(pf.factors, Counter({3: 2, 2: 1, 5: 1, 3607: 1, 3803: 1}))

    def test_negative_number(self):
        pf = PrimeFactorization(-10)
        self.assertEqual(pf.factors, Counter())

    def test_zero(self):
        pf = PrimeFactorization(0)
        self.assertEqual(pf.factors, Counter())


if __name__ == "__main__":
    unittest.main()
