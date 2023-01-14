# Function

Functions are a fundamental concept in Python and in programming in general. They allow you to group a set of related statements together and to give them a name, making your code more organized, readable and reusable.

A function in Python is defined using the `def` keyword, followed by the function name, a set of parentheses, and a colon. The statements that make up the function body are indented under the definition line.

```python
def my_function():
    print("Hello, World!")
```

The above is an example of a simple function that doesn't take any arguments and just print a message. To call a function, you simply use its name followed by parentheses, like this

```python
my_function() # output : Hello, World!
```

Functions can also take arguments, which are values that are passed to the function when it's called. These arguments are used by the function to perform its tasks. Here's an example of a function that takes two arguments, `x` and `y`, and returns their sum

```python
def add(x, y):
    return x + y

result = add(5, 3)
print(result) # output : 8
```

Functions can also `return` values using the return statement. In the above example, the add function takes two arguments and returns their sum.

Functions can also have default values for their arguments. This means that if a value is not provided for an argument when the function is called, it will use the default value instead.

```python
def say_hello(name = "stranger"):
    print("Hello, " + name + "!")

say_hello() # output : Hello, stranger!
say_hello("John") # output : Hello, John!
```

In the above example, the `say_hello` function takes one argument `name`, with a default value of "stranger", and print a greeting message.

## A few more things about functions

1. Docstrings: Docstrings are used to provide documentation for a function. They are enclosed in triple quotes (either single or double) and placed at the beginning of the function body. Docstrings can be accessed using the `__doc__` attribute of a function.

    ```python
    def my_function():
        """This is a docstring for my function"""
        print("Hello, World!")
    print(my_function.__doc__) # output : This is a docstring for my function
    ```

2. Anonymous functions (Lambda functions): Python allows you to create anonymous functions (functions without a name) using the `lambda` keyword. These functions are useful for simple operations that can be written in a single line.

    ```python
    add = lambda x, y: x + y
    result = add(5, 3)
    print(result) # output : 8
    ```

3. Recursive functions: Functions can call themselves. This is known as recursion. Recursive functions can be useful for solving problems that can be broken down into smaller subproblems of the same type.

    ```python
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)
    print(factorial(5)) # output : 120
    ```

4. Closure: A closure is a function object that remembers values in the enclosing scope even if they are not present in memory. It is a record that stores a function together with an environment: a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.

    ```python
    def outer(x):
        def inner():
            print(x)
        return inner

    closure = outer(5)
    closure() # output : 5
    ```

5. Decorators: Decorators are a way to modify the behavior of a function or class. They are typically used to add functionality to an existing function or class, such as logging, caching, or authentication. They are defined using the `@` symbol, followed by the name of the decorator function. Here is an example of how to use a decorator to add logging functionality to a function

    ```python
    def log_it(func):
        def wrapped(*args, **kwargs):
            print(f'Calling {func.__name__} with {args} and {kwargs}')
            result = func(*args, **kwargs)
            print(f'{func.__name__} returned {result}')
            return result
        return wrapped

    @log_it
    def add(x, y):
        return x + y

    result = add(5, 3)
    # output : 
    # Calling add with (5, 3) and {}
    # add returned 8
    ```

    In this example, the `log_it` decorator is defined to take a function as input, and it returns a new function that wraps the input function. The wrapped function will print a message before and after the input function is called, and it will return the result of the input function.

    The `@log_it` line above the add function definition indicates that the add function is decorated with the `log_it` decorator.

    Decorators can be useful for adding functionality to functions and classes in a transparent and reusable way, without having to modify the original code.

## Passing arguments to a function

1. Positional arguments: These are the most basic type of arguments, where the values passed to the function match the order of the function's parameters.

    ```python
    def my_function(x, y):
        print(x + y)

    my_function(x = 5, y = 3) # 8
    ```

    In this example, the values 5 and 3 are passed to the function as positional arguments, and they match the order of the parameters `x` and `y`.

2. Keyword arguments: Keyword arguments are arguments that are passed to a function by explicitly specifying the parameter name and value.

    ```python
    def my_function(x, y):
        print(x + y)

    my_function(x = 5, y = 3) # 8
    ```

    In this example, the values 5 and 3 are passed to the function as keyword arguments, and they match the parameter names `x` and `y`.

3. Default arguments: Default arguments are arguments that have a predefined value, which will be used if no value is passed to the function.

    ```python
    def my_function(x, y = 2):
        print(x + y)

    my_function(5) # 7
    ```

    In this example, the function `my_function` takes 2 arguments `x` and `y` with a default value of 2. If we call the function by passing only one argument, the default value of `y` will be used.

4. Variable-length arguments: Some functions may need to accept a variable number of arguments. In python, we can use `*` and `**` syntax to define a variable-length argument list, which will be passed to the function as a tuple or a dictionary respectively.

    - `*args` : The `*` syntax is used to pass a variable number of non-keyworded arguments to a function. It will be passed to the function as a tuple.

        ```python
        def my_function(*args):
            print(args)

        my_function(1, 2, 3) # (1, 2, 3)
        ```
    
    - `**kwargs` : The `**` syntax is used to pass a variable number of keyworded arguments to a function. It will be passed to the function as a dictionary.

        ```python
        def my_function(**kwargs):
            print(kwargs)

        my_function(x = 1, y = 2, z = 3) # {'x': 1, 'y': 2, 'z': 3}
        ```

It's also possible to use a combination of these different types of arguments in the same function.

```python
def my_function(x, y, *args, **kwargs):
    print(x, y, args, kwargs)

my_function(1, 2, 3, 4, 5, a = 6, b = 7)
# output : 1 2 (3, 4, 5) {'a': 6, 'b': 7}
```