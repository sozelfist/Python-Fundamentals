# Variables in Python

Variables are used to store data in Python. A variable is a named container that holds a value, which can be a number, a string, or any other data type. Variables in Python are dynamically typed, meaning you don't need to declare the data type of a variable before using it.

## Variable Naming Rules
In Python, there are certain rules for naming variables:

- Variable names can contain letters, digits, and underscores.
- Variable names must start with a letter or an underscore.
- Variable names are case sensitive, meaning name and Name are two different variables.
- Avoid using reserved keywords as variable names, such as `if`, `while`, `for`, `and`, `or`, and so on.

## Variable Assignment

To create a variable in Python, you use the assignment operator `=`. Here's an example:

```python
x = 5
```

In this example, `x` is the variable name, and 5 is the value assigned to the variable. You can also assign multiple variables at once:

```python
x, y, z = 5, "hello", True
```

In this example, `x` is assigned the value `5`, `y` is assigned the string value `"hello"`, and `z` is assigned the boolean value `True`.

## Variable Types

In Python, variables can hold values of different data types, such as integers, floating-point numbers, strings, lists, and dictionaries. Here are some examples:

```python
# Integer variable
x = 5

# Floating-point variable
y = 3.14

# String variable
name = "John"

# List variable
my_list = [1, 2, 3, 4, 5]

# Dictionary variable
my_dict = {"name": "John", "age": 30}
```

## Variable Scope

In Python, variables have a scope, which determines where the variable can be accessed. A variable can be either `local` or `global`:

A local variable is declared inside a function and can only be accessed within that function.
A global variable is declared outside a function and can be accessed anywhere in the program. Here's an example

```python
x = 10 # global variable

def my_function():
    x = 5 # local variable
    print(x) # Output: 5

my_function()
print(x) # Output: 10
```

In this example, `x` is a global variable with the value 10. The `my_function()` function creates a local variable `x` with the value 5, which is only accessible within the function. When the function is called, it prints the value of the local variable `x`. Outside the function, the global variable `x` is still accessible, and it retains its original value of 10.

## Conclusion

Variables are an essential concept in Python and are used to store data throughout your program. Understanding how to declare and use variables is crucial to writing effective code in Python.