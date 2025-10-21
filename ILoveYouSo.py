import sys
import time

def jalankan_i_love_you_so():
    lirik = [
        ("I just need someone in my life to give it structure", 0.08),
        ("To handle all the selfish ways I'd spend my time without her", 0.09),
        ("You're everything I want, but I can't deal with all your lovers", 0.08),
        ("You're saying I'm the one, but it's your actions that speak louder", 0.06),
        ("Giving me love when you are down and need another", 0.06),
        ("I've gotta get away and let you go, I've gotta get over", 0.06),
        ("But I love you so", 0.12),
        ("I love you so", 0.10),
        ("I love you so", 0.10),
        ("I love you so", 0.08),
        ("I'm gonna pack my things and leave you behind", 0.06),
        ("This feeling's old and I know that I've made up my mind", 0.06),
        ("I hope you feel what I felt when you shattered my soul", 0.06),
        ("'Cause you were cruel and I'm a fool", 0.06),
        ("So please let me go", 0.08),
        ("But I love you so", 0.12),
        ("I love you so", 0.10),
        ("I love you so", 0.10),
        ("I love you so", 0.08)
    ]

    jeda_setiap_baris = 1.2  # jeda antar baris

    print("\n== I Love You So - The Walters (Typewriter Style) ==\n")
    time.sleep(2)

    for baris, delay_karakter in lirik:
        for karakter in baris:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        print('')
        time.sleep(jeda_setiap_baris)

    print("\n🎵 SELESAI 🎵\n")

jalankan_i_love_you_so()
