import unittest


class Rotor:
    def __init__(self, wiring: str, notch: str):
        self.wiring = wiring
        self.notch = notch
        self.position = 0

    def forward(self, char: str) -> str:
        relative_pos = (ord(char) - ord("A") + self.position) % 26
        return self.wiring[relative_pos]

    def backward(self, char: str) -> str:
        relative_pos = (self.wiring.index(char) - self.position) % 26
        return chr(relative_pos + ord("A"))

    def rotate(self):
        self.position = (self.position + 1) % 26


class Reflector:
    def __init__(self, wiring: str):
        self.wiring = wiring

    def reflect(self, char: str) -> str:
        return self.wiring[ord(char) - ord("A")]


class Enigma:
    def __init__(self, rotors: tuple[Rotor, Rotor, Rotor], reflector: Reflector):
        self.rotors = rotors
        self.reflector = reflector

    def encode_letter(self, letter: str) -> str:
        for rotor in self.rotors:
            letter = rotor.forward(letter)
        letter = self.reflector.reflect(letter)
        for rotor in reversed(self.rotors):
            letter = rotor.backward(letter)
        for rotor in self.rotors:
            if rotor.position == ord(rotor.notch) - ord("A"):
                rotor.rotate()
        return letter

    def encode(self, message: str) -> str:
        message = message.upper()
        encoded_message = ""
        for letter in message:
            if letter.isalpha():
                encoded_letter = self.encode_letter(letter)
                encoded_message += encoded_letter
        return encoded_message


class TestEnigma(unittest.TestCase):
    def test_encode_letter(self):
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
        rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
        rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
        reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

        enigma = Enigma((rotor1, rotor2, rotor3), reflector)

        self.assertEqual(enigma.encode_letter("A"), "N")
        self.assertEqual(enigma.encode_letter("B"), "F")
        self.assertEqual(enigma.encode_letter("C"), "X")
        self.assertEqual(enigma.encode_letter("D"), "U")

    def test_encode(self):
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
        rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
        rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
        reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

        enigma = Enigma((rotor1, rotor2, rotor3), reflector)

        message = "HELLO WORLD"
        expected_output = "EHPPKMKIPU"
        self.assertEqual(enigma.encode(message), expected_output)

        message = "ENIGMA MACHINE"
        expected_output = "HARJWNWNXERAH"
        self.assertEqual(enigma.encode(message), expected_output)


if __name__ == "__main__":
    unittest.main()
