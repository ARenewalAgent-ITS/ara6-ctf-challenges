# El Kebanteren

## Deskripsi
Prabu Negronegoro I adalah raja yang bijaksana dan adil, dihormati oleh rakyatnya karena kepemimpinannya yang tegas namun penuh kasih. Ia dikenal karena kemampuannya mendengarkan suara rakyat dan membuat keputusan yang bijak dalam memimpin kerajaan yang subur dan makmur. Putranya, Raden Banter, mewarisi sifat-sifat ayahnya, penuh semangat dan ambisi untuk membawa perubahan yang lebih baik bagi kerajaan, menjadikannya sosok yang diharapkan dapat melanjutkan legasi kebijaksanaan dan keberanian Prabu Negronegoro I.

## Author
abdieryy

## To Do ⚠

To Do List yang harus dilakukan setelah melakukan deploy challenge, yaitu menggunakan iptables demi mitigasi dari reverse shell dan cara unintended lainnya.

1. Deploy challenge
2. Masuk pada shell container docker dengan tambahan command --privileged
3. Masukan command berikut
    ```
    iptables -A OUTPUT -p tcp --sport 5000 -j ACCEPT
    iptables -P OUTPUT DROP
    ```
## Flag
ARA6{Raden_Banter_is_SPEEEEEEEED_SUIIIIIIIIII}
