import sys
import time

def jalankan_lirik():
    lirik = [
        ("So you think you can stone me and spit in my eye?", 0.06),
        ("So you think you can love me and leave me to die?", 0.06),
        ("Oh, baby, can't do this to me, baby!", 0.06),
        ("Just gotta get out, just gotta get right outta here!", 0.06),
    ]

    delay = [1.3, 1.4, 1.4, 1.6]

    print("\n== Bohemian Rhapsody (Queen) - Part 5 (Rock) ==")
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
