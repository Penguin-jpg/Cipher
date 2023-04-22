"""
Code is based on
1. https://github.com/carlstoker/classical_ciphers/blob/master/vigenere.py
2. https://github.com/carlstoker/classical_ciphers/blob/master/gronsfeld.py
"""

import string

"""
流程: 
 - key:
    - 階段1(準備初始key):
        1. 先將key中的每個字元轉成對應的ascii
        2. 按照[2,3,2,3]的切割長度循環切割字串
        3. 將切割出的數字對應到[a-zA-Z0-9]
        4. 由於做完之後key長度會變長，所以要切到跟原本一樣長
    - 階段2(Autokey):
        1. 從明文中取字元，共取len(plaintext)-len(key)個，並接到目前的key後面
        2. 重複階段1的2~3步驟
- 加解密:
    目前和一般的Vigenere cipher方法一樣
"""


class Gronsfeld:
    def __init__(self, key):
        self.AVAILABLE_CHARS = string.digits + string.ascii_letters + "-+="
        self.key = key
        self._autokey_finished = False
        self._process_key()

    def _key_to_all_nums(self):
        """Turn every char in key to number"""
        for char in self.AVAILABLE_CHARS:
            self.key = self.key.replace(char, str(ord(char)))

    def _split_to_groups(self):
        """Randomly split key into k groups with length 2 or 3 and map them to AVAILABLE_CHARS"""
        # 切割字元數會在 [2,3,2,3] 中循環
        splits, index, splited_keys = [2, 3, 2, 3], 0, []

        while len(self.key) > 0:
            split = splits[index]
            num = sum(ord(char) for char in self.key[:split])
            splited_keys.append(num % len(self.AVAILABLE_CHARS))
            self.key = self.key[split:]
            index = (index + 1) % len(splits)
        self.key = "".join(self.AVAILABLE_CHARS[key] for key in splited_keys)

    def _process_key(self):
        original_length = len(self.key)
        self._key_to_all_nums()
        self._split_to_groups()
        # 因為做完上面的步驟後 key 長度會變長，所以要切到原長度
        self.key = self.key[:original_length]

    def _autokey(self, plaintext):
        """add plaintext[:length_diff] to key and do process_key again"""
        length_diff = len(plaintext) - len(self.key)
        self.key += plaintext[:length_diff]
        self._process_key()

    def _rotate_string(self, string, reverse=False):
        """Shift a string using a key (use reverse=True for decrypt)"""
        key_index, result = 0, ""

        for char in string:
            # char在AVAILABLE_CHARS的位置
            pos = self.AVAILABLE_CHARS.index(char)
            # 位移量
            shift = self.AVAILABLE_CHARS.index(self.key[key_index])
            # 解密時移動方向要反過來
            shift *= -1 if reverse else 1

            # 位移
            new_pos = (pos + shift) % len(self.AVAILABLE_CHARS)
            result += self.AVAILABLE_CHARS[new_pos]

            key_index = (key_index + 1) % len(self.key)

        return result

    def encrypt(self, plaintext):
        """Encrypt plaintext using Vigenere cipher"""
        if not self._autokey_finished:
            self._autokey(plaintext)
            self._autokey_finished = True
        return self._rotate_string(plaintext)

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Vigenere cipher"""
        return self._rotate_string(ciphertext, reverse=True)


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
