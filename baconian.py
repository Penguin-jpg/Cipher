"""
Code is based on https://www.geeksforgeeks.org/baconian-cipher/
"""


class Baconian:
    def __init__(self):
        # Added Numbers and an extra digit, because 2**6 > 36 > 2**5.
        # Added lowercase letters, which can fit, since 2**6 > 62
        self.table = {
            "A": "aaaaaa",
            "B": "aaaaab",
            "C": "aaaaab",
            "D": "aaaabb",
            "E": "aaabaa",
            "F": "aaabab",
            "G": "aaabba",
            "H": "aaabbb",
            "I": "aabaaa",
            "J": "aabaab",
            "K": "aababa",
            "L": "aababb",
            "M": "aabbaa",
            "N": "aabbab",
            "O": "aabbba",
            "P": "aabbbb",
            "Q": "abaaaa",
            "R": "abaaab",
            "S": "abaaba",
            "T": "abaabb",
            "U": "ababaa",
            "V": "ababab",
            "W": "ababba",
            "X": "ababbb",
            "Y": "abbaaa",
            "Z": "abbaab",
            "a": "abbaba",
            "b": "abbabb",
            "c": "abbbaa",
            "d": "abbbab",
            "e": "abbbba",
            "f": "abbbbb",
            "g": "baaaaa",
            "h": "baaaab",
            "i": "baaaba",
            "j": "baaabb",
            "k": "baabaa",
            "l": "baabab",
            "m": "baabba",
            "n": "baabbb",
            "o": "babaaa",
            "p": "babaab",
            "q": "bababa",
            "r": "bababb",
            "s": "babbaa",
            "t": "babbab",
            "u": "babbba",
            "v": "babbbb",
            "w": "bbaaaa",
            "x": "bbaaab",
            "y": "bbaaba",
            "z": "bbaabb",
            "0": "bbabaa",
            "1": "bbabab",
            "2": "bbabba",
            "3": "bbabbb",
            "4": "bbbaaa",
            "5": "bbbaab",
            "6": "bbbaba",
            "7": "bbbabb",
            "8": "bbbbaa",
            "9": "bbbbab"
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
    print("plaintext: " + plaintext)
    baconian = Baconian()
    encrypted = baconian.encrypt(plaintext)
    print("encrypted: " + encrypted)
    decrypted = baconian.decrypt(encrypted)
    print("decryted: " + decrypted)
