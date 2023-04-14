import unittest


def calculate_posterior_probability(
        hypothesis: str, evidence: str,
        prior_probabilities: dict[str, float],
        likelihoods: dict[str, dict[str, float]]
) -> float:
    """
    Calculates the posterior probability of a hypothesis given some evidence.

    # Parameters:
    - hypothesis (`str`): The hypothesis being considered.
    - evidence (`str`): The evidence being used to update the hypothesis.
    - prior_probabilities (`Dict[str, float]`): A dictionary mapping
    each hypothesis to its prior probability.
    - likelihoods (`Dict[str, Dict[str, float]]`): A dictionary mapping each
    hypothesis to a dictionary of likelihoods of the evidence.

    # Returns:
    - `float`: The posterior probability of the hypothesis given the evidence.
    """
    evidence_probability = sum(
        [likelihoods[h][evidence] * prior_probabilities[h]
         for h in likelihoods.keys()])
    posterior_probability = likelihoods[hypothesis][evidence] * \
        prior_probabilities[hypothesis] / evidence_probability
    return posterior_probability


class TestBayesTheorem(unittest.TestCase):
    def test_calculate_posterior_probability(self):
        hypotheses = ['h1', 'h2']
        prior_probabilities = {'h1': 0.5, 'h2': 0.5}
        likelihoods = {
            'h1': {'e1': 0.6, 'e2': 0.3},
            'h2': {'e1': 0.4, 'e2': 0.7},
        }
        evidence = 'e1'
        result = calculate_posterior_probability(
            hypotheses[0], evidence, prior_probabilities, likelihoods)
        self.assertEqual(result, 0.6)


if __name__ == '__main__':
    unittest.main()
