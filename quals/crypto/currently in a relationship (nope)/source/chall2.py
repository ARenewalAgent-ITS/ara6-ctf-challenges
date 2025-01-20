from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

password = b"withintemptation"
assert len(password) == 16 or len(password) == 24 or len(password) == 32

with open("flag2.txt", "rb") as f:
    flag = f.read()

cipher = AES.new(password, AES.MODE_ECB)
padded = pad(flag, AES.block_size)
encrypted = cipher.encrypt(padded)

with open("flag2.enc", "wb") as f:
    f.write(encrypted)