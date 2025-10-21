import sys
import time

def jalankan_bunga_maaf():
    lirik = [
        ("Hai", 0.07),
        ("Masihkah", 0.07),
        ("Luka itu", 0.07),
        ("Ada di sana", 0.07),
        ("Yang ku", 0.07),
        ("Tinggalkan", 0.07),
        ("Saat kita", 0.07),
        ("Masih bersama", 0.07),
        ("Kini waktu terasa berbeda", 0.06),
        ("Tanpa hadirmu", 0.06),
        ("Keras hati yang dulu bicara", 0.06),
        ("Berujung pilu", 0.06),
        ("Andai", 0.07),
        ("Angin mengulang", 0.07),
        ("Sebuah masa yang t'lah usang", 0.07),
        ("Kan ku telan isi bumi hanya untukmu", 0.06),
        ("Terima bunga maafku", 0.07),
        ("Layu termakan egoku", 0.07),
        ("Meski ku tahu", 0.07),
        ("Tak bisa", 0.08),
        ("Oh", 0.07),
        ("Mungkinkah", 0.07),
        ("Ada rindu", 0.07),
        ("Dibalik benci itu", 0.07),
        ("Yang perlahan", 0.07),
        ("Menghilang", 0.07),
        ("Saat nyamanku tak lagi kau butuh", 0.06),
        ("Andai", 0.07),
        ("Angin mengulang", 0.07),
        ("Semua masa yang t'lah hilang", 0.07),
        ("Ku tak akan bisa", 0.08),
    ]

    jeda_setiap_baris = 1.2  # jeda antar baris

    print("\n== Bunga Maaf - The Lantis (Typewriter Style) ==\n")
    time.sleep(2)

    for baris, delay_karakter in lirik:
        for karakter in baris:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        print('')
        time.sleep(jeda_setiap_baris)

    print("\n🌸 SELESAI 🌸\n")

jalankan_bunga_maaf()
