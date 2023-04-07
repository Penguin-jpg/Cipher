"""
Code is based on
1. https://github.com/carlstoker/classical_ciphers/blob/master/vigenere.py
2. https://github.com/carlstoker/classical_ciphers/blob/master/gronsfeld.py
"""

import string


class Gronsfeld:
    def __init__(self, key, alphabet=string.ascii_lowercase):
        self.alphabet = alphabet
        self.key = "".join(alphabet[i] for i in key)
        self.check_key()

    def check_key(self):
        for char in self.key:
            if char not in self.alphabet:
                err = 'Invalid character in key which does not exist in the alphabet: "{}"'.format(char)
                raise ValueError(err)

    def encrypt(self, plaintext):
        """Encrypt plaintext using Vigenere cipher

        :param plaintext: Plaintext to encrypt
        :return: Encrypted plaintext
        """
        return self.rotate_string(plaintext)

    def decrypt(self, ciphertext):
        """Decrypt plaintext using Vigenere cipher

        :param ciphertext: Ciphertext to decrypt
        :return: Decrypted ciphertext
        """
        return self.rotate_string(ciphertext, True)

    def rotate_string(self, string, reverse=False):
        """Shift a string using a key

        :param string: String to shift using the key
        :param reverse:
        :return:
        """
        key_pos = 0
        shifted = ""

        # Iterate through each char in the plaintext
        for char in string:
            # Ignore characters not in the alphabet
            if char not in self.alphabet:
                shifted += char
                continue

            # Get the position in the alphabet of that char
            pos = self.alphabet.index(char)

            # Calculate the shift based on the current character in the keyword
            key_char = self.key[key_pos]
            shift = self.alphabet.index(key_char)

            # If the copher is being reversed, make the shift negative.
            if reverse:
                shift *= -1

            # Add shifted character to the string
            new_pos = (pos + shift) % len(self.alphabet)
            shifted += self.alphabet[new_pos]

            # Shift key position up 1, mod its length.
            key_pos = (key_pos + 1) % len(self.key)

        return shifted


if __name__ == "__main__":
    key = "7616864623"
    key_list = [int(char) for char in key]
    g = Gronsfeld(key_list)
    encrypted = g.encrypt("helloworld123")
    print(encrypted)
    decrypted = g.decrypt(encrypted)
    print(decrypted)
