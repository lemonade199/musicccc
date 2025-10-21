import sys
import time

def jalankan_lirik():
    lirik = [
        ("Do you think I have forgotten?", 0.07),
        ("Do you think I have forgotten?", 0.07),
        ("About you", 0.1),
        ("And there was something 'bout you that now I can't remember", 0.07),
        ("It's the same damn thing that made my heart surrender", 0.07),
        ("And I miss you on a train, I miss you in the morning", 0.07),
        ("I never know what to think about", 0.07),
        ("I think about you (so don't let go)", 0.08),
        ("About you (so don't let go)", 0.08),
        ("Do you think I have forgotten about you? (Don't let go)", 0.07),
        ("About you", 0.1),
        ("About you", 0.1),
        ("Do you think I have forgotten about you? (Don't let go)", 0.07),
    ]

    delay = [
         1.1, 1.1,
        1.5,1.3, 1.3, 1.3, 1.2,
        1.0, 1.0, 1.1, 0.9,
        1.0, 1.5
    ]

    print("\n== About You (The 1975) – Cuplikan Lirik ==")
    time.sleep(2)
    for i, (baris, jeda_karakter) in enumerate(lirik):
        for karakter in baris:
            print(karakter, end='', flush=True)
            time.sleep(jeda_karakter)
        print()
        time.sleep(delay[i])

if __name__ == "__main__":
    jalankan_lirik()

