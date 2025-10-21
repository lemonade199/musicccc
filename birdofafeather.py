import time

def jalankan_lirik_birds_of_a_feather():
    lirik = [
        ("I want you to stay", 0.06),
        ("'Til I'm in the grave", 0.06),
        ("'Til I rot away, dead and buried", 0.06),
        ("'Til I'm in the casket you carry", 0.06),
        ("If you go, I'm going too", 0.06),
        ("'Cause it was always you", 0.06),
        ("And if I'm turning blue, please don't save me", 0.06),
        ("Nothing left to lose without my baby", 0.06),
        ("Birds of a feather, we should stick together, I know", 0.06),
        ("I said I'd never think I wasn't better alone", 0.06),
        ("Can't change the weather, might not be forever", 0.06),
        ("But if it's forever, it's even better", 0.06),
        ("And I don't know what I'm crying for", 0.06),
        ("I don't think I could love you more", 0.06),
        ("It might not be long, but baby, I", 0.06),
        ("I'll love you 'til the day that I die", 0.06),
    ]

    delay = [1.2] * len(lirik)

    print("\n== Billie Eilish - Birds of a Feather ==")
    time.sleep(2)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='', flush=True)
            time.sleep(delay_karakter)
        print()
        time.sleep(delay[i])

# Jalankan lirik
jalankan_lirik_birds_of_a_feather()