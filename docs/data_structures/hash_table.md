# Hash Table

## Implementation

The `HashTable` class is implemented here [hash_table.py](../../data_structures/hash_table.py)

## Explaination

This code is an implementation of a hash table data structure. The hash table uses an array to store key-value pairs, with each key being hashed to an index in the array, where the associated value is stored. The HashTable class has several methods that allow one to insert, search, delete, and get key-value pairs, as well as retrieve all keys and values in the table.

- The `__init__` method initializes the hash table with a given size, and creates an empty array of that size to store key-value pairs. The insert method takes a key and a value and hashes the key to an index in the array, and then appends the key-value pair to that index. 
- The `_resize` method is called when the load factor (number of key-value pairs in the table divided by the size of the table) exceeds 0.75, it will double the size of the table and rehash all the key-value pairs. 
- The `search` method takes a key and returns the associated value if found, otherwise it returns `None`. 
- The `delete` method takes a key and removes the key-value pair with that key from the table. 
- The `get` method takes a key and returns the associated value, or raises a `KeyError` if the key is not found. 
- The `keys` method returns a list of all keys in the table, and the values method returns a list of all values in the table.

The class is also equipped with `unittest` that tests the basic functionality of the class.