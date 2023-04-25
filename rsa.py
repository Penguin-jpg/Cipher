from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
import base64


def generate_keys(bits):
    private_key = RSA.generate(bits)
    private_key = private_key
    public_key = private_key.public_key()

    with open("private_key.pem", "wb") as file:
        file.write(private_key.export_key())

    with open("public_key.pem", "wb") as file:
        file.write(public_key.export_key())

    print("keys generated!")


def read_key(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
        key = RSA.import_key(data)
    return key


def encrypt(plaintext, public_key):
    cipher = PKCS1_cipher.new(public_key)
    ciphertext = base64.b64encode(cipher.encrypt(plaintext.encode("utf-8")))
    return ciphertext.decode("utf-8")


def decrypt(ciphertext, private_key):
    cipher = PKCS1_cipher.new(private_key)
    plaintext = cipher.decrypt(base64.b64decode(ciphertext), 0)
    return plaintext.decode("utf-8")


if __name__ == "__main__":
    generate_keys(1024)
    private_key, public_key = read_key("private_key.pem"), read_key("public_key.pem")
    key = "2g3qp6GOI"
    plaintext = "Ab1c23D7"

    encrypted = encrypt(plaintext, public_key)
    print("encrypted_text: " + encrypted)

    decrypted = decrypt(encrypted, private_key)
    print("decrypted_text: " + decrypted)

    if decrypted == plaintext:
        print("!")
