"""
Code is based on
1. https://github.com/carlstoker/classical_ciphers/blob/master/vigenere.py
2. https://github.com/carlstoker/classical_ciphers/blob/master/gronsfeld.py
"""

import string

"""
流程: 
 - key:
    1. 先將key中的每個字元轉成對應的ascii
    2. 按照[2,3]的切割長度循環切割字串
    3. 將切割出的數字對應到table
    (註: 因為在demo過程中收到的plaintext是來自上一個方法的密文，而非原本的明文，若用一般的Autokey方法會失敗，所以才改成這種方式)
- 加解密:
    1. 先按照一般的Vigenere cipher方法
    2. 將key的ascii相加後除上密文的長度取餘數當做位移量來左移
"""


class Gronsfeld:
    def __init__(self, key):
        self.AVAILABLE_CHARS = string.printable[:-6]  # 取所有可印出的ascii(但不包含" ","\t","\n","\r","\x0b","\x0c")
        self.key = self._key_transform(key)

    def _key_to_all_nums(self, key):
        """Turn every char in key to number"""
        for char in self.AVAILABLE_CHARS:
            key = key.replace(char, str(ord(char)))
        return key

    def _split_to_groups(self, key):
        """Split key into k groups with length 2 or 3 and map them to AVAILABLE_CHARS"""
        # 切割字元數會在 [2,3] 中循環
        splits, index, splited_keys = [2, 3], 0, []

        while len(key) > 0:
            split = splits[index]
            num = sum(ord(char) for char in key[:split])
            splited_keys.append(num % len(self.AVAILABLE_CHARS))
            key = key[split:]
            index = (index + 1) % len(splits)

        return "".join(self.AVAILABLE_CHARS[splited_key] for splited_key in splited_keys)

    def _key_transform(self, key):
        """Make key valid for Gronsfeld cipher"""
        key = self._key_to_all_nums(key)
        key = self._split_to_groups(key)
        return key

    def _rotate_text(self, text, reverse=False):
        """Shift text by (sum(ascii of key) % len(text))"""
        rotate_amount = sum(ord(char) for char in self.key) % len(text)

        # 如果reverse(解密)，就需要把原本從後段截取的部分從前面取出，再接回後面
        if reverse:
            rotate_amount = len(text) - rotate_amount

        # 循環位移
        return text[rotate_amount:] + text[:rotate_amount]

    def encrypt(self, plaintext):
        """Encrypt plaintext using Vigenere cipher"""
        ciphertext = ""
        key_index = 0

        for char in plaintext:
            # char在AVAILABLE_CHARS的位置
            pos = self.AVAILABLE_CHARS.index(char)
            # 字元位移量(右移)
            shift = self.AVAILABLE_CHARS.index(self.key[key_index])
            # 位移
            new_pos = (pos + shift) % len(self.AVAILABLE_CHARS)
            ciphertext += self.AVAILABLE_CHARS[new_pos]

            key_index = (key_index + 1) % len(self.key)

        # 位移密文
        ciphertext = self._rotate_text(ciphertext)

        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Vigenere cipher"""
        plaintext = ""
        key_index = 0

        # 先位移密文換成正確順序
        ciphertext = self._rotate_text(ciphertext, reverse=True)

        for char in ciphertext:
            # char在AVAILABLE_CHARS的位置
            pos = self.AVAILABLE_CHARS.index(char)
            # 字元位移量(左移)
            shift = -self.AVAILABLE_CHARS.index(self.key[key_index])
            # 位移
            new_pos = (pos + shift) % len(self.AVAILABLE_CHARS)
            plaintext += self.AVAILABLE_CHARS[new_pos]

            key_index = (key_index + 1) % len(self.key)

        return plaintext


if __name__ == "__main__":
    key = "DeT3Qhx6j8SQ7OL6PwlsHjcha9JUpyXD"
    # key = "joSFzkRgUgjhoz4RWkAhBLRnwho8ZAm7"
    # plaintext = "456ThismagazineisavailableinanybigcityinJapanShemiscalculatedtheamountofbrothinhersoupandinadvertentlyboileditalloff123"
    plaintext = "789Yesphil=osophicallyspeakingalltweetsarebadbuttobefullyhumanistorebelagainstthisfacttosendourterribletw=eetsoutintothe+universeanyway4425-6321"
    print("original key: " + key)
    gronsfeld = Gronsfeld(key)
    encrypted = gronsfeld.encrypt(plaintext)
    print("encrypted: " + encrypted)
    decrypted = gronsfeld.decrypt(encrypted)
    print("decrypted: " + decrypted)
