from Crypto.Cipher import Salsa20
from Crypto.Util.number import bytes_to_long, long_to_bytes
import ast
from secrets import token_bytes, token_hex
from zlib import crc32
import hashlib
import os

FLAG = b'ajdnkandkajsndkasndkandkandkandkandak'
KEY = token_bytes(32)

def verification(key,data):
        return hashlib.sha1(key[:16] + data).hexdigest()


def encrypt_ticket(team_name):
    cipher = Salsa20.new(key=KEY)
    nonce = cipher.nonce
    data={}
    team_id = hex(crc32(team_name.encode()))[2:]
    data['ticket'] = (team_name+'-'+team_id).encode()
    checksum = verification(KEY,data['ticket'])
    data = str(data).encode()
    ciphertext = cipher.encrypt(data)
    print('Your encrypted ticket is:', (nonce + bytes.fromhex(checksum) + ciphertext).hex())


def read_ticket(ticket):
    packet = bytes.fromhex(ticket)
    nonce = packet[:8]
    checksum = packet[8:28].hex()
    ciphertext = packet[28:]
    try:
        cipher = Salsa20.new(key=KEY, nonce=nonce)
        plaintext = str(cipher.decrypt(ciphertext))[2:-1]
        plaintext = ast.literal_eval(plaintext)

        if verification(KEY[:16],plaintext['ticket']) != checksum:
            print('Invalid checksum. Aborting!')
            return

        parsed = plaintext['ticket'].split(b'-')

        if len(parsed) == 3 and parsed[-1] == b'invited':
             print('We have invited and waited for you for a very long time, this for you')
             print(FLAG.decode())
        else:
              print('sorry your team not invited yet, please wait next batch')
              return 0

    except:
        print('Invalid data. Aborting!')


def menu():
    print('[G]et ticket')
    print('[I]nsert ticket')
    print('[Q]uit')


def main():
    print('Welcome to ARA 6.0, Get your ticket here!!\n')
    while True:
        menu()
        option = input('\n>> ').upper()
        if option == 'G':
            team_name = input('Your team name: ')
            encrypt_ticket(team_name)
        elif option == 'I':
            ticket = input('Your encrypted ticket (hex): ')
            if(read_ticket(ticket) == 0):
                exit(0)
        elif option == 'Q':
            exit(0)
        else:
            print('Invalid option!!\n')


if __name__ == '__main__':
    main()
