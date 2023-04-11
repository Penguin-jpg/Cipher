"""
Code is based on https://www.geeksforgeeks.org/baconian-cipher/
"""


class Baconian:
    def __init__(self):
        # Added Numbers and an extra digit, because 2**6 > 36 > 2**5.
        # Letters end in a, numbers end in b.
        self.table = {
            "A": "aaaaaa",
            "B": "aaaaba",
            "C": "aaabaa",
            "D": "aaabba",
            "E": "aabaaa",
            "F": "aababa",
            "G": "aabbaa",
            "H": "aabbba",
            "I": "abaaaa",
            "J": "abaaba",
            "K": "ababaa",
            "L": "ababba",
            "M": "abbaaa",
            "N": "abbaba",
            "O": "abbbaa",
            "P": "abbbba",
            "Q": "baaaaa",
            "R": "baaaba",
            "S": "baabaa",
            "T": "baabba",
            "U": "babaaa",
            "V": "bababa",
            "W": "babbaa",
            "X": "babbba",
            "Y": "bbaaaa",
            "Z": "bbaaba",
            "0": "aaaaab",
            "1": "aaaabb",
            "2": "aaabab",
            "3": "aaabbb",
            "4": "aabaab",
            "5": "aababb",
            "6": "aabbab",
            "7": "aabbbb",
            "8": "abaaab",
            "9": "abaabb",
        }
        self.reverse_table = {value: key for key, value in self.table.items()}

    def encrypt(self, plaintext):
        """Encrypt plaintext using Baconian cipher"""
        encrypted = ""
        for char in plaintext:
            encrypted += self.table[char] if char != " " else " "
        return encrypted

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Baconian cipher"""
        decrypted = ""
        while len(ciphertext) > 0:
            sub = ciphertext[:6]
            if sub[0] != " ":
                decrypted += self.reverse_table[sub]
                ciphertext = ciphertext[6:]
            else:
                decrypted += " "
                ciphertext = ciphertext[1:]
        return decrypted


if __name__ == "__main__":
    # key = ""
    plaintext = "helloworld123"
    baconian = Baconian()
    encrypted = baconian.encrypt(plaintext.upper())
    print("encrypted: " + encrypted)
    decrypted = baconian.decrypt(encrypted)
    print("decryted: " + decrypted.lower())
