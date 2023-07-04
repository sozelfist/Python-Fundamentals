import unittest


def generateParentheses(n: int) -> list[str]:
    """
    Generates all well-formed parentheses sequences with n pairs of parentheses.

    Args:
        `n`: The number of pairs of parentheses.
    Returns:
        A list of well-formed parentheses sequences.
    """
    result = []
    backtrack(result, "", 0, 0, n)
    return result


def backtrack(result: list[str], current: str, open_count: int, close_count: int, n: int) -> None:
    """
    Recursive function to generate well-formed parentheses sequences.

    Args:
        `result`: The list to store the generated sequences.
        `current`: The current parentheses sequence.
        `open_count`: The count of open parentheses added.
        `close_count`: The count of close parentheses added.
        `n`: The number of pairs of parentheses.
    """
    if len(current) == n * 2:
        result.append(current)
        return

    if open_count < n:
        backtrack(result, current + "(", open_count + 1, close_count, n)

    if close_count < open_count:
        backtrack(result, current + ")", open_count, close_count + 1, n)


class TestGenerateParentheses(unittest.TestCase):

    def test_generate_parentheses_with_n_1(self):
        expected_output = ["()"]
        self.assertEqual(generateParentheses(1), expected_output)

    def test_generate_parentheses_with_n_2(self):
        expected_output = ["(())", "()()"]
        self.assertEqual(generateParentheses(2), expected_output)

    def test_generate_parentheses_with_n_3(self):
        expected_output = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertEqual(generateParentheses(3), expected_output)

    def test_generate_parentheses_with_n_4(self):
        expected_output = [
            "(((())))", "((()()))", "((())())", "((()))()", "(()(()))",
            "(()()())", "(()())()", "(())(())", "(())()()", "()((()))",
            "()(()())", "()(())()", "()()(())", "()()()()"
        ]
        self.assertEqual(generateParentheses(4), expected_output)


if __name__ == "__main__":
    unittest.main()
