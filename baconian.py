"""
Code is based on https://www.geeksforgeeks.org/baconian-cipher/
"""

import secrets
import string
from functools import partial


class Baconian:
    def __init__(self):
        # Added Numbers and an extra digit, because 2**6 > 36 > 2**5.
        # Added lowercase letters, which can fit, since 2**6 > 62
        self.AVAILABLE_CHARS = string.ascii_letters + string.digits
        self.table = {
            key: value
            for key, value in zip(
                self.AVAILABLE_CHARS,
                self._produce_amount_keys(
                    num_keys=len(self.AVAILABLE_CHARS), available_chars=self.AVAILABLE_CHARS
                ),
            )
        }
        self.reverse_table = {value: key for key, value in self.table.items()}

    def _produce_amount_keys(self, num_keys, available_chars):
        keys = set()
        pickchar = partial(secrets.choice, available_chars)
        while len(keys) < num_keys:
            keys |= {"".join([pickchar() for _ in range(6)]) for _ in range(num_keys - len(keys))}
        return keys

    def encrypt(self, plaintext):
        """Encrypt plaintext using Baconian cipher"""
        encrypted = ""
        for char in plaintext:
            encrypted += self.table[char] if char != " " else " "
        return encrypted

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Baconian cipher"""
        decrypted = ""
        while len(ciphertext) > 0:
            sub = ciphertext[:6]
            if sub[0] != " ":
                decrypted += self.reverse_table[sub]
                ciphertext = ciphertext[6:]
            else:
                decrypted += " "
                ciphertext = ciphertext[1:]
        return decrypted


if __name__ == "__main__":
    key = "DeT3Qhx6j8SQ7OL6PwlsHjcha9JUpyXD"
    plaintext = "456ThismagazineisavailableinanybigcityinJapanShemiscalculatedtheamountofbrothinhersoupandinadvertentlyboileditalloff123"
    print("plaintext: " + plaintext)
    baconian = Baconian()
    encrypted = baconian.encrypt(plaintext)
    print("encrypted: " + encrypted)
    decrypted = baconian.decrypt(encrypted)
    print("decryted: " + decrypted)
