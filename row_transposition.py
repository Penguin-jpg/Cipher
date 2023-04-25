import re
import math

"""
流程: 
 - key:
    1. 將所有字元轉ascii後接起來
    2. 去除重複數字(如果有0要去掉)，並轉字串
    3. 補上缺的數字
- 加解密:
    目前和原本的Row Transposition cipher一樣
"""


class RowTransposition:
    def __init__(self, key):
        self.key = self._key_transform(key)

    def _key_transform(self, key):
        """Make key valid for Grille cipher"""
        # 把所有字元轉ascii後接起來
        digits = "".join(str(ord(char)) for char in key)

        # 去除重複數字(順序不變)
        deduplicated_digits = dict.fromkeys(digits)
        # 如果有0要去掉
        if "0" in deduplicated_digits:
            deduplicated_digits.pop("0")

        # 轉成字串
        numeric_key = "".join(list(deduplicated_digits))

        # 將缺的數字插到空隙中
        index = 0
        for num in range(1, int(max(numeric_key))):
            if str(num) not in numeric_key:
                numeric_key = numeric_key[:index] + str(num) + numeric_key[index:]
                index += 2

        return numeric_key

    def encrypt(self, plaintext):
        """Encrpyt plaintext using Row transposition cipher"""
        self.num_cols = len(self.key)
        self.num_rows = math.ceil(len(plaintext) / self.num_cols)
        ciphertext = ""
        table = [[""] * self.num_cols for _ in range(self.num_rows)]

        length_diff = self.num_cols * self.num_rows - len(plaintext)
        # 補x到指定長度
        if length_diff > 0:
            plaintext += "x" * length_diff

        row_index, col_index = 0, 0
        for char in plaintext:
            table[row_index][col_index] = char
            col_index += 1
            if col_index == self.num_cols:
                col_index = 0
                row_index += 1

        for i in range(self.num_cols):
            col = self.key.index(str(i + 1))
            for j in range(self.num_rows):
                ciphertext += table[j][col]

        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Row transposition cipher"""
        self.num_cols = len(self.key)
        self.num_rows = math.ceil(len(ciphertext) / self.num_cols)
        plaintext = ""
        table = [[""] * self.num_cols for _ in range(self.num_rows)]

        index = 0
        for i in range(self.num_cols):
            col = self.key.index(str(i + 1))
            for j in range(self.num_rows):
                table[j][col] = ciphertext[index]
                index += 1

        for row in table:
            plaintext += "".join(row)

        position_of_x = plaintext.find("x")
        if position_of_x != -1:
            return plaintext[:position_of_x]
        return plaintext


if __name__ == "__main__":
    key = "DeT3Qhx6j8SQ7OL6PwlsHjcha9JUpyXD"
    plaintext = "456ThismagazineisavailableinanybigcityinJapanShemiscalculatedtheamountofbrothinhersoupandinadvertentlyboileditalloff123"
    print("original key: " + key)
    row_transposition = RowTransposition(key)
    encrypted = row_transposition.encrypt(plaintext)
    print("encrypted: " + encrypted)
    decrypted = row_transposition.decrypt(encrypted)
    print("decrypted: " + decrypted)
