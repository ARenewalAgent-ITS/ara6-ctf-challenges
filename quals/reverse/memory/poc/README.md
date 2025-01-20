# memory POC

Banyak caranya, tapi yang simpel dulu ya.

## Solusi Simpel
1. Reverse binarynya dan pahami isinya
2. Run `./memory aaaaaaaaaaaa} | base64`. Hasilnya adalah `CQgMDgwYQGFAGAxhfQ==`
3. Masukkan ke CyberChef dengan recipe sebagai berikut: [recipe here](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)XOR(%7B'option':'UTF8','string':'aaaaaaaaaaaa%7D'%7D,'Standard',false)To_Hex('Space',0)&input=Q1FnTURnd1lRR0ZBR0F4aGZRPT0&oeol=FF)
4. Diperoleh key XOR `68 69 6d 6f 6d 79 21 00 21 79 6d 00 00` dalam representasi hex
5. Masukkan konten dari `output.txt` dengan recipe berikut: [recipe here](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'68%2069%206d%206f%206d%2079%2021%2000%2021%2079%206d%2000%2000'%7D,'Standard',false)&input=MjkzYiAyYzU5IDE2NGMgMTA3OCA3ZTBkIDVlNmUgN2Q&oeol=CR)
6. Diperoleh flag `ARA6{51x_t3n}`

## Solusi Ribet
1. Reverse binarynya
![image](https://github.com/user-attachments/assets/ac24c24b-ca32-40fa-a1fd-1d089ae8e4ad)
2. Follow global variable `child`
![image](https://github.com/user-attachments/assets/2b9f5355-ac0a-446d-860b-d97715c14f61)
3. Didapati bahwa for loop melebihi ukuran dari variabel `child`, maka 4 karakter selanjutnya berasal dari binary offset 0x00004028 yaitu `21 79 6d 00`.
4. `child` + 4 karakter selanjutnya adalah key untuk operasi XOR (untuk selanjutnya disebut `child` sebagai satu kesatuan)
5. `flag`⊕`child` = `output.txt`. Sehingga, `output.txt`⊕`child` = `flag`

Flag: `ARA6{51x_t3n}`
