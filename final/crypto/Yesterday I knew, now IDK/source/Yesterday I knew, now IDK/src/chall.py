from Crypto.Util.number import *
from math import gcd
from sage.all import *
flag= b'ARA6{idk_i_ran_out_of_idea_but_from_this_i_learn_a_lot_coz_trial&error_when_read_various_solution_of_cry_problems}'
m= bytes_to_long(flag)

def init(bit):
        seed = getRandomInteger(bit)
        while seed.bit_length() != bit:
                seed = getRandomInteger(bit)
        return seed

def randomize(seed):
        a = getPrime(384)
        b = getPrime(200)
        return a*seed+b

def genPrime(seed):
    seed_bits = seed.bit_length()
    if seed_bits < 512:
        half_bits = seed_bits // 2
        while True:
            a = getPrime(half_bits)
            b = getPrime(half_bits)
            p = a * seed + b
            if isPrime(p):
                return p

    else:
        R = __import__('random')
        R.seed(seed)
        R = R.randint
        while True:
            p = (ZZ**2).gen(0)
            while p.norm() < 5**85:
                  a,b = ((-1)**R(0,1)*R(1,7**y) for y in (2,1))
                  p *= matrix([[a,b],[123*b,-a]])
            p += (ZZ**2).gen(0)
            p *= diagonal_matrix((1,123)) * p
            if is_pseudoprime(p): 
                  return p

seed = init(384)

print("generating key's flag...")
p,q = genPrime(seed),genPrime(seed)
n = p*q
e = 0x10001
phi = (p-1)*(q-1)
assert gcd(e,phi)==1


print("encrypting flag...")
msg = {}
msg['c'] = pow(m,e,n)
msg['e'] = e
msg['n'] = n
counter = 0
print(f'{msg}\n\n')
print('I give you 5 chances to test this')


while counter < 5:
        user_seed = randomize(seed)
        print("generating new key...")
        p = genPrime(bytes_to_long(str(user_seed)[:len(str(user_seed))//2].encode()))
        q = genPrime(bytes_to_long(str(user_seed)[len(str(user_seed))//2:].encode()))
        n = p*q
        m = bytes_to_long(str(input('your message: ')).encode())
        c = (pow(n+1, user_seed, n*n) * pow(m, n, n*n)) % (n*n)
        msg = {'c':c,'n':n}
        print(msg)
        counter+=1
