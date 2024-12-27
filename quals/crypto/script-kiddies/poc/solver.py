import json
from pwn import *
from Crypto.Util.number import long_to_bytes
from zlib import crc32

#https://github.com/mheistermann/HashPump-partialhash
team_name = b'asdankdjnaksjdnakdn'
team_id = hex(crc32(team_name))[2:]
ending = b"'}"
original_ticket = b"{'ticket': b'"+team_name+b"-"+team_id.encode()



def modify(known,before,after,ciphertext):
	target = xor(before,after)
	idx = known.rfind(before)
	return (ciphertext[:idx]+xor(ciphertext[idx:idx+len(target)],target)+ciphertext[idx+len(target):]).hex()
	

def parse(ticket):
	ticket = bytes.fromhex(ticket)
	data = ticket[:28]
	ct = ticket[28:]
	return data,ct


r = process(['python3', 'chall.py'])
r.sendline(b'g')
r.sendline(team_name)
r.recvuntil(b'is:')
ticket = r.recvline().strip().decode()

#print(ticket)
data,ciphertext = parse(ticket)

print('./hashpump -s "' + data[8:].hex() + '" -d "' + team_name.decode() + '-' + team_id + '" -a "-invited" -k 16')
targets = bytes.fromhex(input('target: '))

for target in targets:
	data,ciphertext = parse(ticket)
	new_ticket = data.hex()+modify(original_ticket+ending, ending, long_to_bytes(target) + b"'", ciphertext)
	print(new_ticket)


	for i in range(256):
		oracle = new_ticket+long_to_bytes(i).hex()
		r.sendline(b'i')
		r.sendline(oracle.encode())
		r.recvline()
		r.recvline()
		r.recvline()
		r.recvline()
		res = r.recvline().strip().decode()
		if not 'Invalid data. Aborting!' in res:
#			print(res,oracle)
			original_ticket += long_to_bytes(target)
			break
	ticket = oracle

data,ciphertext = parse(ticket)
checksum = input('new hash: ')
ticket = (data[:8].hex()+checksum+ciphertext.hex())
print(ticket)
r.interactive()
