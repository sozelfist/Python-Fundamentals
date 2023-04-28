# Hash Table

In computing, a _hash table_, also known as hash map, is a data structure that implements an associative array or dictionary. It is an abstract data type that maps keys to values. A hash table uses a _hash function_ to compute an _index_, also called a _hash code_, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored.

Ideally, the hash function will assign each key to a unique bucket, but most hash table designs employ an imperfect hash function, which might cause hash collisions where the hash function generates the same index for more than one key. Such collisions are typically accommodated in some way.

In a well-dimensioned hash table, the average time complexity for each lookup is independent of the number of elements stored in the table. Many hash table designs also allow arbitrary insertions and deletions of key–value pairs, at amortized constant average cost per operation.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/315px-Hash_table_3_1_1_0_1_0_0_SP.svg.png">
    <p>A small phone book as a hash table</p>
</div>

For more information, see :books: [Wikipedia](https://en.wikipedia.org/wiki/Hash_table)

## Time complexity in big O notation

| **Algorithm** | **Average** | **Worst case** |
| ------------- | ----------- | -------------- |
| **Space**     | $\Theta(n)$ | $O(n)$         |
| **Search**    | $\Theta(1)$ | $O(n)$         |
| **Insert**    | $\Theta(1)$ | $O(n)$         |
| **Delete**    | $\Theta(1)$ | $O(n)$         |

## Implementation

The `HashTable` class is implemented here [hash_table.py](../../data_structures/hash_table.py)

## Explanation

This code is an implementation of a hash table data structure. The hash table uses an array to store key-value pairs, with each key being hashed to an index in the array, where the associated value is stored. The HashTable class has several methods that allow one to insert, search, delete, and get key-value pairs, as well as retrieve all keys and values in the table.

- The `__init__` method initializes the hash table with a given size, and creates an empty array of that size to store key-value pairs. The insert method takes a key and a value and hashes the key to an index in the array, and then appends the key-value pair to that index.
- The `_resize` method is called when the load factor (number of key-value pairs in the table divided by the size of the table) exceeds 0.75, it will double the size of the table and rehash all the key-value pairs.
- The `search` method takes a key and returns the associated value if found, otherwise it returns `None`.
- The `delete` method takes a key and removes the key-value pair with that key from the table.
- The `get` method takes a key and returns the associated value, or raises a `KeyError` if the key is not found.
- The `keys` method returns a list of all keys in the table, and the values method returns a list of all values in the table.

The class is also equipped with `unittest` that tests the basic functionality of the class.