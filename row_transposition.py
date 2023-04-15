import re
import math


class RowTransposition:
    def __init__(self, key):
        self.key = self._key_transform(key)

    def _key_transform(self, key):
        """Make key valid for Grille cipher"""
        # 先把key中的數字提取出來並轉成set確保不重複
        digits = set(re.findall(r"\d+", key))

        # 把缺的數字補進去變連續數字
        digits = digits.union([str(i) for i in range(1, int(max(digits)))])

        # 將數字合成字串
        numeric_key = "".join(digits)

        return numeric_key

    def encrypt(self, plaintext):
        """Encrpyt plaintext using Row transposition cipher"""
        self.num_cols = len(self.key)
        self.num_rows = math.ceil(len(plaintext) / self.num_cols)
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
    rowTransposition = RowTransposition(key)
    encrypted = rowTransposition.encrypt(plaintext)
    print("encrypted: " + encrypted)
    decrypted = rowTransposition.decrypt(encrypted)
    print("decrypted: " + decrypted)
