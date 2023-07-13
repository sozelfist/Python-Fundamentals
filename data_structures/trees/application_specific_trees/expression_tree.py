import ast
import unittest


class ExpressionTree:
    def __init__(self, node: ast.AST):
        self.node = node
        self.left: ExpressionTree | None = None
        self.right: ExpressionTree | None = None

    def evaluate(self) -> float:
        if isinstance(self.node, ast.BinOp):
            left = self.left.evaluate()
            right = self.right.evaluate()
            if isinstance(self.node.op, ast.Add):
                return left + right
            elif isinstance(self.node.op, ast.Sub):
                return left - right
            elif isinstance(self.node.op, ast.Mult):
                return left * right
            elif isinstance(self.node.op, ast.Div):
                return left / right
        elif isinstance(self.node, ast.Name):
            return self.node.id
        elif isinstance(self.node, ast.Load):
            return self.node.value
        else:
            return self.node.n


def build_expression_tree(expression: str) -> ExpressionTree:
    node = ast.parse(expression, mode='eval').body
    return build_subtree(node)


def build_subtree(node: ast.AST) -> ExpressionTree:
    if isinstance(node, ast.BinOp):
        tree = ExpressionTree(node)
        tree.left = build_subtree(node.left)
        tree.right = build_subtree(node.right)
        return tree
    elif isinstance(node, ast.Name):
        return ExpressionTree(node)
    elif isinstance(node, ast.Load):
        return ExpressionTree(node)
    else:
        return ExpressionTree(node)


class TestExpressionTree(unittest.TestCase):
    def test_addition(self):
        expression = "1 + 2"
        tree = build_expression_tree(expression)
        result = tree.evaluate()
        self.assertEqual(result, 3.0)

    def test_subtraction(self):
        expression = "5 - 2"
        tree = build_expression_tree(expression)
        result = tree.evaluate()
        self.assertEqual(result, 3.0)

    def test_multiplication(self):
        expression = "3 * 4"
        tree = build_expression_tree(expression)
        result = tree.evaluate()
        self.assertEqual(result, 12.0)

    def test_division(self):
        expression = "8 / 2"
        tree = build_expression_tree(expression)
        result = tree.evaluate()
        self.assertEqual(result, 4.0)

    def test_complex_expression(self):
        expression = "( 1 + 2 ) * 3"
        tree = build_expression_tree(expression)
        result = tree.evaluate()
        self.assertEqual(result, 9.0)

    def test_mismatched_parentheses(self):
        expression = "( 1 + 2"
        with self.assertRaises(SyntaxError):
            build_expression_tree(expression)

    def test_empty_expression(self):
        expression = ""
        with self.assertRaises(SyntaxError):
            build_expression_tree(expression)


if __name__ == '__main__':
    unittest.main()
