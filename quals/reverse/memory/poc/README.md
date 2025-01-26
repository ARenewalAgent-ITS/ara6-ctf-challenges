# memory POC

1. Buka `memory` di binaryninja
![image](https://github.com/user-attachments/assets/93b08f2d-1209-4001-9d9c-a70d9789946e)
2. Masuk ke fungsi `memory::main::*`
![image](https://github.com/user-attachments/assets/b8e8335c-cbd3-40b3-b1f5-54a9b152f1bd)
3. Pengecekan pertama adalah flag dimulai dengan substring `ARA6{`
![image](https://github.com/user-attachments/assets/bbb67815-58ff-4305-bfa6-2e70e0dbd882)
![image](https://github.com/user-attachments/assets/062ad29d-242e-4b74-9fae-befc5b90c40f)
Mohon diingat bahwa fungsi `memory::no::*` dipanggil ketika user-input salah. Maka, ada baiknya kita cari syarat-syarat yang harus dipenuhi agar fungsi tersebut tidak dipanggil.
5. Pengencekan dalam loop dipenuhi oleh proses casting yang bertujuan untuk mempersulit proses reverse engineering.

Decompilation | Tidy-Up | Source Code
-- | -- | --
![image](https://github.com/user-attachments/assets/65c9de81-ec97-4ac7-8f7d-56b74e8ed2e2) | | ![image](https://github.com/user-attachments/assets/06da38a7-54d2-47a7-8d66-42aed051b2a3)
![image](https://github.com/user-attachments/assets/f1efd01b-e5a7-40c1-a6a4-27662f0a5ce7) | ![image](https://github.com/user-attachments/assets/3f6c026d-138a-4c50-aa9c-e4ec89fbf131) | 
![image](https://github.com/user-attachments/assets/65b7f936-175b-42db-8f9b-0c804ab72d8e) | ![image](https://github.com/user-attachments/assets/1fa3241c-df8e-416c-b481-06f1e5baee67) | ![image](https://github.com/user-attachments/assets/3c88587f-ff63-4a8a-85ed-5f3e1d3a06ce)
![image](https://github.com/user-attachments/assets/0208843d-1eb8-43d8-992c-83597c2cacc6) | ![image](https://github.com/user-attachments/assets/a8cc1ea6-2a01-4df9-8730-4db879d586fa) | ![image](https://github.com/user-attachments/assets/426c27ff-67f2-47b2-b71d-28e5b523dde3)


Saran bagi para peserta adalah untuk merunut sumber value dari suatu variabel yang menarik secara sistematis. Bermulai pada akhir penggunaan variabel tersebut, hingga pertama kali sumber value dari variabel tersebut muncul.

Jika stuck, gunakan debugger untuk melakukan dynamic analysis.

6. Yang terakhir, ada pengecekan huruf terakhir yang dapat dengan mudah dianalisis
![image](https://github.com/user-attachments/assets/1ac428e0-a0ac-45de-96d2-09c56788bed5)

Before | After
-- | --
![image](https://github.com/user-attachments/assets/5403e767-cf04-447a-b42b-7cede3dbe078) | ![image](https://github.com/user-attachments/assets/2a382ffc-b449-4703-b528-6e3ec84f292b)


Flag: `ARA6{@ABCDEFGHIJKLMNABCDEFGHIJKLMNOBCDEFGHIJKLMNOPCDEFGHIJKLMNOPQD}`
