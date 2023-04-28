# Trie

In computer science, a trie, also called digital tree or prefix tree, is a type of k-ary search tree, a tree data structure used for locating specific keys from within a set. These keys are most often strings, with links between nodes defined not by the entire key, but by individual characters. In order to access a key (to recover its value, change it, or remove it), the trie is traversed depth-first, following the links between nodes, which represent each character in the key.

Unlike a binary search tree, nodes in the trie do not store their associated key. Instead, a node's position in the trie defines the key with which it is associated. This distributes the value of each key across the data structure, and means that not every node necessarily has an associated value.

All the children of a node have a common prefix of the string associated with that parent node, and the root is associated with the empty string. This task of storing data accessible by its prefix can be accomplished in a memory-optimized way by employing a radix tree.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Trie_example.svg/250px-Trie_example.svg.png">
    <p>A trie for keys "A", "to", "tea", "ted", "ten", "i", "in", and "inn". Each complete English word has an arbitrary integer value associated with it.</p>
</div>

Tries support various operations: insertion, deletion, and lookup of a string key. Tries are composed of
nodes *nodes* that contain links that are either references to other child suffix child nodes, or *nil* . Except for root, each node is pointed to by just one other node, called the parent. Each node contains $R$ links, where $R$ is the cardinality of the applicable alphabet, although tries have a substantial number of
*nil* links.

## Time complexity in big O notation
| **Algorithm** | **Average** | **Worst case** |
| ------------- | ----------- | -------------- |
| **Space**     | $O(n)$      | $O(n)$         |
| **Search**    | $O(n)$      | $O(n)$         |
| **Insert**    | $O(n)$      | $O(n)$         |
| **Delete**    | $O(n)$      | $O(n)$         |

## Implementation

The `Trie` class implementation is placed in [trie.py](../../data_structures/tries.py)

## Explanation

This code defines a `Trie` data structure and its related classes and methods. A `Trie`, also known as a prefix tree, is a tree-like data structure that stores an associative array where the keys are sequences (usually strings). The basic operations of a `Trie` are insertion, search and deletion of a key.

The `Trie` class is defined with three main methods:

- `insert(word: str)`: This method is used to insert a word into the `Trie`. It starts at the root of the `Trie` and creates a new `TrieNode` for each character of the word, if the `TrieNode` does not already exist. It then marks the last `TrieNode` as the end of a word.
- `search(word: str) -> bool`: This method is used to search for a word in the `Trie`. It starts at the root of the `Trie` and traverses through the `TrieNode` of each character of the word. If at any point, the `TrieNode` for a character does not exist, it returns `False`. If it successfully reaches the last character of the word, it checks if the last TrieNode is marked as the end of a word, if yes it returns `True`, otherwise `False`.
- `starts_with(prefix: str) -> bool`: This method is similar to the search method, but instead of checking for the end of a word, it checks if the prefix is present in the Trie.

The `TrieNode` class is a simple class that has three fields:

- `char: str`: The character stored in the `TrieNode`.
- `children: {}`: A dictionary that stores the child TrieNodes of the current `TrieNode`, where the keys are the characters of the child TrieNodes.
- `is_end_of_word: bool`: A flag that indicates if the current `TrieNode` is the end of a word.

The `TestTrie` class is used for testing the `Trie` class, it tests the `Trie` class by creating a `Trie` instance and adding words to it, then it tests the search and starts_with methods by checking if the `Trie` contains the words that were added and the prefixes that were added.
