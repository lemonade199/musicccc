import sys
import time

def jalankan_nina_feast():
    lirik = [
        ("Maaf atas perjalanan yang tidak sempurna", 0.07),
        ("Namun percayalah, untukmu kujual dunia", 0.07),
        ("Segala hal kuupayakan untuk melindungi", 0.09),
        ("......................................",0.06),
        ("Tunggu aku kembali lagi esok pagi", 0.06),
        ("Tumbuh lebih baik, cari panggilanmu", 0.07),
        ("Jadi lebih baik dibanding diriku", 0.07),
        ("Dan tertawalah saat ini selepas-lepasnya", 0.07),
        ("Kar'na kelak kau 'kan tersakiti", 0.07),
        ("Aku tahu kamu hebat", 0.08),
        ("Namun, s'lamanya diriku pasti berkutat", 0.07),
        ("'Tuk s'lalu jauhkanmu dari dunia yang jahat", 0.07),
        ("Ini sumpahku padamu 'tuk biarkanmu", 0.07),
        ("Tumbuh lebih baik, cari panggilanmu", 0.07),
        ("Jadi lebih baik dibanding diriku", 0.07),
        ("'Tuk sementara kita tertawakan berbagai hal", 0.07),
        ("Yang lucu dan lara selepas lepasnya", 0.07),
        ("Saat dewasa kau 'kan mengerti", 0.08),
        ("Kar'na kelak kau 'kan tersakiti", 0.08),
        ("Saat dewasa kau 'kan mengerti", 0.08),
        ("Kar'na kelak kau 'kan tersakiti", 0.08),
    ]

    jeda_setiap_baris = 1.1  # jeda antar baris

    print("\n== Nina - .Feast (Typewriter Style) ==\n")
    time.sleep(2)

    for baris, delay_karakter in lirik:
        for karakter in baris:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        print('')
        time.sleep(jeda_setiap_baris)

    print("\n🎵 SELESAI 🎵\n")

jalankan_nina_feast()
