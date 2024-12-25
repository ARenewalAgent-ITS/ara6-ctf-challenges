from Crypto.Util.number import *
from sympy import nextprime
from Crypto.Util.Padding import pad

n = 8
flag = pad(b'ajkjdnkajndkjansdaihanjbjabsjdbasdhajbdjasbdjhasbjdabsjdhabsjdbajsdbjasbdjasbdjasbdjabdjadb',n)

assert len(flag)%n == 0

n = len(flag)//n
flag = [flag[i:i+n] for i in range(0,len(flag),n)]
c = sum([nextprime(bytes_to_long(flag[i]))*2**(0x1337-158*(2*i+1)) for i in range(len(flag))])

print(c)
