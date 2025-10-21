import sys
import time

def jalankan_lirik():
    lirik = [
        ("Nothing really matters,", 0.07),
        ("Anyone can see,", 0.07),
        ("Nothing really matters,", 0.07),
        ("Nothing really matters to me.", 0.07),
        ("Any way the wind blows...", 0.1),
    ]

    delay = [1.3, 1.3, 1.5, 2.0, 2.5]

    print("\n== Bohemian Rhapsody (Queen) - Part 6 (Outro) ==")
    time.sleep(2)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    print("\n🎵 THE END 🎵\n")

jalankan_lirik()
