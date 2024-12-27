import dis

code = """
def conv(str, l=5):
    for i in range(0, len(str), l):
        yield str[i:i + l]

flag = open("flag.txt").read()
flags = []
N = [412881107802, 397653008560, 378475773842, 412107467700, 410815948500, 424198405792, 379554633200, 404975010927, 419449858501, 383875726561]
NR = reversed(N)

assert len(flag) % 5 == 0 

for i, j, k in zip(conv(flag), N, NR):
    x = int.from_bytes(i.encode(), 'big')
    y = ( x + j ) * 1337 ^ k
    y -= 871366131
    flags.append(y)
    
print(flags)
"""

# Compile the code and disassemble it into bytecode
compiled_code = compile(code, "<string>", "exec")
dis.dis(compiled_code)
