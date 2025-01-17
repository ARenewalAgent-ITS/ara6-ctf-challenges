from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from sage.all import *

def gcd(a, b): 
    while b:
        a, b = b, a % b
    return a.monic()

def franklinreiter(C1, C2, e, N, a, b):
    P.<X> = PolynomialRing(Zmod(N))
    g1 = (a*X + b)^e - C1
    g2 = X^e - C2
    result = -gcd(g1, g2).coefficients()[0]
    if result < 0:
        result = -result
    return hex(int(result))[2:]


def main():
    block = 192
    n = int(open("out.txt", 'r').read())
    enc1 = open("flag1.enc", 'rb').read()
    enc2 = open("flag2.enc", 'rb').read()
    png_bytes = b""
    for i in range(0, len(enc2), block):
        m = franklinreiter(b2l(enc2[i:i+block]), b2l(enc1[i:i+block]), 245, n, 24, 50)
        m = m.zfill(382)
        png_bytes += bytes.fromhex(m)
    
    with open("test.png", 'wb') as f:
        f.write(png_bytes)
        f.close()
    print("DONE CUY, CEK flag.png")

main()
