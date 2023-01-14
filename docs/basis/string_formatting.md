# String Formatting

In Python, string formatting is the process of creating a new string by combining a fixed string (the format string) with one or more placeholders, and replacing the placeholders with values.

There are several ways to format strings in Python

1. The `%` operator: This method uses the `%` operator to replace placeholders in a string with values.

    ```python
    name = "Alice"
    age = 30
    print("My name is %s and I am %d years old." % (name, age))
    # Output: My name is Alice and I am 30 years old.
    ```

    In this example, the placeholders `%s` and `%d` are replaced with the values of the variables name and age, respectively.

2. The `format()` method: This method uses the `format()` method to replace placeholders in a string with values.

    ```python
    name = "Alice"
    age = 30
    print("My name is {} and I am {} years old.".format(name, age))
    # Output: My name is Alice and I am 30 years old.
    ```

    In this example, the curly braces `{}` are placeholders that are replaced with the values of the variables `name` and `age`, respectively.

3. `f-strings` (or formatted string literals): This method uses f-strings (introduced in `Python 3.6`) to embed expressions inside string literals using `{}`.

    ```python
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")
    # Output: My name is Alice and I am 30 years old.
    ```

    In this example, the expressions name and age are evaluated and replaced inside the f-string.

All of these methods allow you to create new strings by combining a fixed string with one or more placeholders, and replacing the placeholders with values. String formatting is a powerful feature in Python, and it allows you to create dynamic and customized strings with ease.