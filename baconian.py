"""
Code is based on https://www.geeksforgeeks.org/baconian-cipher/
"""

import string

"""
流程: 
 - key:
    不做改變
- 加解密:
    - 加密
        1. 建立一個table照順序包含[a-zA-Z0-9]還有[-+](還有反向的table)
        2. 取字元和key的字元在table中的index做XOR，並轉成長度6的二進位
        3. 將轉換後的二進位當index對應回table中的字元
    - 解密
        把加密倒過來做
"""


class Baconian:
    def __init__(self, key):
        # Added Numbers and an extra digit, because 2**6 > 36 > 2**5.
        # Added lowercase letters, which can fit, since 2**6 > 62
        self.AVAILABLE_CHARS = string.ascii_letters + string.digits
        # [a-zA-Z0-9]只有62個，但XOR完之後會有62,63，所以補上兩個特殊符號
        self.table = {char: i for i, char in enumerate(self.AVAILABLE_CHARS + "-+")}
        self.reverse_table = {value: key for key, value in self.table.items()}
        self.key = key

    def encrypt(self, plaintext):
        """Encrypt plaintext using Baconian cipher"""
        ciphertext = ""
        key_index = 0

        for char in plaintext:
            # 先將字元與key做XOR
            xor = self.table[char] ^ self.table[self.key[key_index]]

            # 將結果轉成長度6的二進位
            binary = bin(xor)[2:].zfill(6)

            # 對應reverse_table的字元
            ciphertext += self.reverse_table[int(binary, 2)]

            key_index = (key_index + 1) % len(self.key)

        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Baconian cipher"""
        plaintext = ""
        key_index = 0
        # 將字元轉回長度6的二進位
        binary_ciphertext = "".join(bin(self.table[char])[2:].zfill(6) for char in ciphertext)

        while len(binary_ciphertext) > 0:
            # 每6個一組切開轉成a~z,A~Z,0~9,-,+後，再對應回index
            num = self.table[self.reverse_table[int(binary_ciphertext[:6], 2)]]
            # 再做一次XOR還原成原本的字元
            plaintext += self.reverse_table[num ^ self.table[self.key[key_index]]]
            key_index = (key_index + 1) % len(self.key)
            binary_ciphertext = binary_ciphertext[6:]

        return plaintext


if __name__ == "__main__":
    key = "DeT3Qhx6j8SQ7OL6PwlsHjcha9JUpyXD"
    plaintext = "456ThismagazineisavailableinanybigcityinJapanShemiscalculatedtheamountofbrothinhersoupandinadvertentlyboileditalloff123"
    print("plaintext: " + plaintext)
    baconian = Baconian(key)
    encrypted = baconian.encrypt(plaintext)
    print("encrypted: " + encrypted)
    decrypted = baconian.decrypt(encrypted)
    print("decryted: " + decrypted)
