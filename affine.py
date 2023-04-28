"""
Code is based on https://www.geeksforgeeks.org/implementation-affine-cipher/
"""

"""
流程: 
 - key:
    第一個key固定取17，第二個key把所有key中字元的ascii總和mod64
- 加解密:
    目前和原本的Affine cipher一樣
"""


class Affine:
    def __init__(self, key):
        self.key = self._key_transform(key)

    def _key_transform(self, key):
        """Make key valid for Affine cipher"""
        new_key = 0
        for char in key:
            new_key += ord(char)
        return [17, new_key % 64]

    def _egcd(self, a, b):
        """Extended Euclidean Algorithm for finding modular inverse"""
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
        return gcd, x, y

    def _mod_inverse(self, a, m):
        gcd, x, _ = self._egcd(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m

    def encrypt(self, plaintext):
        """Encrypt plaintext using Affine cipher"""
        # remove the space in the string
        plaintext = plaintext.replace(" ", "")
        ciphertext = ""
        for char in plaintext:
            # calculate x: 0~9 no change; A~Z is 10~35; a~z is 36~61; + is 62; - is 63
            if ord(char) < ord("A"):
                if ord(char) == ord("+"):
                    x = ord(char) - ord("+") + 62
                elif ord(char) == ord("-"):
                    x = ord(char) - ord("-") + 63
                else:
                    x = ord(char) - ord("0")
            elif ord(char) > ord("Z"):
                x = ord(char) - ord("a") + 36
            else:
                x = ord(char) - ord("A") + 10

            # calculate C: C = (a*P + b) % 64
            x = (self.key[0] * x + self.key[1]) % 64

            # product the Cipher: x = 0~9 -> number 0~9; x = 10~35 -> A~Z; x = 36~61 -> a~z; x = 62 -> +; x = 63 -> -
            if x < 10:
                ciphertext += chr(x + ord("0"))
            elif x < 36:
                ciphertext += chr(x - 10 + ord("A"))
            elif x < 62:
                ciphertext += chr(x - 36 + ord("a"))
            elif x == 62:
                ciphertext += chr(x - 62 + ord("+"))
            elif x == 63:
                ciphertext += chr(x - 63 + ord("-"))

        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using Affine cipher"""
        plaintext = ""
        for char in ciphertext:
            # calculate y: 0~9 no change; A~Z is 10~35; a~z is 36~61; + is 62; - is 63
            if ord(char) < ord("A"):
                if ord(char) == ord("+"):
                    y = ord(char) - ord("+") + 62
                elif ord(char) == ord("-"):
                    y = ord(char) - ord("-") + 63
                else:
                    y = ord(char) - ord("0")
            elif ord(char) > ord("Z"):
                y = ord(char) - ord("a") + 36
            else:
                y = ord(char) - ord("A") + 10

            # calculate P: P = (a^-1 * (C - b)) % 64
            y = (self._mod_inverse(self.key[0], 64) * (y - self.key[1])) % 64

            # product the Plain: y = 0~9 -> number 0~9; y = 10~35 -> A~Z; y = 36~61 -> a~z; y = 62 -> +; y = 63 -> -
            if y < 10:
                plaintext += chr(y + ord("0"))
            elif y < 36:
                plaintext += chr(y - 10 + ord("A"))
            elif y < 62:
                plaintext += chr(y - 36 + ord("a"))
            elif y == 62:
                plaintext += chr(y - 62 + ord("+"))
            elif y == 63:
                plaintext += chr(y - 63 + ord("-"))

        return plaintext


if __name__ == "__main__":
    # key = [17, 20]
    # plaintext = "Hello 123"
    key = "DeT3Qhx6j8SQ7OL6PwlsHjcha9JUpyXD"
    plaintext = "456ThismagazineisavailableinanybigcityinJapanShemiscalculatedtheamountofbrothinhersoupandinadvertentlyboileditalloff123"
    affine = Affine(key)
    encrypted = affine.encrypt(plaintext)
    print("encrypted: " + encrypted)
    decrypted = affine.decrypt(encrypted)
    print("decrypted: " + decrypted)
