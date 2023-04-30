# 代換
from affine import Affine
from baconian import Baconian
from gronsfeld import Gronsfeld

# 換位
from railfence import RailFence
from row_transposition import RowTransposition
from grille import Grille

# rsa
from rsa import read_key, decrypt


if __name__ == "__main__":
    answer = "Ab1c23D7"

    # read private key
    private_key = read_key("private_key.pem")

    # read from qr code
    encrypted_key = "jB+ZY78157cdS1/9Ani9sX4PiBylUDY8OdmF+mJcAUTO3UQpioW4Y5oDRNdGOuGwoDdVpxBObyQ4OuEy4Ca9bGfpilEd5/tHJCr/kIHMLX1V1zltAodquqcfdMw54GYE2PShpdINLlHZp+3sCFOTtBFBSB6GzE0KX6CxkYbrzZg="
    ciphertext = "-|.fp<j.DXd;/tJreXMCPUBM3x+V}<_4owq("

    # decrypt key
    key = decrypt(encrypted_key, private_key)

    gronsfeld = Gronsfeld(key)
    grille = Grille(key)
    affine = Affine(key)
    rail_fence = RailFence(key)
    baconian = Baconian(key)
    row_transposition = RowTransposition(key)

    methods = [
        gronsfeld,
        grille,
        affine,
        rail_fence,
        baconian,
        row_transposition,
    ]

    plaintext = ciphertext
    for method in methods:
        plaintext = method.decrypt(plaintext)
        print("decrypted: ")
        print(plaintext)
        print()

    if plaintext == answer:
        print("!")
