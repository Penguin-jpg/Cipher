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
    1. 先將key中的英文全部轉數字(0~25)
    2. 將字串打亂
    3. 隨機分割key成k個長度1或2的group
    4. 將每個group的值按照以下規則替換成英文
        - 長度1: 將該字元轉數字mod26
        - 長度2: 將字元a,b轉數字後相乘並加上randint(a,b)後mod26
    5. 由於合併完後的key長度會變小，所以將key用a-z的隨機值補到原長度
 - 階段2(Autokey):
    1. 從明文中取字元，共取len(plaintext)-len(key)個
    2. 將英文全部轉數字
    3. 重複階段1的2~5步驟
    4. 將字串打亂
"""


class Gronsfeld:
    def __init__(self, key, alphabet=string.ascii_lowercase):
        self.alphabet = alphabet
        # self.key = "".join(alphabet[i] for i in key)
        self.key = key
        self._prepare_key(splits=[random.randint(1, 2) for _ in range(10)], original_length=len(key))

    def _key_to_all_nums(self):
        """Turn every char in key to number"""
        for i, letter in enumerate(self.alphabet):
            self.key = self.key.replace(letter, str(i))
        print("numeric key: " + self.key)

    def _shuffle_key(self):
        self.key = "".join(random.sample(self.key, len(self.key)))
        print("shuffle key: " + self.key)

    def _random_split(self, splits):
        """Randomly split key into k groups within range [0,25] and turn them to letters"""
        splited_key = []
        for split in splits:
            if split > len(self.key):
                break
            if split == 2:
                # if split to length 2, use (a * b + randint(a, b)) % 26 as new key
                a, b = map(int, self.key[:split])
                if a > b:  # make sure a < b
                    a, b = b, a
                offset = random.randint(a, b)
                splited_key.append((a * b + offset) % 26)
            else:
                # if split to length 1, use this char % 26 as new key
                splited_key.append(int(self.key[:split][0]) % 26)
            self.key = self.key[split:]
        print(f"splited key: {splited_key}")
        self.key = "".join(self.alphabet[key] for key in splited_key)
        print("random split key: " + self.key)

    def _pad_to_original_length(self, original_length):
        """Pad random alphabet to reach original length"""
        length_diff = original_length - len(self.key)
        for _ in range(length_diff):
            self.key += self.alphabet[random.randint(0, 25)]
        print("padded key: " + self.key)

    def _prepare_key(self, splits, original_length):
        self._key_to_all_nums()
        self._shuffle_key()
        self._random_split(splits)
        self._pad_to_original_length(original_length)

    def _autokey(self, plaintext):
        """add plaintext[:length_diff] to key and use prepare_key"""
        length_diff = len(plaintext) - len(self.key)
        self.key += plaintext[:length_diff]
        print("added plaintext: " + self.key)
        self._prepare_key(splits=[random.randint(1, 2) for _ in range(10)], original_length=len(plaintext))
        self._shuffle_key()
        print("autokey: " + self.key)

    def encrypt(self, plaintext):
        """Encrypt plaintext using Vigenere cipher

        :param plaintext: Plaintext to encrypt
        :return: Encrypted plaintext
        """
        self._autokey(plaintext)
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
    # key = "7616864623"
    key = "9b33a532fd9e6"
    print("original key: " + key)
    # key_list = [int(char) for char in key]
    g = Gronsfeld(key)
    # encrypted = g.encrypt("helloworld123")
    encrypted = g.encrypt("thismagazineisavailableinanybigcityinjapan")
    print(encrypted)
    decrypted = g.decrypt(encrypted)
    print(decrypted)
