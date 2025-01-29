from aes import AES
from utils import *
from flag import *
import os

KEY = os.urandom(16)

def encrypt(plaintext):
    aes = AES(KEY, 2)
    key_expand = aes._key_matrices

    state = aes.encrypt_block(plaintext)
    state = bytes2matrix(state)
    add_round_key(state, key_expand[-1])
    mix_columns(state)
    add_round_key(state, key_expand[-1])
    
    return matrix2bytes(state)

def decrypt(ciphertext, key):
    aes = AES(key, 2)
    key_expand = aes._key_matrices
    state = bytes2matrix(ciphertext)
    add_round_key(state, key_expand[-1])
    inv_mix_columns(state)
    add_round_key(state, key_expand[-1])

    return aes.decrypt_block(matrix2bytes(state))

def generate_pairs(n=5):
    while True:
        bs = [os.urandom(4) for _ in range(n)]

        unique = True
        for i in range(4):
            seen = set()
            for j in range(n):
                val = bs[j][i]
                if val in seen:
                    unique = False
                    break
                seen.add(val)
            if not unique:
                break

        if unique:
            ctx = [encrypt(b + b'\x00' * 12) for b in bs]
            pairs = [
                [bs[i] + b'\x00' * 12, bs[j] + b'\x00' * 12, ctx[i], ctx[j]]
                for i in range(n-1) for j in range(i+1, n)
            ]
            return pairs

def main():
    pairs = generate_pairs()
    for p in pairs:
        with open ("pairs.txt", "a") as f:
            f.write(p[0].hex() + "\n" + p[1].hex() + "\n" + p[2].hex() + "\n" + p[3].hex() + "\n\n")
    ct1 = encrypt(FLAG1)
    ct2 = encrypt(FLAG2)
    ct3 = encrypt(FLAG3)
    with open ("out.txt", "w") as f:
        f.write(ct1.hex() + "\n" + ct2.hex() + "\n" + ct3.hex())

if __name__ == "__main__":
    main()