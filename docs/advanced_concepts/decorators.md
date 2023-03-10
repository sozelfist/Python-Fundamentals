# Decorators in Python

Decorators are a powerful feature in Python that allow you to modify or extend the behavior of a function or class without changing its source code. In other words, decorators are functions that take another function as input and return a new function as output.

## Basic Syntax
The basic syntax for using decorators in Python is as follows:

```python
@decorator_function
def my_function():
    # function code here
```

In this example, `decorator_function` is a function that takes `my_function` as input and returns a new function as output. The `@` symbol is used to indicate that `my_function` should be decorated with `decorator_function`.

## Creating Decorators

To create a decorator in Python, you define a new function that takes a function as input and returns a new function as output. Here is an example of a decorator that adds logging functionality to a function:

```python
def logger(function):
    def wrapper(*args, **kwargs):
        print(f"Calling function {function.__name__} with arguments {args}
    and {kwargs}")
        result = function(*args, **kwargs)
        print(f"Function {function.__name__} returned {result}")
        return result
    return wrapper
```

In this example, `logger` is a decorator function that takes a function as input and returns a new function wrapper that logs the function's input and output. The `*args` and `**kwargs` syntax is used to allow the wrapper function to accept any number of positional and keyword arguments.

## Applying Decorators

To apply a decorator to a function, you simply use the `@` symbol followed by the decorator function name before the function definition. Here is an example of using the logger decorator from above to decorate a function:

```python
@logger
def add_numbers(a, b):
    return a + b
```

In this example, the `add_numbers` function is decorated with the logger decorator, which means that the `add_numbers` function will now have logging functionality added to it.

## Chaining Decorators

It is also possible to chain multiple decorators together to modify a function's behavior in multiple ways. To chain decorators, you simply apply each decorator in sequence using the `@` symbol. Here is an example of chaining two decorators together:

```python
@logger
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

In this example, the `fibonacci` function is decorated with two decorators: `logger` and `memoize`. The `logger` decorator will add logging functionality to the function, and the `memoize` decorator will cache the function's output to improve performance.

## Conclusion

Decorators are a powerful and flexible feature in Python that allow you to modify or extend the behavior of a function or class without changing its source code. By understanding how to create and apply decorators in Python, you can write more efficient and reusable code.