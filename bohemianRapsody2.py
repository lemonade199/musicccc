import sys
import time

def jalankan_lirik():
    lirik = [
        ("Too late, my time has come,", 0.07),
        ("Sends shivers down my spine,", 0.07),
        ("Body's aching all the time.", 0.07),
        ("Goodbye, everybody, I've got to go,", 0.07),
        ("Gotta leave you all behind and face the truth.", 0.07),
        ("Mama, ooh (any way the wind blows),", 0.09),
        ("I don't wanna die,", 0.07),
        ("I sometimes wish I'd never been born at all.", 0.07),
    ]

    delay = [1.3, 1.2, 1.3, 1.5, 1.6, 1.2, 1.3, 2.0]
    print("\n== Bohemian Rhapsody (Queen) - Part 3 ==")
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