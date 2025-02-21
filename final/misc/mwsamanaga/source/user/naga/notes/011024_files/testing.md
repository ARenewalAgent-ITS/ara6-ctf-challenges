Setup:
```
model = LLMManager.get_model(
    "Hastagaras/L3.2-JametMini-3B-MK.III",
)

covertext_dist = LLMMarginal(
    prompt="Alan Turing was",
    max_len=128,
    temperature=1.0,
    k=64,
    lm_model=model
)

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def derive_key(shared_secret, salt, length):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=length,
        salt=salt,
        iterations=100000,
    )
    return kdf.derive(shared_secret.encode())

bytetext = plaintext.encode("utf-8")

cipher_len = len(bytetext) # This is 25 for our thing, the pt was 25, at least
key_salt = b'salting'
shared_private_key = derive_key(shared_secret, key_salt, cipher_len)
assert len(bytetext) == cipher_len
```

Output:
```
"Alan Turing was" + "---SEP---" + stego_decoded
# Alan Turing was---SEP--- a mathematician and computer scientist famous for developing the first practical computer, the Turing Machine. He also proposed the Turing Test, for which the Turing Test is named. He was also a key figure in cracking the German Enigma code during World War II. But he was caught up in a criminal law by the British government and "chemically castrated." He died in 1954 at the age of 41. He was posthumously pardoned for his conviction in 2009. The Alan Turing Act in 2009 also overturned the conviction of many others who were convicted for the same crimes he was convicted for. His
```
