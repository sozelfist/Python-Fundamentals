import unittest


def caesar_cipher(text: str, key: int, encrypt: bool = True) -> str:
    """Encrypt or decrypt text using the Caesar cipher."""
    result = ""
    for char in text:
        # Convert each character to its ASCII code
        code = ord(char)
        # Shift the code by the key (positive for encryption,
        # negative for decryption)
        shift = key if encrypt else -key
        new_code = (
            (code - 65 + shift) % 26 + 65
            if char.isupper()
            else (code - 97 + shift) % 26 + 97
            if char.islower()
            else code
        )
        # Convert the new code back to a character and add it to the result
        result += chr(new_code)
    return result


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(caesar_cipher("HELLO WORLD", 3), "KHOOR ZRUOG")
        self.assertEqual(caesar_cipher("PYTHON IS GREAT", 7), "WFAOVU PZ NYLHA")
        self.assertEqual(
            caesar_cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 25),
            "ZABCDEFGHIJKLMNOPQRSTUVWXY",
        )
        self.assertEqual(caesar_cipher("hello world", 10), "rovvy gybvn")
        self.assertEqual(caesar_cipher("1234!@#$", 5), "1234!@#$")

    def test_decrypt(self):
        self.assertEqual(caesar_cipher("KHOOR ZRUOG", 3, encrypt=False), "HELLO WORLD")
        self.assertEqual(
            caesar_cipher("WFAOVU PZ NYLHA", 7, encrypt=False), "PYTHON IS GREAT"
        )
        self.assertEqual(
            caesar_cipher("ZABCDEFGHIJKLMNOPQRSTUVWXY", 25, encrypt=False),
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        )
        self.assertEqual(caesar_cipher("rovvy gybvn", 10, encrypt=False), "hello world")
        self.assertEqual(caesar_cipher("1234!@#$", 5, encrypt=False), "1234!@#$")


if __name__ == "__main__":
    unittest.main()
