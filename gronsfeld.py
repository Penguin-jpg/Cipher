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
    3. 將切割出的數字對應到[a-zA-Z0-9]+[-+=]
    4. 重複1~3步3次
    4. 由於做完之後key長度會變長，所以要切到跟原本一樣長
    (註: 因為在demo過程中收到的plaintext是來自上一個方法的密文，而非原本的明文，若用一般的Autokey方法會失敗，所以才改成這種方式)
- 加解密:
    目前和一般的Vigenere cipher方法一樣
"""


class Gronsfeld:
    def __init__(self, key):
        self.AVAILABLE_CHARS = string.digits + string.ascii_letters + "-+="
        self.key = key
        # 三次之後重複的字有點多，先做三次就好
        self._process_key(repeat_times=3, truncate_length=len(key))

    def _key_to_all_nums(self):
        """Turn every char in key to number"""
        for char in self.AVAILABLE_CHARS:
            self.key = self.key.replace(char, str(ord(char)))

    def _split_to_groups(self):
        """Randomly split key into k groups with length 2 or 3 and map them to AVAILABLE_CHARS"""
        # 切割字元數會在 [2,3] 中循環
        splits, index, splited_keys = [2, 3], 0, []

        while len(self.key) > 0:
            split = splits[index]
            num = sum(ord(char) for char in self.key[:split])
            splited_keys.append(num % len(self.AVAILABLE_CHARS))
            self.key = self.key[split:]
            index = (index + 1) % len(splits)

        self.key = "".join(self.AVAILABLE_CHARS[splited_key] for splited_key in splited_keys)

    def _process_key(self, repeat_times, truncate_length):
        """Repeat process for n times"""
        for _ in range(repeat_times):
            self._key_to_all_nums()
            self._split_to_groups()

        # 由於上面的步驟重複多次後會使key變得更長，所以要切回原本的長度
        self.key = self.key[:truncate_length]

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
        return self._rotate_string(plaintext)

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Vigenere cipher"""
        return self._rotate_string(ciphertext, reverse=True)


if __name__ == "__main__":
    key = "DeT3Qhx6j8SQ7OL6PwlsHjcha9JUpyXD"
    # key = "joSFzkRgUgjhoz4RWkAhBLRnwho8ZAm7"
    plaintext = "456ThismagazineisavailableinanybigcityinJapanShemiscalculatedtheamountofbrothinhersoupandinadvertentlyboileditalloff123"
    # plaintext = "789Yesphil=osophicallyspeakingalltweetsarebadbuttobefullyhumanistorebelagainstthisfacttosendourterribletw=eetsoutintothe+universeanyway4425-6321"
    print("original key: " + key)
    gronsfeld = Gronsfeld(key)
    encrypted = gronsfeld.encrypt(plaintext)
    print("encrypted: " + encrypted)
    decrypted = gronsfeld.decrypt(encrypted)
    print("decrypted: " + decrypted)
