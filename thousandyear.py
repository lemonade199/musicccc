import sys
import time

def jalankan_lirik():
    lirik = [
        ("Heart beats fast", 0.07),
        ("Colors and promises", 0.07),
        ("How to be brave?", 0.08),
        ("How can I love when I'm afraid to fall?", 0.08),
        ("But watching you stand alone", 0.07),
        ("All of my doubt suddenly goes away somehow", 0.07),
        ("One step closer", 0.1),
        ("I have died every day waiting for you", 0.07),
        ("Darling, don't be afraid, I have loved you", 0.07),
        ("For a thousand years", 0.07),
        ("I'll love you for a thousand more", 0.07),
    ]

    delay = [
        1.0, 1.1, 1.2,
        1.3, 1.1, 1.2,
        1.5, 1.3, 1.3,
        1.2, 1.5
    ]

    print("\n== A Thousand Years (Christina Perri) - Part 1 ==")
    time.sleep(2)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='', flush=True)
            time.sleep(delay_karakter)
        print()
        time.sleep(delay[i])

if __name__ == "__main__":
    jalankan_lirik()
