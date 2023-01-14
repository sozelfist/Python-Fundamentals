# Decorators

In Python, decorators are a way to modify or extend the functionality of a function or class, without having to make changes to the original source code. They are implemented as callable objects (i.e. functions or classes) that take a function or class as an input, and return a new function or class with the desired modifications.

Decorators are often used to add functionality such as logging, caching, or input validation to a function or class, and they can be applied to both functions and methods.

Here's an example of a simple decorator that logs the input and output of a function

```python
import time
def log_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Function {func.__name__} took {end_time - start_time} seconds')
        return result
    return wrapper

@log_function
def my_function(x, y):
    return x + y

my_function(1, 2)
```

This will print out a message saying that the `my_function` took some number of seconds to execute.

# Metprogramming

Metaprogramming is a technique that allows you to write code that can manipulate code. This is usually achieved through the use of metaclasses and decorators.

An example of metaprogramming in Python is the use of the `@property` decorator, which allows you to define a method that is accessed like an attribute.

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

obj = MyClass(5)
print(obj.value) # prints 5
obj.value = 10
print(obj.value) # prints 10
```

This example defines a class `MyClass` that has a private attribute `_value` and a property `value` that is used to access and modify it.

In addition, it is also possible to use metaclasses to create custom class behavior, such as custom class creation or custom attribute access.

## A few examples of meta-programming

### Dynamic Attribute Creation

```python
class MyClass:
    pass

obj = MyClass()
obj.x = 5
obj.y = 10

print(obj.x) # 5
print(obj.y) # 10
```

Here, we can create new attributes on the fly for an object of `MyClass`, This can be useful when working with dynamic data, such as user input.

### Dynamic Method Creation

```python
class MyClass:
    pass

def my_function(self):
    print("Hello World!")

obj = MyClass()
obj.my_method = my_function
obj.my_method() # Hello World!
```

Here, we can create new methods on the fly for an object of `MyClass`, this can be useful when working with dynamic functions, such as user input.

### Dynamic Class Creation

```python
class_name = "MyClass"
class_parents = (object,)
class_dict = {"x": 5}

MyClass = type(class_name, class_parents, class_dict)

obj = MyClass()
print(obj.x) # 5
```

Here, we can create new classes on the fly, this can be useful when working with dynamic class, such as user input.

### Metaclass

```python
class MyMeta(type):
    def __init__(cls, name, bases, dct):
        print("MyMeta.__init__")
        super().__init__(name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass
```

Here, we defined our own metaclass called `MyMeta` which will be used to create `MyClass`. This allows you to define custom behavior for class creation and attribute access.

### Mokey Patching

```python
class MyClass:
    def my_method(self):
        return "original"

def new_method(self):
    return "patched"

MyClass.my_method = new_method

obj = MyClass()
print(obj.my_method()) # patched
```

Here, we can change the behavior of a method of a class after it has been defined by modifying its definition in the class's namespace. This is known as monkey patching, and it can be useful for adding new features to a class, fixing bugs, or customizing the behavior of third-party libraries without modifying the original source code. However, it's important to use this feature with caution, as it can lead to unexpected behavior and make the code more difficult to understand and maintain.

These are just a few examples of metaprogramming in Python. Metaprogramming can be a powerful tool for making your code more flexible and dynamic, but it can also make your code more complex and harder to understand. It's important to use metaprogramming techniques judiciously, and to make sure that the benefits outweigh the costs.