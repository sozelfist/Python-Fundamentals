import unittest


def is_balanced(
    s: str,
    open_parens: list[str] = ["(", "[", "{"],
    close_parens: list[str] = [")", "]", "}"],
) -> bool:
    stack: list[str] = []
    for c in s:
        if c in open_parens:
            stack.append(c)
        elif c in close_parens:
            if not stack:
                return False
            if open_parens.index(stack.pop()) != close_parens.index(c):
                return False
    return not stack


class TestBalancedParentheses(unittest.TestCase):
    def test_balanced_parentheses(self):
        self.assertTrue(is_balanced("()"))
        self.assertTrue(is_balanced("([]{})"))
        self.assertTrue(is_balanced("{[()]}"))
        self.assertTrue(is_balanced("(((())))"))
        self.assertTrue(is_balanced("[{()}]"))
        self.assertTrue(is_balanced("(){}[]"))

    def test_unbalanced_parentheses(self):
        self.assertFalse(is_balanced("("))
        self.assertFalse(is_balanced(")("))
        self.assertFalse(is_balanced("([]{})}"))
        self.assertFalse(is_balanced("([)]"))
        self.assertFalse(is_balanced("({)}"))
        self.assertFalse(is_balanced("(()))"))
        self.assertFalse(is_balanced("{[]}()("))


if __name__ == "__main__":
    unittest.main()
