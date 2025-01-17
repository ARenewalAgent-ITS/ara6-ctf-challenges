from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import string

with open('flag2.enc', 'rb') as enc_file:
    ciphertext = enc_file.read()

def is_valid_plaintext(text):
    try:
        text.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False

with open('wordlist.txt', 'r') as wordlist_file:
    passwords = [line.strip() for line in wordlist_file]

valid_passwords = [
    pwd for pwd in passwords
    if all(c in string.ascii_letters + string.digits for c in pwd)
    and len(pwd.encode()) in [16, 24, 32]
]

for pwd in valid_passwords:
    print(f"Trying password: {pwd}")
    key = pwd.encode()
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = b""
        for i in range(0, len(ciphertext), AES.block_size):
            block = ciphertext[i:i+AES.block_size]
            decrypted_block = cipher.decrypt(block)
            decrypted += decrypted_block
        plaintext = unpad(decrypted, AES.block_size)
        if is_valid_plaintext(plaintext):
            print(f"Password found: {pwd}")
            print(f"Decrypted message: {plaintext.decode()}")
            break
    except:
        continue