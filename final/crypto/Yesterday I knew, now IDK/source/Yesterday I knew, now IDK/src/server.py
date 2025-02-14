from Crypto.Util.number import *
from math import gcd
from sage.all import *
import time

class IDK:
    def __init__(self, bit_length):
        self.bit_length = bit_length
        self.seed = self.gen_seed()
        self.e = 0x10001
        self.p, self.q = self.gen_primes()
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        assert gcd(self.e, self.phi) == 1

    def gen_seed(self):
        seed = getRandomInteger(self.bit_length)
        while seed.bit_length() != self.bit_length:
            seed = getRandomInteger(self.bit_length)
        return seed

    def gen_prime(self, seed):
        start_time = time.time()
        seed_bits = seed.bit_length()
        
        if seed_bits < 512:
            half_bits = seed_bits // 2
            while True:
                if time.time() - start_time > 10:
                    return None
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
                    a, b = ((-1)**R(0,1) * R(1,7**y) for y in (2,1))
                    p *= matrix([[a, b], [123*b, -a]])
                p += (ZZ**2).gen(0)
                p *= diagonal_matrix((1, 123)) * p
                if is_pseudoprime(p): 
                    return p

    def gen_primes(self):
        print("Generating key's flag...")
        while True:
            p = self.gen_prime(self.seed)
            if p is None:
                self.seed = self.gen_seed()
                continue
            return p, self.gen_prime(self.seed)

    def gen_flag(self, message):
        print("encrypting flag...")
        m = bytes_to_long(message)
        c = pow(m, self.e, self.n)
        return {'c': c, 'e': self.e, 'n': self.n}

    def randomize_seed(self, seed):
        a = getPrime(384)
        b = getPrime(200)
        return a * seed + b

    def user_test(self, max=5):
        print("I give you 5 chances to test this")
        counter = 0
        while counter < max:
            user_seed = self.randomize_seed(self.seed)
            print("Generating new key...")
            p = self.gen_prime(bytes_to_long(str(user_seed)[:len(str(user_seed))//2].encode()))
            q = self.gen_prime(bytes_to_long(str(user_seed)[len(str(user_seed))//2:].encode()))
            n = p * q
            m = bytes_to_long(str(input('Your message: ')).encode())
            c = (pow(n+1, user_seed, n*n) * pow(m, n, n*n)) % (n*n)
            print({'c': c, 'n': n})
            counter += 1
        print("Thanks")
        

if __name__ == "__main__":
    flag = b'ARA6{idk_i_ran_out_of_idea_but_from_this_i_learn_a_lot_coz_trial&error_when_read_various_solution_of_cry_problems}'
    for_u = IDK(384)
    print(for_u.gen_flag(flag), "\n\n")
    for_u.user_test()
