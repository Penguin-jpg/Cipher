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
    encrypted_key = "bLYYdLMJPpXr0/VYwG8sNwi/6mJ0j4Hzmmk7HiCAGj/Rp7p4T3zmYhXpIejZm/tQqZmCXlHWqmQicPLQV5Y6cZTc3f1WKrWT0f0/ijSA5Puy2TYpmIwOxTevnLmL+i0HxiTMschG7qV6JQIrbabWx292I56Wl8Y9RxSD2RY9MrI="
    ciphertext = "CrzmxfFgDFiFmxfFgDc-FmxfFgD7FYqxfFgD"

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
