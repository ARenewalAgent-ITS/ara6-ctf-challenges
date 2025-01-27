def main():
    questions = [
        { 
            "question": "Nama pengguna (username) pada perangkat yang terinfeksi malware?",
            "format": "-"
        },
        { 
            "question": "Wallet BTC milik threact actor?",
            "format": "15cxezxyj3PxxNtoVAJ6rwiDYKnrchTNMm"
        },
        { 
            "question": "Email yang digunakan oleh victim?",
            "format": "example@example.com"
        },
        { 
            "question": "Email yang digunakan oleh threat actor?",
            "format": "example@example.com"
        },
        { 
            "question": "Berapa rentang gaji yang ditawarkan oleh threat actor? (Dalam Rupiah)",
            "format": "5.000.000 - 7.000.000"
        },
        { 
            "question": "Link meeting yang digunakan untuk wawancara kerja?",
            "format": "https://example.com/example"
        },
        { 
            "question": "Repositori yang mengandung malware?",
            "format": "https://example.com/example/example"
        },
        { 
            "question": "Full path yang mengandung malicious code?",
            "format": "/root/folder1/folder2/file.ext"
        },
        { 
            "question": "IP beserta port yang digunakan threat actor?",
            "format": "127.0.0.1:8080"
        },
        { 
            "question": "Berikan isi file yang ada di path berikut: /home/ubuntu/Downloads/important_notes.txt",
            "format": "-"
        }
    ]

    answers = [
        "ubuntu",
        "197MJHgAPu5znTX836e4VXLHEPJp8ZCoV",
        "sudirmanryan579@gmail.com",
        "sanglegendaabdi@gmail.com",
        "32.000.000 - 45.000.000",
        "https://meet.google.com/nkb-ukxi-exj",
        "https://github.com/wengdev-33/nodejs-simple-file-upload",
        "/home/ubuntu/nodejs-simple-file-upload/node_modules/multer/storage/disk.js",
        "157.245.204.42:1337",
        "YATTA_BERHASIL_DECRYPT_CUY",

    ]

    print("Silahkan jawab pertanyaan-pertanyaan yang telah disediakan:")

    correct_answers = 0

    for index, q in enumerate(questions, start=1):
        print(f"\nNo {index}:")
        print("Pertanyaan: " + q["question"])
        print("Format: " + q["format"])
        user_answer = input("Jawaban: ")

        if user_answer.strip() == answers[index - 1]:
            correct_answers += 1
            print("Correct")
        else:
            print("Incorrect")
            return
    
    if correct_answers == len(questions):
        print("\nCongrats! Flag: ARA6{504l_Ini_di8u47_83rD454rK4N_r34l_c453_y4_G35_h3H3}")

if __name__ == "__main__":
    main()