# 代換
from affine import Affine
from baconian import Baconian
from gronsfeld import Gronsfeld

# 換位
from railfence import RailFence
from row_transposition import RowTransposition
from grille import Grille


# key = "DeT3Qhx6j8SQ7OL6PwlsHjcha9JUpyXD"
# plaintext =
# "456ThismagazineisavailableinanybigcityinJapanShemiscalculatedtheamountofbrothinhersoupandinadvertentlyboileditalloff123"
self.key = "joSFzkRgUgjhoz4RWkAhBLRnwho8ZAm7"
plaintext = "789Yesphilosophicallyspeakingalltweetsarebadbuttobefullyhumanistorebelagainstthisfacttosendourterribletweetsoutintotheuniverseanyway44256321"

row_transposition = RowTransposition(self.key)
baconian = Baconian(self.key)
rail_fence = RailFence(self.key)
affine = Affine(self.key)
grille = Grille(self.key)
gronsfeld = Gronsfeld(self.key)

methods = [
    row_transposition,
    baconian,
    rail_fence,
    affine,
    grille,
    gronsfeld,
]
encrypted = plaintext

for method in methods:
    encrypted = method.encrypt(encrypted)
    print("encrypted: ")
    print(encrypted)
    print()

print()
plaintext = encrypted
for i, method in enumerate(methods[::-1]):
    plaintext = method.decrypt(plaintext)
    print("decrypted: ")
    print(plaintext)
    print()

if plaintext == plaintext:
    print("!")
