"""
Code is based on: https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/
"""

"""
流程: 
 - key:
    - 如果key的最後一位是英文字，就取2軌
    - 如果key的最後一位是數字且是偶數，就取3軌
    - 否則取4軌
- 加解密:
    目前和原本的Rail Fence cipher一樣
"""


class RailFence:
    def __init__(self, key):
        self.key = self._key_transform(key)

    def _key_transform(self, key):
        """Make key valid for Rail Fence cipher"""
        # key = 軌道數量
        # 若太多軌道的話會沒有意義，因此設計以下程式
        if key[-1].isalpha():
            return 2
        elif key[-1].isdigit() and int(key[-1]) % 2 == 0:
            return 3
        else:
            return 4

    def encrypt(self, plaintext):
        """Encrypt plaintext using Rail Fence cipher"""
        rail = [["\n" for _ in range(len(plaintext))] for _ in range(self.key)]

        dir_down = False
        row, col = 0, 0

        for i in range(len(plaintext)):
            if row == 0 or row == self.key - 1:
                dir_down = not dir_down

            rail[row][col] = plaintext[i]
            col += 1
            row += 1 if dir_down else -1

        result = []
        for i in range(self.key):
            for j in range(len(plaintext)):
                if rail[i][j] != "\n":
                    result.append(rail[i][j])

        return "".join(result)

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Rail Fence cipher"""
        rail = [["\n" for _ in range(len(ciphertext))] for _ in range(self.key)]

        dir_down = None
        row, col = 0, 0

        for i in range(len(ciphertext)):
            if row == 0:
                dir_down = True
            if row == self.key - 1:
                dir_down = False

            rail[row][col] = "*"
            col += 1
            row += 1 if dir_down else -1

        index = 0
        for i in range(self.key):
            for j in range(len(ciphertext)):
                if rail[i][j] == "*" and index < len(ciphertext):
                    rail[i][j] = ciphertext[index]
                    index += 1

        result = []
        row, col = 0, 0
        for i in range(len(ciphertext)):
            if row == 0:
                dir_down = True
            if row == self.key - 1:
                dir_down = False

            if rail[row][col] != "*":
                result.append(rail[row][col])
                col += 1

            row += 1 if dir_down else -1

        return "".join(result)


if __name__ == "__main__":
    # key = "7616864623"
    # plaintext = "helloworld123"
    key = "DeT3Qhx6j8SQ7OL6PwlsHjcha9JUpyXD"
    plaintext = "456ThismagazineisavailableinanybigcityinJapanShemiscalculatedtheamountofbrothinhersoupandinadvertentlyboileditalloff123"
    rail_fence = RailFence(key)
    encrypted = rail_fence.encrypt(plaintext)
    print("encrypted: " + encrypted)
    decrypted = rail_fence.decrypt(encrypted)
    print("decrypted: " + decrypted)
