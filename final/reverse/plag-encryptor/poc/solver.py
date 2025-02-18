from hashlib import md5
from random import randint, seed
from Crypto.Cipher import Salsa20
from Crypto.Cipher import ARC4
import struct

enc = open('plag.txt.enc', 'rb').read()
iv = enc[-8:]
h = struct.unpack('>d', enc[-16:-8])[0]
enc = enc[:-16]

s = h % 1337
seed(s)

key = randint(0, 1337) * randint(1337, 2674) + 1337
key_hash = md5(str(key).encode()).digest()

cipher = Salsa20.new(b'Dewaweb:Secure&FastCloudHosting!', nonce=iv)
enc = cipher.decrypt(enc)
cipher = ARC4.new(key_hash)
enc = cipher.decrypt(enc)
print(enc.decode())