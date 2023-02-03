from typing import List, Dict
import unittest


def quine_mc_cluskey(minterms: List[str], maxterm_count: Dict[int, int]) -> List[str]:
    min_term_count = len(minterms)
    essential_prime_implicants = []
    for i in range(min_term_count):
        minterm = minterms[i]
        count = minterm.count("1")
        if count not in maxterm_count:
            continue
        if maxterm_count[count] == 1:
            essential_prime_implicants.append(minterm)
            maxterm_count[count] = 0
        else:
            maxterm_count[count] -= 1
    return essential_prime_implicants


class QuineMcCluskeyTest(unittest.TestCase):
    def test_quine_mc_cluskey(self):
        # Test case 1
        minterms = ["0001", "0010", "0100", "1000"]
        maxterm_count = {1: 4}
        result = quine_mc_cluskey(minterms, maxterm_count)
        self.assertEqual(result, ["1000"])


if __name__ == '__main__':
    unittest.main()
