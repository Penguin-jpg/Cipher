import re
import math


class RowTransposition:
    def __init__(self, key, text):
        self.key = self._key_transform(key)
        self.num_cols = len(self.key)
        self.num_rows = math.ceil(len(text) / self.num_cols)

    def _key_transform(self, key):
        """Make key valid for Grille cipher"""
        # 先把key中的數字提取出來並轉成set確保不重複
        digits = set(re.findall(r"\d+", key))
        # 將數字合成字串
        numeric_key = "".join(digits)

        index = 0
        # 把缺的數字補進去變連續數字
        for i in range(1, int(max(numeric_key))):
            if str(i) not in numeric_key:
                numeric_key = numeric_key[:index] + str(i) + numeric_key[index:]
                index += 2

        return numeric_key

    def encrypt(self, plaintext):
        """Encrpyt plaintext using Row transposition cipher"""
        ciphertext = ""
        table = [[""] * self.num_cols for _ in range(self.num_rows)]

        num_x = self.num_cols - (len(plaintext) % self.num_cols)
        # 補x到指定長度
        if num_x != 0:
            plaintext += "x" * num_x

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

        return plaintext


if __name__ == "__main__":
    key = "DeT3Qhx6j8SQ7OL6PwlsHjcha9JUpyXD"
    plaintext = "456ThismagazineisavailableinanybigcityinJapanShemiscalculatedtheamountofbrothinhersoupandinadvertentlyboileditalloff123"
    print("original key: " + key)
    rowTransposition = RowTransposition(key, plaintext)
    encrypted = rowTransposition.encrypt(plaintext)
    print("encrypted: " + encrypted)
    decrypted = rowTransposition.decrypt(encrypted)
    print("decrypted: " + decrypted)
