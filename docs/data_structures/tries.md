# Trie

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
