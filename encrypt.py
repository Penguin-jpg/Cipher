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

    # 正常測資
    # key = "2g3qp6GO"
    # plaintext = "Ab1c23D7"

    # 明文中有"x"的測資且解出的尾巴不是"x"
    # key = "nfrNVALs"
    # plaintext = "ymixeZLG"

    # 明文中有"x"且解出來的尾巴是"x"的測資
    # key = "OTgdMeio"
    # plaintext = "cxTjQV8J"

    # 明文的"x"在尾巴(無解)
    # key = "SD1I9Ger"
    # plaintext = "zbCPS7ix"

    # 正常測資(測出affine不應該可以加密出"=")
    key = "zggN57o7"
    plaintext = "raNitPfe"

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
