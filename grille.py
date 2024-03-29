import string
import re

"""
流程: 
 - key:
    如果key長度不到9，就補1補到長度9
- 加解密:
    目前和原本的6x6 Grille cipher一樣
"""


class Grille:
    def __init__(self, key, num_groups=9, num_members=4):
        # initialize the selection groups of grille matrix position (base on 6 x 6 grille matrix)
        self.num_groups = num_groups
        self.num_members = num_members
        self.position_matrix = [[0] * num_members for _ in range(self.num_groups)]
        self.position_matrix = [
            [1, 6, 36, 31],
            [2, 12, 35, 25],
            [3, 18, 34, 19],
            [13, 4, 24, 33],
            [7, 5, 30, 32],
            [8, 11, 29, 26],
            [9, 17, 28, 20],
            [14, 10, 23, 27],
            [15, 16, 22, 21],
        ]
        self.key_transform_table = "1234567890" + string.ascii_letters + "-+"
        self.key = self._key_transform(key)

    def _key_transform(self, key):
        """Make key valid for Grille cipher"""
        new_key = ""
        # table for key transformation

        # 要確保迴圈正常運行
        for i in range(min(len(key), self.num_groups)):
            key_index = self.key_transform_table.index(key[i])
            new_key += str(key_index % 4 + 1)

        # 長度不到9要補1
        if len(new_key) < self.num_groups:
            new_key += "1" * (self.num_groups - len(new_key))

        return new_key

    def encrypt(self, plaintext):
        """Encrpyt plaintext using Grille cipher"""
        # store the input key into the position_key array
        position_key = [int(self.key[i]) - 1 for i in range(self.num_groups)]
        # the array to store the selected position of the grille matrix
        selected_position = [0] * self.num_groups
        # encrypted result
        ciphertext = ""
        # check if the remain string length is larger than 36 or not
        larger_than_36 = False

        # in while loop do the encrypt part
        while True:
            # if the length of text is longer than 36, encrypt the text partially
            if len(plaintext) > 36:
                temp_text = plaintext[0:36]
                plaintext = plaintext[36:]
                larger_than_36 = True
            else:
                larger_than_36 = False
                # pad length to 36
                if len(plaintext) < 36:
                    plaintext += "=" * (36 - len(plaintext))

            for _ in range(self.num_members):
                for j in range(self.num_groups):
                    selected_position[j] = self.position_matrix[j][position_key[j]]
                    position_key[j] = (position_key[j] + 1) % 4
                selected_position.sort()
                for j in range(self.num_groups):
                    ciphertext += (
                        temp_text[selected_position[j] - 1]
                        if larger_than_36
                        else plaintext[selected_position[j] - 1]
                    )

            if not larger_than_36:
                break

        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Grille cipher"""
        # store the input key into the position_key array
        position_key = [int(self.key[i]) - 1 for i in range(self.num_groups)]
        # the array to store the selected position of the grille matrix
        selected_position = [0] * self.num_groups
        # decryted result
        plaintext = ""
        # the array to store the decrypt text character
        decrypt_array = ["0"] * (self.num_groups * self.num_members)
        # check if the remain string length is larger than 36 or not
        larger_than_36 = False

        # in while loop do the decrypt part
        while True:
            if len(ciphertext) > 36:
                temp_text = ciphertext[0:36]
                ciphertext = ciphertext[36:]
                larger_than_36 = True
            else:
                larger_than_36 = False

            for i in range(self.num_members):
                for j in range(self.num_groups):
                    selected_position[j] = self.position_matrix[j][position_key[j]]
                    position_key[j] = (position_key[j] + 1) % 4
                selected_position.sort()
                for j in range(self.num_groups):
                    decrypt_array[selected_position[j] - 1] = (
                        temp_text[i * self.num_groups + j]
                        if larger_than_36
                        else ciphertext[i * self.num_groups + j]
                    )

            plaintext += "".join(decrypt_array)
            if not larger_than_36:
                # 找出所有包含"="的位置
                positions_of_equal = [it.start() for it in re.finditer("=", plaintext)]

                # 某些特殊情況下，在只有一個等號且該等號在最後一個字的情況下不能山
                if len(positions_of_equal) == 1 and positions_of_equal[0] == len(plaintext) - 1:
                    break

                # 刪掉多餘的符號
                for position in positions_of_equal:
                    if self._all_equal_behind(plaintext, position):
                        return plaintext[:position]
                break

        return plaintext

    def _all_equal_behind(self, text, start):
        """Check if there are any char other than '=' from 'start'"""
        for i in range(start, len(text)):
            if text[i] != "=":
                return False
        return True


if __name__ == "__main__":
    # input the text and key to start encrypt (the key must be 9 numbers string in range 1~4)
    input_text1 = "ThismagazineisavailableinanybigcityinJapanShemiscalculatedtheamountofbrothinhersoupandinadvertentlyboileditalloff"
    input_text2 = "456ThismagazineisavailableinanybigcityinJapanShemiscalculatedtheamountofbrothinhersoupandinadvertentlyboileditalloff123"
    key = "DeT3Qhx6j8SQ7OL6PwlsHjcha9JUpyXD"
    num_groups, num_members = 9, 4
    grille = Grille(key, num_groups, num_members)

    print("input text1: " + input_text1)
    encrypted_text1 = grille.encrypt(input_text1)
    print("encrypted text1: " + encrypted_text1)
    decrypted_text1 = grille.decrypt(encrypted_text1)
    print("decrypted text1: " + decrypted_text1)

    print("input text2: " + input_text2)
    encrypted_text2 = grille.encrypt(input_text2)
    print("encrypted text2: " + encrypted_text2)
    decrypted_text2 = grille.decrypt(encrypted_text2)
    print("decrypted text2: " + decrypted_text2)
