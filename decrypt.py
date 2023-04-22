# 代換
from affine import Affine
from baconian import Baconian
from gronsfeld import Gronsfeld

# 換位
from railfence import RailFence
from row_transposition import RowTransposition
from grille import Grille

key = "joSFzkRgUgjhoz4RWkAhBLRnwho8ZAm7"
encrypted = "YYrTDyKbMnhvaw+JYkrmd3KjwngX1AhWAyOBkyRxQhjepnR4-lEcpUGvrtc8-sEOhFOEDbRaUoevDk+JIpAfi2LFsknYNlF+yFKEso4qQcAvanRJ9zuuCH+aEskTHEm2ryShHYD+uX+Y"

gronsfeld = Gronsfeld(key)
grille = Grille(key)
affine = Affine(key)
rail_fence = RailFence(key)
baconian = Baconian(key)
row_transposition = RowTransposition(key)


methods = [
    # gronsfeld,
    # grille,
    # affine,
    # rail_fence,
    # baconian,
    row_transposition,
]

plaintext = encrypted
for method in methods:
    plaintext = method.decrypt(plaintext)
    print("decrypted: ")
    print(plaintext)
    print()
