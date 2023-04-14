import unittest


def evaluate_expression(expression):
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    ops = []

    for token in expression.split():
        if token.isnumeric():
            stack.append(int(token))
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                op = ops.pop()
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = perform_operation(op, operand1, operand2)
                stack.append(result)
            ops.pop()
        elif token in precedence:
            while ops and ops[-1] != '(' and precedence[ops[-1]]\
                    >= precedence[token]:
                op = ops.pop()
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = perform_operation(op, operand1, operand2)
                stack.append(result)
            ops.append(token)

    while ops:
        op = ops.pop()
        operand2 = stack.pop()
        operand1 = stack.pop()
        result = perform_operation(op, operand1, operand2)
        stack.append(result)

    return stack.pop()


def perform_operation(op, operand1, operand2):
    if op == '+':
        return operand1 + operand2
    elif op == '-':
        return operand1 - operand2
    elif op == '*':
        return operand1 * operand2
    elif op == '/':
        return operand1 / operand2
    elif op == '^':
        return operand1 ** operand2


class TestEvaluateExpression(unittest.TestCase):
    def test_simple_expression(self):
        self.assertEqual(evaluate_expression('3 + 4'), 7)
        self.assertEqual(evaluate_expression('5 * 6'), 30)
        self.assertEqual(evaluate_expression('7 - 2'), 5)
        self.assertEqual(evaluate_expression('10 / 5'), 2)
        self.assertEqual(evaluate_expression('3 ^ 5'), 243)

    def test_expression_with_parentheses(self):
        self.assertEqual(evaluate_expression('3 + 4 * 2 / ( 1 - 5 ) ^ 2'), 3.5)
        self.assertEqual(evaluate_expression('4 + 3 * 2 / ( 1 - 3 ) ^ 2'), 5.5)
        self.assertEqual(evaluate_expression('( 5 - 2 ) * ( 8 + 1 )'), 27)
        self.assertEqual(evaluate_expression('( 7 + 3 ) / ( 2 + 2 )'), 2.5)
        self.assertEqual(evaluate_expression('( 8 - 3 ) * ( 4 - 2 ) + 7'), 17)


if __name__ == '__main__':
    unittest.main()
