# 代換
from affine import Affine
from baconian import Baconian
from gronsfeld import Gronsfeld

# 換位
from railfence import RailFence
from row_transposition import RowTransposition
from grille import Grille

key = "joSFzkRgUgjhoz4RWkAhBLRnwho8ZAm7"
encrypted = ""

row_transposition = RowTransposition(key)
baconian = Baconian()
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

decrypted = encrypted
for method in methods[::-1]:
    decrypted = method.decrypt(decrypted)
    print("decrypted: ")
    print(decrypted)
    print()
