# 代換
from affine import Affine
from baconian import Baconian
from gronsfeld import Gronsfeld

# 換位
from railfence import RailFence
from row_transposition import RowTransposition
from grille import Grille

key = "joSFzkRgUgjhoz4RWkAhBLRnwho8ZAm7"
answer = "789Yesphilosophicallyspeakingalltweetsarebadbuttobefullyhumanistorebelagainstthisfacttosendourterribletweetsoutintotheuniverseanyway44256321"
encrypted = "OoaQaZHYF5vaTK7zH64UGfER+=W7xbgUG1isjLLgHkz4-Tk8aYLYhFEeDwUO6sifFAMm5B3tqetvtpxr=8Hyf+ep85eo55n6M51eQRrT=mGqiKYzKaKhvmGr9j1hXfgnO+UKFb2HJQPC8CqM"

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

plaintext = encrypted
for method in methods:
    plaintext = method.decrypt(plaintext)
    print("decrypted: ")
    print(plaintext)
    print()

if plaintext == answer:
    print("!")
