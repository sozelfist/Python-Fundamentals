import unittest


def vigenere_cipher(plaintext: str, keyword: str, encrypt: bool = True) -> str:
    """
    Encrypts or decrypts a plaintext message using the Vigenère
    cipher with a given keyword.

    Args:
        plaintext: The plaintext message to encrypt or decrypt.
        keyword: The keyword to use for the Vigenère cipher.
        encrypt: If True, encrypt the plaintext message (default).
        If False, decrypt the ciphertext message.

    Returns:
        The encrypted or decrypted message as a string.

    """
    key = ""
    for i in range(len(plaintext)):
        key += keyword[i % len(keyword)]
    # generate the key string by repeating the keyword over the length of the
    # plaintext

    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(key[i].upper()) - 65
            # convert the current key letter to a shift value (A=0, B=1, etc.)
            if not encrypt:
                shift = 26 - shift
                # if decrypting, invert the shift value
            char = chr((ord(plaintext[i].upper()) - 65 + shift) % 26 + 65)
            # encrypt or decrypt the current plaintext letter using a
            # Caesar cipher with the current shift value
            ciphertext += char
        else:
            ciphertext += plaintext[i]
            # non-alphabetic characters are copied directly to the ciphertext

    return ciphertext


class TestVigenereCipher(unittest.TestCase):

    def test_encrypt(self):
        plaintext = "HELLO WORLD"
        keyword = "SECRET"
        ciphertext = vigenere_cipher(plaintext, keyword)
        self.assertEqual(ciphertext, "ZINCS OSTCH")

    def test_decrypt(self):
        ciphertext = "ZINCS OSTCH"
        keyword = "SECRET"
        plaintext = vigenere_cipher(ciphertext, keyword, encrypt=False)
        self.assertEqual(plaintext, "HELLO WORLD")

    def test_uppercase(self):
        plaintext = "HELLO WORLD"
        keyword = "SECRET"
        ciphertext = vigenere_cipher(plaintext, keyword)
        self.assertEqual(ciphertext, ciphertext.upper())

    def test_non_alpha(self):
        plaintext = "HELLO WORLD!"
        keyword = "SECRET"
        ciphertext = vigenere_cipher(plaintext, keyword)
        self.assertEqual(ciphertext, "ZINCS OSTCH!")

    def test_long_keyword(self):
        plaintext = "HELLO WORLD"
        keyword = "VERYLONGKEYWORD"
        ciphertext = vigenere_cipher(plaintext, keyword)
        self.assertEqual(ciphertext, "CICJZ JUBPB")


if __name__ == '__main__':
    unittest.main()
