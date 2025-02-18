# Plag Encryptor

Author: jjcho

---------

## POC / Solver

1. Unpack binary onefile (ada di `/tmp/onefile_....../` saat runtime)
2. Decompile binary hasil dump dan cari `modulecode___main__` 
3. Recover simbol (compile [kode sederhana](main2.py) dengan argumen `--unstripped` -> produce [file header](main2.bin.h), [file pattern .pat](main2.pat) dan [file signature .sig](main2.sig))
4. Analisa logic kode pada module main, gunakan [nuitka-helper](https://github.com/goatmilkkk/nuitka-helper/tree/main/scripts) untuk mempermudah analisis. Sebagai alternatif dari [nuitka-helper](https://github.com/goatmilkkk/nuitka-helper/tree/main/scripts), kita tetap bisa melakukan recovery module constants jika memahami struktur `PyObject` dengan referensi artikel berikut, [CPython Objects](https://goatmilkk.notion.site/CPython-Objects-53123c8e09cb4a43ae412c75ba27a734)
5. Pahami algoritma enkripsi yang digunakan, fokus pada bagaimana encryption key dan nonce digenerate dan disimpan.
6. Buat [decryptor](solve.py)

Referensi : https://x.com/goatmilkkk/status/1809883244537508275