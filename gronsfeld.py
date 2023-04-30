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
- 整體流程重複7次
"""


class Gronsfeld:
    def __init__(self, key, repeat_times=7):
        self.AVAILABLE_CHARS = string.printable[:-6]  # 取所有可印出的ascii(但不包含" ","\t","\n","\r","\x0b","\x0c")
        self.repeat_times = repeat_times
        self.keys = []  # 儲存每階段的key
        for _ in range(repeat_times):
            key = self._key_transform(key)
            self.keys.append(key)

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

    def _cipher_round(self, text, key, reverse=False):
        """Do one round of cipher"""
        result = ""
        key_index = 0

        for char in text:
            # char在AVAILABLE_CHARS的位置
            pos = self.AVAILABLE_CHARS.index(char)
            # 字元位移量
            shift = self.AVAILABLE_CHARS.index(key[key_index])
            # 決定右移或左移
            shift *= -1 if reverse else 1
            # 位移
            new_pos = (pos + shift) % len(self.AVAILABLE_CHARS)

            result += self.AVAILABLE_CHARS[new_pos]
            key_index = (key_index + 1) % len(key)

        return result

    def _swap_text_blocks(self, text, key, reverse=False):
        """Shift text by (ascii sum of key) % len(text))"""
        # 用key的ascii和當做分段的index
        split_index = sum(ord(char) for char in key) % len(text)

        # 如果reverse(解密)，就需要把原本從後段截取的部分從前面取出，再接回後面
        if reverse:
            split_index = len(text) - split_index

        # 交換兩段文字
        return text[split_index:] + text[:split_index]

    def encrypt(self, plaintext):
        """Encrypt plaintext using Gronsfeld cipher"""
        ciphertext = ""

        for i in range(self.repeat_times):
            # 加密該round
            ciphertext = self._cipher_round(plaintext, self.keys[i])
            # 旋轉密文
            ciphertext = self._swap_text_blocks(ciphertext, self.keys[i])

            # 開始下一輪
            plaintext = ciphertext

        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Gronsfeld cipher"""
        plaintext = ""

        # 反著做回來
        for i in range(self.repeat_times - 1, -1, -1):
            # 先旋轉密文回到正確順序
            ciphertext = self._swap_text_blocks(ciphertext, self.keys[i], reverse=True)
            # 解密該round
            plaintext = self._cipher_round(ciphertext, self.keys[i], reverse=True)

            # 開始下一輪
            ciphertext = plaintext

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
