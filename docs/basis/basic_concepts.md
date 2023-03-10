# Python Basics

Python is a high-level, interpreted programming language that is used for a wide range of applications, from web development to scientific computing. Here are some basic concepts that you should know when getting started with Python

## Variables

Variables are used to store data in Python. You can create a variable by assigning a value to it using the `=` operator. For example:

```python
x = 5
y = "hello"
```

In this example, `x` is an integer variable with the value 5, and `y` is a string variable with the value `"hello"`.

## Data Types

Python supports several different data types, including integers, floating-point numbers, strings, lists, tuples, and dictionaries. Here are some examples of each data type:

```python
# Integers
x = 5
y = 10

# Floating-point numbers
a = 3.14
b = 2.718

# Strings
name = "John"
message = "Hello, world!"

# Lists
my_list = [1, 2, 3, 4, 5]

# Tuples
my_tuple = (1, 2, 3, 4, 5)

# Dictionaries
my_dict = {"name": "John", "age": 30, "city": "New York"}
```

## Operators

Python supports a variety of operators, including arithmetic operators, comparison operators, and logical operators. Here are some examples

```python
# Arithmetic operators
x = 5 + 3
y = 5 - 3
z = 5 * 3
w = 5 / 3

# Comparison operators
a = 5 > 3
b = 5 < 3
c = 5 == 3
d = 5 != 3

# Logical operators
p = True and False
q = True or False
r = not True
```

## Control Structures

Python uses control structures to control the flow of a program. The most common control structures are `if` statements, `for` loops, and `while` loops. Here are some examples

```python
# If statement
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")

# For loop
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i)

# While loop
x = 0
while x < 10:
    print(x)
    x += 1
```

## Functions

Functions are used to encapsulate a block of code that can be reused throughout a program. You can define a function using the `def` keyword. Here's an example

```python
def add_numbers(x, y):
    return x + y

result = add_numbers(5, 10)
print(result) # Output: 15
```

These are just a few of the basic concepts in Python. As you continue to work with the language, you'll encounter many more advanced concepts and features.