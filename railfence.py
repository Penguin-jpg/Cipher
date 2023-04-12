"""
Code is based on: https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/
"""

class RailFence:
    def encrypt(self, text, key):
        # key = 軌道數量
        # 若太多軌道的話會沒有意義，因此設計以下程式
        if (len(text) <= 10): key = 2  # 若原文長度 <= 10，key = 2 (兩軌)
        else:
            key = int(key) % len(text)  # 若原文長度 > 10，取 key 和原文長度的餘數
            if (key == 0 or key == 1): key = 2  # 若餘數剛好為 0 或 1，key = 2 (兩軌)

        rail = [['\n' for i in range(len(text))]
                    for j in range(key)]

        dir_down = False
        row, col = 0, 0

        for i in range(len(text)):
            if ((row == 0) or (row == key - 1)):
                dir_down = not dir_down

            rail[row][col] = text[i]
            col += 1

            if (dir_down): row += 1
            else: row -= 1

        result = []
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])

        return("".join(result))


    def decrypt(self, cipher, key):
        if (len(cipher) <= 10): key = 2
        else:
            key = int(key) % len(cipher)
            if (key == 0 or key == 1): key = 2

        rail = [['\n' for i in range(len(cipher))]
                    for j in range(key)]

        dir_down = None
        row, col = 0, 0

        for i in range(len(cipher)):
            if (row == 0):
                dir_down = True
            if (row == key - 1):
                dir_down = False

            rail[row][col] = '*'
            col += 1

            if dir_down: row += 1
            else: row -= 1

        index = 0
        for i in range(key):
            for j in range(len(cipher)):
                if ((rail[i][j] == '*') and (index < len(cipher))):
                    rail[i][j] = cipher[index]
                    index += 1

        result = []
        row, col = 0, 0
        for i in range(len(cipher)):
            if (row == 0): dir_down = True
            if (row == key - 1): dir_down = False

            if (rail[row][col] != '*'):
                result.append(rail[row][col])
                col += 1

            if (dir_down): row += 1
            else: row -= 1

        return("".join(result))

if (__name__ == "__main__"):
    key = "7616864623"
    plain_text = "helloworld123"
    rail_fence = RailFence()

    encrypted = rail_fence.encrypt(plain_text, key)
    print(encrypted)
    decrypted = rail_fence.decrypt(encrypted, key)
    print(decrypted)