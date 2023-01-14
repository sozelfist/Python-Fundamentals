# Operators

In Python, operators are special symbols that perform specific operations on one or more operands (values or variables). Here are some of the basic operators in Python

## Arithmetic operators

These operators perform arithmetic operations such as addition, subtraction, multiplication, and division.

```python
x = 5
y = 3
print(x + y)  # 8
print(x - y)  # 2
print(x * y)  # 15
print(x / y)  # 1.66666667
print(x % y)  # 2
print(x ** y) # 125
```

## Comparison operators

These operators compare two values and return a Boolean value (`True` or `False`).

```python
x = 5
y = 3
print(x > y)  # True
print(x < y)  # False
print(x == y) # False
print(x != y) # True
print(x >= y) # True
print(x <= y) # False
```

## Logical operators

These operators perform logical operations such as `and`, `or` and `not`.

```python
x = True
y = False
print(x and y) # False
print(x or y)  # True
print(not x)   # False
```

## Assignment operators

These operators are used to assign values to variables.

```python
x = 5
x += 3  # x = x + 3
x -= 2  # x = x - 2
x *= 4  # x = x * 4
x /= 6  # x = x / 6
x %= 3  # x = x % 3
x **= 2 # x = x ** 2
```

## Identity operators

These operators are used to compare the memory location of two objects, and return a Boolean value.

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y) # False
print(x is z) # True
print(x is not y) # True
```

In the above example, `x` and `y` are two different lists, even though they have the same elements. Therefore the is operator returns False when comparing `x` and `y`. However `x` and `z` are pointing to the same list in memory, therefore the is operator returns `True` when comparing `x` and `z`.

## Membership operators

These operators are used to test whether a value is found in a sequence (such as a `string`, `list`, or `tuple`).

```python
x = [1, 2, 3]
print(1 in x)  # True
print(4 in x)  # False
print(1 not in x)  # False
```

These are the basic operators in Python, but there are more advanced operators such as bitwise, ternary, slicing, etc. It's important to understand how these operators work and how to use them correctly to write effective and efficient Python code.