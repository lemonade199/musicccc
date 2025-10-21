import sys
import time

def jalankan_lirik():
    lirik = [
        ("Is this the real life?", 0.07),
        ("Is this just fantasy?", 0.07),
        ("Caught in a landslide,", 0.07),
        ("No escape from reality.", 0.07),
        ("Open your eyes,", 0.07),
        ("Look up to the skies and see...", 0.07),
        ("I'm just a poor boy, I need no sympathy,", 0.07),
        ("Because I'm easy come, easy go,", 0.07),
        ("Little high, little low,", 0.07),
        ("Any way the wind blows doesn't really matter to me, to me.", 0.07),
    ]

    delay = [1.2, 1.3, 1.4, 1.4, 1.2, 1.5, 1.7, 1.2, 1.2, 2.0]
    print("\n== Bohemian Rhapsody (Queen) ==")
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