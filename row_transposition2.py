import re

class RowTransposition:
    def __init__(self, key, text):
        self.key = self._key_transform(key)
        self.num_cols = len(self.key)
        self.num_rows = -(-len(text) // self.num_cols)

    def _key_transform(self, key):
        key_transferred = ""
        key_digital = ""

        # 先把key中的數字提取出來
        for d in re.findall(r'\d+',key):
            key_digital += str(d)
        
        # 判斷key中重複的數字
        for i in key_digital:
            if i not in key_transferred: 
                key_transferred += i

        index = 0
        # 把缺的數字補進去變連續數字
        for i in range(1,int(max(key_transferred))):
            if str(i) not in key_transferred:
                key_transferred = key_transferred[:index] + str(i) + key_transferred[index:]
                index += 2

        return key_transferred

    def encrypt(self, plaintext):
        ciphertext = ""
        table = [[''] * self.num_cols for _ in range(self.num_rows)]

        num_x = self.num_cols - (len(plaintext) % self.num_cols)
        if num_x != 0:
            plaintext += 'x' * num_x

        row_index = 0
        col_index = 0
        
        for char in plaintext:
            table[row_index][col_index] = char
            col_index += 1
            if col_index == self.num_cols:
                col_index = 0
                row_index += 1
        
        for i in range(self.num_cols):
            col = self.key.index(str(i+1))
            for j in range(self.num_rows):
                ciphertext += table[j][col]
        
        return ciphertext


    def decrypt(self, ciphertext):
        plaintext = ""
        table = [[''] * self.num_cols for _ in range(self.num_rows)]

        row_index = 0
        col_index = 0
        
        for char in ciphertext:
            table[row_index][col_index] = "*"
            col_index += 1
            if col_index == self.num_cols:
                col_index = 0
                row_index += 1
        
        index = 0
        for i in range(self.num_cols):
            col = self.key.index(str(i+1))
            for j in range(self.num_rows):
                table[j][col] = ciphertext[index]
                index += 1
        
        for row in table:
            plaintext += "".join(row)
        
        plaintext = plaintext.replace("*", "")
        
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