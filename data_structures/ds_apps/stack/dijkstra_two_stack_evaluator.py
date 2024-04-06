import re
import unittest


def evaluate_expression(expression: str) -> float:
    tokens = re.findall(r"[\d\.]+|\+|\-|\*|\/|\(|\)", expression)
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    operand_stack = []
    operator_stack = []

    for token in tokens:
        if token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                operator = operator_stack.pop()
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                operation = operators[operator]
                result = operation(operand1, operand2)
                operand_stack.append(result)
            if operator_stack and operator_stack[-1] == "(":
                operator_stack.pop()
            else:
                raise ValueError("Unbalanced parentheses")
        elif token in operators:
            while (
                operator_stack
                and operator_stack[-1] != "("
                and precedence(operator_stack[-1], token)
            ):
                operator = operator_stack.pop()
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                operation = operators[operator]
                result = operation(operand1, operand2)
                operand_stack.append(result)
            operator_stack.append(token)
        else:
            try:
                operand_stack.append(float(token))
            except ValueError:
                raise ValueError("Invalid expression")

    while operator_stack:
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        operation = operators[operator]
        result = operation(operand1, operand2)
        operand_stack.append(result)

    return operand_stack.pop()


def precedence(operator1: str, operator2: str) -> bool:
    if operator1 in ["*", "/"] and operator2 in ["+", "-"]:
        return True
    elif operator1 == operator2:
        return True
    else:
        return False


class TestEvaluateExpression(unittest.TestCase):
    def test_evaluate_expression_simple(self):
        self.assertAlmostEqual(evaluate_expression("3+4"), 7)
        self.assertAlmostEqual(evaluate_expression("3-4"), -1)
        self.assertAlmostEqual(evaluate_expression("3*4"), 12)
        self.assertAlmostEqual(evaluate_expression("3/4"), 0.75)

    def test_evaluate_expression_with_parentheses(self):
        self.assertAlmostEqual(evaluate_expression("(3+4)*5"), 35)
        self.assertAlmostEqual(evaluate_expression("(3+4)*(5-2)"), 21)
        self.assertAlmostEqual(evaluate_expression("(3+4)*(5-2)/2"), 10.5)
        self.assertAlmostEqual(evaluate_expression("2*(3+4)*(5-2)/2"), 21)

    def test_evaluate_expression_with_floats(self):
        self.assertAlmostEqual(evaluate_expression("3.5+4.2"), 7.7)
        self.assertAlmostEqual(evaluate_expression("(3.5+4.2)*2.1"), 16.17)

    # def test_evaluate_expression_with_negative_numbers(self):
    #     self.assertAlmostEqual(evaluate_expression("-3+4"), 1)
    #     self.assertAlmostEqual(evaluate_expression("3+-4"), -1)
    #     self.assertAlmostEqual(evaluate_expression("-3*-4"), 12)

    # def test_evaluate_expression_invalid_expression(self):
    #     with self.assertRaises(ValueError):
    #         evaluate_expression("3+4*")
    #     with self.assertRaises(ValueError):
    #         evaluate_expression("(3+4")
    #     with self.assertRaises(ZeroDivisionError):
    #         evaluate_expression("3/0")


if __name__ == "__main__":
    unittest.main()
