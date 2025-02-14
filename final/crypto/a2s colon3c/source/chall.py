lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll = __name__, range, set, bool, open

from os import urandom as lIIllIlIIIIllI
from aes import AES as lIlIIIlIllIIIl
from utils import *
from flag import *
IlllIlllIIIlIIIllI = lIIllIlIIIIllI(16)

def IllIlIlIlllIIllIll(IIIllIlllllIlIlIlI):
    IIIlIIllIIIIllIIlI = lIlIIIlIllIIIl(IlllIlllIIIlIIIllI, 2)
    lIllIlIIlIIIlIIIII = IIIlIIllIIIIllIIlI._key_matrices
    llIlIlllllllllIllI = IIIlIIllIIIIllIIlI.encrypt_block(IIIllIlllllIlIlIlI)
    llIlIlllllllllIllI = bytes2matrix(llIlIlllllllllIllI)
    add_round_key(llIlIlllllllllIllI, lIllIlIIlIIIlIIIII[-1])
    mix_columns(llIlIlllllllllIllI)
    add_round_key(llIlIlllllllllIllI, lIllIlIIlIIIlIIIII[-1])
    return matrix2bytes(llIlIlllllllllIllI)

def IIlIllIIIIIllIlllI(lIlIlIllIllIllIIIl, llIlIIIlIIlIIlIIll):
    IIIlIIllIIIIllIIlI = lIlIIIlIllIIIl(llIlIIIlIIlIIlIIll, 2)
    lIllIlIIlIIIlIIIII = IIIlIIllIIIIllIIlI._key_matrices
    llIlIlllllllllIllI = bytes2matrix(lIlIlIllIllIllIIIl)
    add_round_key(llIlIlllllllllIllI, lIllIlIIlIIIlIIIII[-1])
    inv_mix_columns(llIlIlllllllllIllI)
    add_round_key(llIlIlllllllllIllI, lIllIlIIlIIIlIIIII[-1])
    return IIIlIIllIIIIllIIlI.decrypt_block(matrix2bytes(llIlIlllllllllIllI))

def IlllIllIIlIIIIlllI(IlllllIIIllIIIIIlI=5):
    while lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1):
        IIIIlIIllIllIllIlI = [lIIllIlIIIIllI(4) for lIIllIIIlIllIIlIIl in llllllllllllllI(IlllllIIIllIIIIIlI)]
        llIIIllllIIIIlIIlI = lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
        for lllIllIlIlIIIIlIII in llllllllllllllI(4):
            lllIllllIIlIIlllIl = lllllllllllllIl()
            for lIIIIlIllIlIlIIIll in llllllllllllllI(IlllllIIIllIIIIIlI):
                IIlIllIIIIlIIIlllI = IIIIlIIllIllIllIlI[lIIIIlIllIlIlIIIll][lllIllIlIlIIIIlIII]
                if IIlIllIIIIlIIIlllI in lllIllllIIlIIlllIl:
                    llIIIllllIIIIlIIlI = lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
                    break
                lllIllllIIlIIlllIl.add(IIlIllIIIIlIIIlllI)
            if not llIIIllllIIIIlIIlI:
                break
        if llIIIllllIIIIlIIlI:
            IIIllllIllllIlllII = [IllIlIlIlllIIllIll(lIIllIIIlIlIllIllI + b'\x00' * 12) for lIIllIIIlIlIllIllI in IIIIlIIllIllIllIlI]
            IlIIIIIIIIlIllIIIl = [[IIIIlIIllIllIllIlI[lllIllIlIlIIIIlIII] + b'\x00' * 12, IIIIlIIllIllIllIlI[lIIIIlIllIlIlIIIll] + b'\x00' * 12, IIIllllIllllIlllII[lllIllIlIlIIIIlIII], IIIllllIllllIlllII[lIIIIlIllIlIlIIIll]] for lllIllIlIlIIIIlIII in llllllllllllllI(IlllllIIIllIIIIIlI - 1) for lIIIIlIllIlIlIIIll in llllllllllllllI(lllIllIlIlIIIIlIII + 1, IlllllIIIllIIIIIlI)]
            return IlIIIIIIIIlIllIIIl

def IlIlIlllIllIlIIIIl():
    IlIIIIIIIIlIllIIIl = IlllIllIIlIIIIlllI()
    for lIlIIllllIlllllllI in IlIIIIIIIIlIllIIIl:
        with llllllllllllIll('pairs.txt', 'a') as lllllIllllIlllIllI:
            lllllIllllIlllIllI.write(lIlIIllllIlllllllI[0].hex() + '\n' + lIlIIllllIlllllllI[1].hex() + '\n' + lIlIIllllIlllllllI[2].hex() + '\n' + lIlIIllllIlllllllI[3].hex() + '\n\n')
    lllIIIlIlllIIIIIII = IllIlIlIlllIIllIll(FLAG1)
    IllIlIIlIlllllIIII = IllIlIlIlllIIllIll(FLAG2)
    IIlIIIlllIlIIllIlI = IllIlIlIlllIIllIll(FLAG3)
    with llllllllllllIll('out.txt', 'w') as lllllIllllIlllIllI:
        lllllIllllIlllIllI.write(lllIIIlIlllIIIIIII.hex() + '\n' + IllIlIIlIlllllIIII.hex() + '\n' + IIlIIIlllIlIIllIlI.hex())
if lllllllllllllll == '__main__':
    IlIlIlllIllIlIIIIl()