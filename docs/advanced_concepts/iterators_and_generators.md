# Iterators and Generators

In Python, an iterator is an object that implements the iterator protocol, which consists of the methods `__iter__()` and `__next__()`. The `__iter__()` method returns the iterator object itself, and the `__next__()` method returns the next value from the iterator. When there are no more items to return, the `__next__()` method should raise `StopIteration`.

An object which will return data, one element at a time. They’re used to represent a stream of data. Iterators can be created by implementing two methods, _`_iter__()` and `__next__()`.

A generator is a special type of iterator, defined as a function that uses the yield keyword rather than returning data. When a generator function is called, it returns an iterator object without actually executing the function. The function is only executed when the iterator's `__next__()` method is called.

In addition to the `yield` keyword, generator functions also make use of the `send()` method, which allows values to be passed into the generator's scope and returned from the `yield` expression.

Here is an example of a simple generator function that generates a sequence of numbers


```python
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in my_range(5):
    print(i)
```

This will outputs:

```sh
0
1
2
3
4
```

As you can see, we defined a function `my_range` that uses the `yield` keyword to generate a sequence of numbers. When we iterate over this generator function using a `for` loop, the function is executed one step at a time, returning the next value of the sequence each time the `__next__()` method is called.

Another example of a generator function is one that generates a fibonacci sequence

```python
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)
```

This will outputs

```sh
0
1
1
2
3
```

This is a more advanced example, but it demonstrates how generator functions can be used to generate infinite sequences, like the fibonacci sequence.

In summary, iterators and generators are powerful tools for working with streams of data in Python. They allow you to work with large amounts of data without loading it all into memory at once, and they provide an easy way to implement custom iteration patterns.