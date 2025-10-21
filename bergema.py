import sys
import time

def jalankan_lirik():
    lirik = [
        ("Ku tak ingin cepat berlalu",                     0.06),
        ("Waktu yang kupunya denganmu",                   0.06),
        ("Kita berdansa dan tertawa gandeng tangan",      0.05),
        ("Semoga bergema sampai selamanya",               0.06),
        ("",                                              0.00),  
        ("Dunia pasti ada akhirnya",                      0.06),
        ("Bintang‑bintang pun ada umurnya",               0.06),
        ("Maka tenang saja kita di sini berdua",          0.05),
        ("Nikmati sementara yang ada",                    0.06),
    ]

    jeda_baris = [1.2, 1.1, 1.3, 1.4, 0.8, 1.2, 1.2, 1.3, 2.0]

    print("\n== Bergema Selamanya ==")
    time.sleep(2)  
    for i, (teks, jeda_karakter) in enumerate(lirik):
        for huruf in teks:
            print(huruf, end='')
            sys.stdout.flush()
            time.sleep(jeda_karakter)
        time.sleep(jeda_baris[i])
        print() 

if __name__ == "__main__":
    jalankan_lirik()
