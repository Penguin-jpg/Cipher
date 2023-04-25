# 代換
from affine import Affine
from baconian import Baconian
from gronsfeld import Gronsfeld

# 換位
from railfence import RailFence
from row_transposition import RowTransposition
from grille import Grille

# rsa
from rsa import read_key, encrypt

if __name__ == "__main__":
    # read public key
    public_key = read_key("public_key.pem")

    # key and plaintext
    key = "2g3qp6GOI"
    plaintext = "Ab1c23D7"

    row_transposition = RowTransposition(key)
    baconian = Baconian(key)
    rail_fence = RailFence(key)
    affine = Affine(key)
    grille = Grille(key)
    gronsfeld = Gronsfeld(key)

    methods = [
        row_transposition,
        baconian,
        rail_fence,
        affine,
        grille,
        gronsfeld,
    ]
    ciphertext = plaintext

    for method in methods:
        ciphertext = method.encrypt(ciphertext)
        print("encrypted: ")
        print(ciphertext)
        print()

    encrypted_key = encrypt(key, public_key)
    print("encrypted_key: " + encrypted_key)
