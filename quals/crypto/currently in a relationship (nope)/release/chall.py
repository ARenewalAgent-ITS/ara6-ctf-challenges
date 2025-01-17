from Crypto.PublicKey import RSA

FLAG = open('flag.png', 'rb').read()

def encrypt_block(data, rsa_key):
    num1 = int.from_bytes(data, "big")
    num2 = 24 * num1 + 50
    ct_arr = []
    for num in [num1, num2]:
        if num >= rsa_key.n:
            raise ValueError("num >= n")
        enc = pow(num, rsa_key.e, rsa_key.n)
        ct = enc.to_bytes(1536 // 8, "big")
        ct_arr.append(ct)
    return ct_arr

def split_into_blocks(data, size):
    return [data[i:i+size] for i in range(0, len(data), size)]

blocks = split_into_blocks(FLAG, (1536 // 8) - 1)
key = RSA.generate(1536, e=245)

ct1 = []
ct2 = []
# print(blocks)
for block in blocks:
    enc = encrypt_block(block, key)
    ct1.append(enc[0])
    ct2.append(enc[1])

with open("flag1.enc", "wb") as file:
    file.write(b''.join(ct1))

with open("flag2.enc", "wb") as file:
    file.write(b''.join(ct2))

with open("out.txt", "w") as file:
    file.write(str(key.n))