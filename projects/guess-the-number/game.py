import random

DIFFICULTIES = {
    "easy": (1, 50, 10),
    "medium": (1, 100, 7),
    "hard": (1, 500, 9),
}

def play_game(difficulty="medium"):
    min_val, max_val, max_attempts = DIFFICULTIES[difficulty]
    secret = random.randint(min_val, max_val)
    attempts = 0
    print(f"Difficulty: {difficulty} | Range: {min_val}-{max_val} | Max attempts: {max_attempts}")
    
    while attempts < max_attempts:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < secret:
            print(f"Too low! ({max_attempts - attempts} left)")
        elif guess > secret:
            print(f"Too high! ({max_attempts - attempts} left)")
        else:
            print(f"Correct! You got it in {attempts} attempts!")
            return True
    
    print(f"Game over! The number was {secret}")
    return False

if __name__ == "__main__":
    diff = input("Choose difficulty (easy/medium/hard): ").lower()
    play_game(diff if diff in DIFFICULTIES else "medium")
