# Simple Math

Author: Haalloobim

---------

## POC / Solver

- Diberikan sebuah python byte code yang berfungsi untuk mengenkripsi sebuah flag.
- Untuk menganalisis byte code, bisa menggunakan ChatGPT atau bisa menganalisis secara manual dengan mengikuti panduan dari link berikut: [Byte Code Docs](https://docs.python.org/3/library/dis.html)
- Setelah melakukan analisis byte code tersebut, didapatkan sebuah python code yang kurang lebih seperti berikut: 

```py
def conv(str, l=5):
    for i in range(0, len(str), l):
        yield str[i:i+l]

with open("flag.txt") as f:
    flag = f.read()

flags = []
N = [412881107802, 397653008560, 378475773842, 412107467700, 410815948500,
     424198405792, 379554633200, 404975010927, 419449858501, 383875726561]
NR = reversed(N)

# Assert that the length of the flag modulo 5 is 0
assert len(flag) % 5 == 0

for i, j, k in zip(conv(flag), N, NR):
    x = int.from_bytes(i.encode(), 'big')
    y = (x + j) * 1337 ^ k
    y -= 871366131
    flags.append(y)

print(flags)
```

- Dari kode tersebut dapat diketahui bahwa flag dibagi menjadi sebuah block block uyang terdiri atas 5 karakter. Kemudian dilakukan operasi matematika sederhana dan hasil dari operasi matematika tersebut di outputkan. Dan pada challenge ini berfokus untuk mencari nilai `x` karena nilai tersebut adalah representasi dari flag yang telah dibagi.

- Proses reverse dalam operasi matematika tersebut, dapat dilakukan seperti berikut:
```
- y = y + 871366131
- y + 871366131 = ( x + j ) * 1337 ^ k
- (y + 871366131) ^ k = ( x + j ) * 1337
- (y + 871366131) ^ k // 1337 = x + j
- (((y + 871366131) ^ k) // 1337) - j = x
```
- Sehingga rumus untuk mencari x sudah dapat diketahui yaitu `(((y + 871366131) ^ k) // 1337) - j` dengan nilai `y` adalah output, nilai `k` adalah reverse dari list N, dan nilai j adalah list N. 

- Berikut adalah solver dari challenge tersebut:
```py
lst = [927365724618649, 855544946535839, 1075456339888851, 1051300489856216, 854566738228717, 862564607600557, 1107196607637040, 835104762026329, 1108826984434051, 843310935687105]
N = [412881107802, 397653008560, 378475773842, 412107467700, 410815948500, 424198405792, 379554633200, 404975010927, 419449858501, 383875726561]
NR =list(reversed(N))    

for i in range(10):
    awal = (((lst[i] + 871366131) ^ NR[i]) // 1337) - N[i]
    awal = awal.to_bytes(5, 'big').decode()
    print(awal, end='')
```

Flag: `ARA6{8yT3_c0d3_W1Th_51MPl3_m4th_15_345Y____R19ht?}`