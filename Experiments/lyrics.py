import time
import sys

def print_lyrics():
    lyrics=[
        "А в мире много красивых женщин,",
        "И все достойны они любви.",
        "Да, в мире много красивых женщин,",
        "Но они не ты!♥"
    ]

    delays=[1.4,1.7,0.9,1.9]

    print("For Shaponchik")
    time.sleep(1.2)

    for repeat in range(2):
        for i,line in enumerate(lyrics):
            for ch in line:
                sys.stdout.write(ch)
                sys.stdout.flush()
                time.sleep(0.07)
            print()
            time.sleep(delays[i])
    time.sleep(0.5)

if __name__ == "__main__":
    print_lyrics()