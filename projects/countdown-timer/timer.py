import time
import sys
import os

def countdown(seconds, message="Time's up!"):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hrs, mins = divmod(mins, 60)
        print(f"\r{hrs:02d}:{mins:02d}:{secs:02d}", end="")
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
    print(f"\n{message}")
    try:
        os.system('echo -e "\a"')
    except:
        pass

def pomodoro(work=25, rest=5, cycles=4):
    for i in range(cycles):
        print(f"\n--- Work session {i+1}/{cycles} ---")
        countdown(work * 60, "Take a break!")
        if i < cycles - 1:
            print(f"\n--- Break {i+1}/{cycles} ---")
            countdown(rest * 60, "Back to work!")
    print("\nAll cycles complete!")

if __name__ == "__main__":
    mode = input("Mode (timer/pomodoro): ").lower()
    if mode == "pomodoro":
        pomodoro()
    else:
        total = int(input("Enter seconds: "))
        countdown(total)
