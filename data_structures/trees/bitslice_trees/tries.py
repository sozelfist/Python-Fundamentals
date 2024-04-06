import unittest


class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.words = ["hello", "world", "hi", "how", "are", "you"]
        for word in self.words:
            self.trie.insert(word)

    def test_insert(self):
        self.trie = Trie()
        self.trie.insert("hello")
        self.trie.insert("world")
        self.assertEqual(self.trie.search("hello"), True)
        self.assertEqual(self.trie.search("world"), True)
        self.assertEqual(self.trie.search("hi"), False)

    def test_search(self):
        self.assertEqual(self.trie.search("hello"), True)
        self.assertEqual(self.trie.search("world"), True)
        self.assertEqual(self.trie.search("hi"), True)
        self.assertEqual(self.trie.search("how"), True)
        self.assertEqual(self.trie.search("are"), True)
        self.assertEqual(self.trie.search("you"), True)
        self.assertEqual(self.trie.search("hey"), False)

    def test_starts_with(self):
        self.assertEqual(self.trie.starts_with("h"), True)
        self.assertEqual(self.trie.starts_with("ho"), True)
        self.assertEqual(self.trie.starts_with("how"), True)
        self.assertEqual(self.trie.starts_with("hey"), False)


if __name__ == "__main__":
    unittest.main()
