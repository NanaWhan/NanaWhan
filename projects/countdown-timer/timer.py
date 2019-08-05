import time
import sys

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hrs, mins = divmod(mins, 60)
        print(f"\r{hrs:02d}:{mins:02d}:{secs:02d}", end="")
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")

if __name__ == "__main__":
    total = int(input("Enter seconds: "))
    countdown(total)
