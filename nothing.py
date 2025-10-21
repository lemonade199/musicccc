import time

def jalankan_lirik_nothing():
    lirik = [
        ("Track suits and red wine", 0.06),
        ("Movies for two", 0.06),
        ("We'll take off our phones", 0.06),
        ("And we'll turn off our shoes", 0.06),
        ("We'll play Nintendo", 0.06),
        ("Though I always lose", 0.06),
        ("'Cause you'll watch the TV", 0.06),
        ("While I'm watching you", 0.06),
        ("There's not many people", 0.06),
        ("I'd honestly say", 0.06),
        ("I don't mind losing to", 0.06),
        ("But there's nothing", 0.06),
        ("Like doing nothing", 0.06),
        ("With you", 0.06),
    ]

    # Jeda antar baris disesuaikan kira-kira dengan tempo lagu
    delay = [
        1.8,  # Track suits and red wine
        1.6,  # Movies for two
        1.7,  # We'll take off our phones
        1.8,  # And we'll turn off our shoes
        1.7,  # We'll play Nintendo
        1.6,  # Though I always lose
        1.8,  # 'Cause you'll watch the TV
        1.8,  # While I'm watching you
        2.0,  # There's not many people
        1.6,  # I'd honestly say
        2.0,  # I don't mind losing to
        1.8,  # But there's nothing
        1.8,  # Like doing nothing
        2.5,  # With you (lebih lama karena sustain)
    ]

    print("\n== Bruno Major - Nothing ==")
    time.sleep(2)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='', flush=True)
            time.sleep(delay_karakter)
        print()
        time.sleep(delay[i])

# Jalankan lirik
jalankan_lirik_nothing()                           





