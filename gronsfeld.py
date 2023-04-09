"""
Code is based on
1. https://github.com/carlstoker/classical_ciphers/blob/master/vigenere.py
2. https://github.com/carlstoker/classical_ciphers/blob/master/gronsfeld.py
"""

import string
import random

"""
目前構想步驟: 
 - 階段1(準備初始key):
    1. 先將key中的每個英文轉成對應的index
    2. 將字串打亂
    3. 隨機分割key成k個長度1或2的group
    4. 將每個group的值按照以下規則替換成英文
        - 長度1: 將該字元轉數字mod52
        - 長度2: 將字元a,b轉數字後相乘並加上randint(a,b)後mod52
    5. 由於合併完後的key長度會變小，所以將key用[a-zA-Z]的隨機值補到原長度
 - 階段2(Autokey):
    1. 從明文中取字元，共取len(plaintext)-len(key)個
    2. 將英文全部轉數字
    3. 重複階段1的2~5步驟
    4. 將字串打亂
"""


class Gronsfeld:
    def __init__(self, key):
        self.AVAILABLE_CHARS = string.ascii_letters
        self.char_set = set(self.AVAILABLE_CHARS)
        self.key = key
        self._prepare_key(len(key))

    def _key_to_all_nums(self):
        """Turn every char in key to number"""
        for i, char in enumerate(self.AVAILABLE_CHARS):
            self.key = self.key.replace(char, str(i))
        print("numeric key: " + self.key)

    def _shuffle_key(self):
        self.key = "".join(random.sample(self.key, len(self.key)))
        print("shuffle key: " + self.key)

    def _random_split(self):
        """Randomly split key into k groups within range [1,2] and turn them to letters"""
        splited_key = []
        while len(self.key) > 0:
            split = random.randint(1, 2)
            if split == 2 and len(self.key) >= 2:
                # if split to length 2, use (a * b + randint(a, b)) % 52 as new key
                a, b = map(int, self.key[:split])
                if a > b:  # make sure a < b
                    a, b = b, a
                offset = random.randint(a, b)
                splited_key.append((a * b + offset) % len(self.AVAILABLE_CHARS))
            else:
                # if split to length 1, use this char % 52 as new key
                splited_key.append(int(self.key[:split][0]) % len(self.AVAILABLE_CHARS))
            self.key = self.key[split:]
        print(f"splited key: {splited_key}")
        self.key = "".join(self.AVAILABLE_CHARS[key] for key in splited_key)
        print("random split key: " + self.key)

    def _pad_to_target_length(self, length):
        """Pad random alphabet to reach specific length"""
        length_diff = length - len(self.key)
        for _ in range(length_diff):
            # randomly select a char from AVAILABLE_CHARS
            self.key += random.choice(self.AVAILABLE_CHARS)
        print("padded key: " + self.key)

    def _prepare_key(self, target_length):
        self._key_to_all_nums()
        self._shuffle_key()
        self._random_split()
        self._pad_to_target_length(target_length)

    def _autokey(self, plaintext):
        """add plaintext[:length_diff] to key and use prepare_key"""
        length_diff = len(plaintext) - len(self.key)
        self.key += plaintext[:length_diff]
        print("added plaintext: " + self.key)
        self._prepare_key(len(plaintext))
        self._shuffle_key()
        print("autokey: " + self.key)

    def _rotate_string(self, string, reverse=False):
        """Shift a string using a key (use reverse=True for decrypt)"""
        key_pos = 0
        shifted = ""

        # Iterate through each char in the plaintext
        for char in string:
            # Ignore characters not in the AVAILABLE_CHARS
            if char not in self.char_set:
                shifted += char
                continue

            # Get the position in AVAILABLE_CHARS of that char
            pos = self.AVAILABLE_CHARS.index(char)
            # Calculate the shift based on the current character in the keyword
            shift = self.AVAILABLE_CHARS.index(self.key[key_pos])
            # If the copher is being reversed, make the shift negative.
            if reverse:
                shift *= -1

            # Add shifted character to the string
            new_pos = (pos + shift) % len(self.AVAILABLE_CHARS)
            shifted += self.AVAILABLE_CHARS[new_pos]

            # Shift key position up 1, mod its length.
            key_pos = (key_pos + 1) % len(self.key)

        return shifted

    def encrypt(self, plaintext):
        """Encrypt plaintext using Vigenere cipher"""
        self._autokey(plaintext)
        return self._rotate_string(plaintext)

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Vigenere cipher"""
        return self._rotate_string(ciphertext, True)


if __name__ == "__main__":
    # key = "7616864623"
    # plaintext = "helloworld123"
    # key = "9b33a532fd9e6"
    # plaintext = "thismagazineisavailableinanybigcityinjapan123456789"
    key = "DeT3Qhx6j8SQ7OL6PwlsHjcha9JUpyXD"
    plaintext = "456ThismagazineisavailableinanybigcityinJapanShemiscalculatedtheamountofbrothinhersoupandinadvertentlyboileditalloff123"
    print("original key: " + key)
    gronsfeld = Gronsfeld(key)
    encrypted = gronsfeld.encrypt(plaintext)
    print("encrypted: " + encrypted)
    decrypted = gronsfeld.decrypt(encrypted)
    print("decrypted: " + decrypted)
