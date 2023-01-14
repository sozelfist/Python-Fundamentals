# Variables

In Python, a variable is a named location in memory where a value can be stored. Variables are used to store data and values that can be used in your program. Here's an example of how to create and use a variable in Python

```python
# assign a value to a variable
x = 5

# print the value of the variable
print(x)

# assign a new value to the variable
x = 10

# print the new value of the variable
print(x)
```

In the above example, we first assign the value 5 to the variable `x` using the assignment operator (`=`). Then we use the `print()` function to display the value of the variable. Next, we assign a new value 10 to the variable `x` and use the `print()` function again to display the new value.

In Python, variables do not need to be declared with a specific data type, and their type can change dynamically at runtime. Python uses a system called *duck typing* this means that the type of the variable is determined by the value it holds.

```python
# assign a string value to a variable
x = "Hello World"
print(x)

# assign a integer value to the same variable
x = 5
print(x)
```

In the above example, the variable x is first assigned a string value "Hello World" and then it is assigned an integer value 5, showing that a variable in Python can hold different types of values.

It is important to note that variable names in Python must start with a letter or an underscore (`_`), and can only contain letters, numbers, and underscores. Also, Python has a number of reserved keywords that cannot be used as variable names.