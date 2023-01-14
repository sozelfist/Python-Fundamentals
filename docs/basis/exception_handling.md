# Exception Handling

In Python, exception handling is a mechanism to handle errors and exceptional events that occur during the execution of a program. It allows the program to continue running even when an error occurs, instead of abruptly stopping and exiting.

When an error occurs, Python raises an exception. The code that could raise an exception is placed in a try-block, and the code that handles the exception is placed in an except-block.

Here is an example of how to use the `try-except` block in Python

```python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

In this example, the code in the try-block raises a `ZeroDivisionError` exception when it tries to divide 5 by 0. The code in the except-block catches the exception and prints an error message.

You can also have multiple except-blocks for different types of exceptions and also have an optional else block to run a code when the try-block does not raise any exception.

```python
try:
    x = int("hello")
except ValueError:
    print("Invalid input.")
except TypeError:
    print("Invalid type.")
else:
    print("The input is valid.")
```

In this example, the code in the try-block raises a `ValueError` or `TypeError` exception when it tries to convert "hello" to int. The code in the first and second except-blocks catches the exception and prints an error message. If the try-block does not raise any exception, the code in the else-block will be executed.

You can also use the `finally` block to place code that must be executed whether an exception is raised or not.

```python
try:
    x = int("5")
except ValueError:
    print("Invalid input.")
finally:
    print("The try-block is finished.")
```

In this example, the `finally` block will always be executed, whether an exception is raised or not.

Exception handling is an important part of the Python language, and it allows you to write robust and reliable code that can handle errors and exceptional events in a controlled manner.