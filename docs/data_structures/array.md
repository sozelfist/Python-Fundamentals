# Array

## Implementation

The `Array` class is implemented at [array.py](../../data_structures/array.py)

## Explaination

This code defines an `Array` class that is implemented using a Python `list`. The class has the following methods:

- `init`: Initializes the class with an optional `capacity` parameter. If no `capacity` is provided, the default value of 10 is used. The class also has a `size` attribute that starts at 0 and a data attribute that is initialized as a list of 0's with the `capacity` `size`.
- `append`: Adds a value to the end of the array. If the `size` of the array is equal to the `capacity`, it calls the `resize` method.
`insert`: Inserts a value at a given `index` in the array. If the `size` of the array is equal to the `capacity`, it calls the `resize` method. It shifts all elements after the given `index` to the right to make space for the new value.
- `delete`: Removes a value at a given `index` in the array. It shifts all elements after the given `index` to the left to fill the gap left by the removed value.
- `resize`: Doubles the `capacity` of the array and creates a new data list with the new `capacity`. It then copies the values from the old data list to the new one.
- `__getitem__`: Allows for using square bracket notation to access elements in the array. If the `index` is out of range, it raises an `IndexError`.
- `__setitem__`: Allows for using square bracket notation to set the value of an element in the array. If the `index` is out of range, it raises an `IndexError`.
- `__len__`: Returns the `size` of the array


The code also includes a `TestArray` class that inherits from the `unittest.TestCase` class and tests the `Array` class using the `unittest` library. The test cases check that the `append`, `insert`, `delete`, and `indexing` methods work as expected, and that the `resize` method is called when needed, and it also check if the `IndexError` is raised when an `index` is out of range.