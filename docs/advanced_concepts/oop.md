# OOP - Object Oriented Programming

Object-oriented programming (OOP) is a programming paradigm that allows you to model real-world objects and their interactions using classes and objects. OOP has several concepts that are fundamental to understanding how it works, such as

## Class 

A class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Hello, my name is {self.name}")

person = Person("Alice", 30)
person.say_hello() # "Hello, my name is Alice"
```

In this example, `Person` is a class that has two attributes, `name` and `age` and a method `say_hello`.

## Object

An object is an instance of a class, created at runtime. You can create multiple objects of the same class, each with its own unique state.

```python
person1 = Person("Alice", 30)
person2 = Person("Bob", 35)
```

In this example, `person1` and `person2` are two objects of the class `Person`.

## Encapsulation

Encapsulation is the practice of keeping an object's state and behavior hidden from the outside world, and only exposing a well-defined interface for interacting with the object. This allows you to change the implementation of an object without affecting the code that uses it.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def say_hello(self):
        print(f"Hello, my name is {self._name}")
        
person = Person("Alice", 30)
print(person._name) # "Alice"
```

In this example, the class `Person` has two attributes, `_name` and `_age`, which are prefixed with an underscore to indicate that they are intended to be private and should not be accessed or modified directly by code outside the class. Instead, a public method `say_hello` is provided to interact with the object.

## Inheritance

Inheritance is a mechanism that allows you to create a new class that inherits the properties and methods of an existing class. This allows you to reuse and extend existing code, and also create a hierarchy of classes that share a common interface.

```python
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    def say_hello(self):
        print(f"Hello, my name is {self._name} and I am studying {self.major}")

student = Student("Charlie", 20, "Computer Science")
student.say_hello() # "Hello, my name is Charlie and I am studying Computer Science"
```

In this example, `Student` is a new class that inherits from `Person` class and also has an additional attribute `major` and the `say_hello` method is overridden to include this new attribute.

## Polymorphism

Polymorphism is the ability of an object to take on many forms. In OOP, polymorphism allows you to use a single interface to represent different types of objects. For example, you can create a function that takes any object that is an instance of a certain class or its subclasses, and it will work with any object of that type.

```python
def introduce(person: Person):
    person.say_hello()

introduce(person) # "Hello, my name is Alice"
introduce(student) # "Hello, my name is Charlie and I am studying Computer Science"
```

In this example, the `introduce` function takes an object of type `Person` as an argument, and it can be used with any object that is an instance of the `Person` class or any of its subclasses, such as `Student`

These are the core concepts of OOP, and they are fundamental to understanding how to design and implement object-oriented systems using Python. OOP allows you to create organized, reusable, and maintainable code, and it's a powerful tool for solving real-world problems.