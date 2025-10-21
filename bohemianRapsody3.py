import sys
import time

def jalankan_lirik():
    lirik = [
        ("I see a little silhouetto of a man,", 0.06),
        ("Scaramouche, Scaramouche, will you do the Fandango?", 0.06),
        ("Thunderbolt and lightning, very, very frightening me!", 0.06),
        ("(Galileo) Galileo,", 0.08),
        ("(Galileo) Galileo,", 0.08),
        ("Galileo Figaro magnifico!", 0.07),
        ("I'm just a poor boy, nobody loves me.", 0.06),
        ("He's just a poor boy from a poor family,", 0.06),
        ("Spare him his life from this monstrosity.", 0.06),
        ("Easy come, easy go, will you let me go?", 0.06),
        ("Bismillah! No, we will not let you go!", 0.06),
        ("(Let him go!) Bismillah! We will not let you go!", 0.06),
        ("(Let him go!) Bismillah! We will not let you go!", 0.06),
        ("(Let me go) Will not let you go!", 0.06),
        ("(Let me go) Never, never, never, never let me go!", 0.06),
        ("Ah, No, no, no, no, no, no, no!", 0.07),
        ("Oh mama mia, mama mia, mama mia, let me go!", 0.06),
        ("Beelzebub has a devil put aside for me, for me, for me!", 0.06),
    ]

    delay = [
        1.2, 1.3, 1.5,
        0.9, 0.9, 1.2,
        1.2, 1.2, 1.3,
        1.2, 0.8, 0.8,
        0.9, 0.8, 1.0,
        1.3, 1.6
    ]

    print("\n== Bohemian Rhapsody (Queen) - Part 4 (Opera) ==")
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
