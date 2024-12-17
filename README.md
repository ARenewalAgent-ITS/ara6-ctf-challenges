# ARA 6.0 CTF CHALLENGES

## Overview

Repository ini digunakan untuk melakukan tracking dan menyimpan setiap challenge CTF mulai dari penyisihan hingga final untuk event ARA 6.0 CTF. Setiap probset harus mengimplementasikan aturan pembuatan challenge dan struktur folder sesuai dengan aturan yang akan disampaikan pada session berikutnya. Segala challenge yang dibuat akan menjadi hak milik ARA 6.0, namun orisinalitas challenge akan tetap menjadi kepemilikan probset masing - masing.

## General Rules

1. Challenge yang dibuat disesuaikan dengan pembagian probset di masing - masing kategori challenge dan difficulty soal penyisihan adalah easy, medium, dan hard secara berturut - turut, dan untuk final akan diratakan dengan difficulty hard.
2. Challenge yang dibuat dilarang untuk menyinggung atau memiliki konten yang isinya mengenai SARA/Politik/Agama/Bad Words, dan hal lainnya yang melanggar etika digital.
3. Probset bertanggung jawab atas setiap challenge yang dibuat.

## Technical Rules

1. Format flag ARA 6.0 CTF adalah **ARA6{sample}**
2. Setiap probset wajib melakukan uji testing challenge yang dibuat dan memastikan challenge tersebut benar - benar dapat dikerjakan.
3. Setiap probset dilarang membuat challenge dengan sifat **guessy**.
4. Setiap challenge yang mengharuskan untuk membuat sebuah connection service wajib menggunakan **docker** dan **docker compose** sebagai automate docker tersebut.
5. Challenge yang diupload dalam Repository ini harus mengikuti aturan struktur folder yang telah ditentukan.

## Folder Structure

Dalam repository ini akan dibagi menjadi 2 bagian subfolder yaitu **quals** dan **final**, yang masing - masing didalamnya akan ada pengkategorian folder.

```
.
├── final
│   ├── crypto
│   ├── forensic
│   ├── misc
│   ├── pwn
│   ├── reverse
│   └── web
├── quals
│   ├── crypto
│   ├── forensic
│   ├── misc
│   ├── pwn
│   ├── reverse
│   └── web
```

Dan berikut adalah struktur folder untuk setiap challenge yang ada

```
<name>/
├── release/
│   └── ...
├── source/
│   └── <name>/
│       └── ...
└── poc/
    └── ...
└── README.md
```

Penjelasan:

1. **\<name>** adalah nama challenge yang akan dibuat.
2. **release** adalah folder untuk attachment yang akan diberikan ke peserta.
3. **source** adalah folder yang digunakan menyimpan source code challenge asli, dan jika service maka folder ini yang akan dideploy ke server.

> Kenapa harus ada \<name> lagi di source?
> Untuk menghindari conflict docker compose agar tidak ter-sync satu sama lain (idsecconf moment hell nah)

4. **poc** adalah folder yang isinya adalah penjelasan cara solve dari setiap challenge (wajib).
5. **README.md** digunakan untuk memberikan keterangan setiap challenge tersebut. Berikut template README.md yang dapat digunakan.

```md
# <name>

## Author

(username discord)

## Difficulty

Easy/Medium/Hard

## Description

lorem ipsum dolor sit amet.

## Flag

ARA6{sample}
```

## TIA 🕵️
