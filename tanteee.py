import sys
import time

def jalankan_lirik():
    lirik = [
        ("Tante.......", 0.07),
        ("Sudah biasa terjadi tante....,", 0.05),
        ("teman datang kalau lagi butuh saja....", 0.07),
        ("coba kalo lagi susah....", 0.04),
        ("mereka semua menghilang.......", 0.07),
    ]

    delay = [1.3, 1, 0.5, 1.5,2]
    print("\n==tante culik aku")
    time.sleep(2)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    print("")

jalankan_lirik()