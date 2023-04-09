class Grille:
    def __init__(self, key, num_groups=9, num_members=4):
        # initialize the selection groups of grille matrix position (base on 6 x 6 grille matrix)
        self.key = key
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

    def encrypt(self, plaintext):
        """Encrpyt plaintext using Grille cipher"""
        # store the input key into the position_key array
        position_key = [int(self.key[i]) - 1 for i in range(self.num_groups)]
        # the array to store the selected position of the grille matrix
        selected_position = [0] * self.num_groups
        # encrypted result
        encrypted = ""
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
                    encrypted += (
                        temp_text[selected_position[j] - 1]
                        if larger_than_36
                        else plaintext[selected_position[j] - 1]
                    )

            if not larger_than_36:
                break

        return encrypted

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Grille cipher"""
        # store the input key into the position_key array
        position_key = [int(self.key[i]) - 1 for i in range(self.num_groups)]
        # the array to store the selected position of the grille matrix
        selected_position = [0] * self.num_groups
        # decryted result
        decrypted = ""
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

            decrypted += "".join(decrypt_array)
            if not larger_than_36:
                # find where x is and cut there
                position_of_x = decrypted.find("=")
                if position_of_x != -1:
                    return decrypted[:position_of_x]
                break

        return decrypted


if __name__ == "__main__":
    # input the text and key to start encrypt (the key must be 9 numbers string in range 1~4)
    input_text1 = "thisistesttextwithover36numbersandalphabetsa1085509"
    input_text2 = "shortertextwithin36length"
    input_text3 = "abcdefghijklmnopqrstuvwxyz012345678"
    key = "143424314"
    num_groups, num_members = 9, 4
    grille = Grille(key, num_groups, num_members)

    # encrypt_text1 = grille_encrpyt(input_text1, input_key, selection_group)
    print("input text1: " + input_text1)
    encrypted_text1 = grille.encrypt(input_text1)
    print("encrypted text1: " + encrypted_text1)
    # decrypt_text1 = grille_decrypt(encrypt_text1, input_key, selection_group)
    decrypted_text1 = grille.decrypt(encrypted_text1)
    print("decrypted text1: " + decrypted_text1)

    # encrypt_text1 = grille_encrpyt(input_text1, input_key, selection_group)
    print("input text2: " + input_text2)
    encrypted_text2 = grille.encrypt(input_text2)
    print("encrypted text2: " + encrypted_text2)
    # decrypt_text1 = grille_decrypt(encrypt_text1, input_key, selection_group)
    decrypted_text2 = grille.decrypt(encrypted_text2)
    print("decrypted text2: " + decrypted_text2)

    # encrypt_text1 = grille_encrpyt(input_text1, input_key, selection_group)
    print("input text3: " + input_text3)
    encrypted_text3 = grille.encrypt(input_text3)
    print("encrypted text3: " + encrypted_text3)
    # decrypt_text1 = grille_decrypt(encrypt_text1, input_key, selection_group)
    decrypted_text3 = grille.decrypt(encrypted_text3)
    print("decrypted text3: " + decrypted_text3)
