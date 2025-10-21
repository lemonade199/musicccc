import sys
import time

def jalankan_lirik():
    lirik = [
        ("Mama, just killed a man,", 0.07),
        ("Put a gun against his head,", 0.07),
        ("Pulled my trigger, now he's dead.", 0.07),
        ("Mama, life had just begun,", 0.07),
        ("But now I've gone and thrown it all away.", 0.07),
        ("Mama, ooh,", 0.09),
        ("Didn't mean to make you cry,", 0.07),
        ("If I'm not back again this time tomorrow,", 0.07),
        ("Carry on, carry on as if nothing really matters.", 0.07),
    ]

    delay = [1.5, 1.3, 1.4, 1.5, 1.8, 1.2, 1.3, 1.5, 2.0]
    print("\n== Bohemian Rhapsody (Queen) - Part 2 ==")
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