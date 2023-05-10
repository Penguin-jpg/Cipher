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
    encrypted_key = "QLbGtnTeIRJoCpSDT/1sUFPTo0gkIS43JYfoZvTkKjwQ3agI4GCvYysqpy4DU1M33OOeP15b2tXwbx23J7Rp2PkdLS0W/YtXbkXPB51lzZDmRHxNrWYOce8L6u7y2T8lF665HCB2BvkaR6Bm6LJcMQlizQC/q4bgXTYOQaOYQQs="
    ciphertext = "EAE04|E04y`ZT(@04|W04|E04|E04|E04|E0"

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
