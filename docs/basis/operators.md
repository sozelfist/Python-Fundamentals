# Operators in Python

Operators are symbols or keywords in Python that perform operations on one or more operands. Python has several types of operators, including arithmetic, assignment, comparison, logical, bitwise, and identity operators.

## Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on operands. Python supports the following arithmetic operators:

- `+` (addition): Adds two operands.
- `-` (subtraction): Subtracts the second operand from the first operand.
- `*` (multiplication): Multiplies two operands.
- `/` (division): Divides the first operand by the second operand.
- `%` (modulo): Returns the remainder of the division of the first operand by the second operand.
- `**` (exponentiation): Raises the first operand to the power of the second operand.
- `//` (floor division): Returns the integer quotient of the division of the first operand by the second operand.

## Assignment Operators
Assignment operators are used to assign values to variables. Python supports the following assignment operators:

- `=` (assignment): Assigns the value of the right operand to the left operand.
- `+=` (add and assign): Adds the value of the right operand to the left operand and assigns the result to the left operand.
- `-=` (subtract and assign): Subtracts the value of the right operand from the left operand and assigns the result to the left operand.
- `*=` (multiply and assign): Multiplies the value of the right operand with the left operand and assigns the result to the left operand.
- `/=` (divide and assign): Divides the left operand by the right operand and assigns the result to the left operand.
- `%=` (modulo and assign): Performs modulo operation on the left operand with the right operand and assigns the result to the left operand.
- `**=` (exponentiate and assign): Raises the left operand to the power of the right operand and assigns the result to the left operand.
- `//=` (floor divide and assign): Performs floor division on the left operand with the right operand and assigns the result to the left operand.

## Comparison Operators

Comparison operators are used to compare two values. Python supports the following comparison operators:

- `==` (equal to): Returns `True` if the operands are equal; otherwise, returns `False`.
- `!=` (not equal to): Returns `True` if the operands are not equal; otherwise, returns `False`.
- `>` (greater than): Returns `True` if the first operand is greater than the second operand; otherwise, returns `False`.
- `<` (less than): Returns `True` if the first operand is less than the second operand; otherwise, returns `False`.
- `>=` (greater than or equal to): Returns `True` if the first operand is greater than or equal to the second operand; otherwise, returns `False`.
- `<=` (less than or equal to): Returns `True` if the first operand is less than or equal to the second operand; otherwise, returns `False`.

## Logical Operators

Logical operators are used to combine two or more conditions. Python supports the following logical operators:

- `and`: Returns `True` if both conditions are `True`; otherwise, returns `False`.
- `or`: Returns `True` if at least one condition is `True`; otherwise, returns `False`.
- `not`: Returns `True` if the condition is `False`; otherwise, returns `False`.

## Bitwise Operators

Bitwise operators are used to perform bitwise operations on operands. Python supports the following bitwise operators:

- `&` (bitwise AND): Returns 1 if both bits of the corresponding operands are 1; otherwise, returns 0.
- `|` (bitwise OR): Returns 1 if at least one of the corresponding bits of the operands is 1; otherwise, returns 0.
- `^` (bitwise XOR): Returns 1 if the corresponding bits of the operands are different; otherwise, returns 0.
- `~` (bitwise NOT): Inverts the bits of the operand.
- `<<` (left shift): Shifts the bits of the first operand to the left by the number of positions specified by the second operand.
- `>>` (right shift): Shifts the bits of the first operand to the right by the number of positions specified by the second operand.

## Identity Operators

Identity operators are used to check if two objects have the same identity. Python supports the following identity operators:

- `is`: Returns `True` if both operands have the same identity; otherwise, returns `False`.
is not: Returns `True` if both operands do not have the same identity; otherwise, returns `False`.

## Membership Operators

Membership operators are used to check if a value is present in a sequence. Python supports the following membership operators:

- `in`: Returns `True` if the value is present in the sequence; otherwise, returns `False`.
not in: Returns `True` if the value is not present in the sequence; otherwise, returns `False`.

## Operator Precedence

Operators in Python follow a certain precedence order. The order of precedence of operators is as follows (from highest to lowest):

1. Parentheses
2. Exponentiation
3. Multiplication, Division, and Modulo
4. Addition and Subtraction
5. Bitwise Operators
6. Comparison Operators
7. Logical Operators
8. Assignment Operators

Operators with higher precedence are evaluated before operators with lower precedence. If two operators have the same precedence, they are evaluated from left to right.

It's important to understand the precedence of operators in Python to avoid unexpected results in your code.