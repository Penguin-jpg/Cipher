# 代換
from affine import Affine
from baconian import Baconian
from gronsfeld import Gronsfeld

# 換位
from railfence import RailFence
from row_transposition import RowTransposition
from grille import Grille

import secrets
import string
from functools import partial


def random_generate(
    length,
    num_results,
    available_chars,
):
    results = set()
    pickchar = partial(secrets.choice, available_chars)
    while len(results) < num_results:
        results |= {"".join([pickchar() for _ in range(length)]) for _ in range(num_results - len(results))}
    return results


def test(key, plaintext):
    # 加密用
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
    encrypted = plaintext
    print(f"加密(key: {key}, text: {plaintext}):")
    for method in methods:
        encrypted = method.encrypt(encrypted)
        print("encrypted: ")
        print(encrypted)
        print()

    # 解密用
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

    print("解密:")
    print()
    decrypted = encrypted
    for method in methods[::-1]:
        decrypted = method.decrypt(decrypted)
        print("decrypted: ")
        print(decrypted)
        print()

    if decrypted == plaintext:
        print("解密成功!\n")
        return True

    print(f"key: {key}, text: {plaintext} 解密失敗\n")
    return False


if __name__ == "__main__":
    AVAILABLE_CHARS = string.ascii_letters + string.digits
    KEY_LENGTH = 8
    NUM_ITERS = 10
    PLAINTEXT_LENGTH = 8
    keys = list(random_generate(KEY_LENGTH, NUM_ITERS, AVAILABLE_CHARS))
    plaintexts = list(random_generate(PLAINTEXT_LENGTH, NUM_ITERS, AVAILABLE_CHARS))

    counter = 0

    for i in range(NUM_ITERS):
        if test(keys[i], plaintexts[i]):
            counter += 1
    print(f"總共測試次數: {NUM_ITERS}, 成功次數: {counter}")
