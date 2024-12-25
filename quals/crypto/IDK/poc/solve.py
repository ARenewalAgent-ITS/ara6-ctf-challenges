from libnum import n2s


def extract(hint,bit):
    value = []
    while hint:
        hint >>= 1
        if hint % 2 == 1:
            value.append(n2s(hint & (2**bit-1)))
            hint >>= bit
    return value

treat = int(input('treat: '))
print(extract(treat,191))
