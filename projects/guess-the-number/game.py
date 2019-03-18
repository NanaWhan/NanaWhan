import random

def play_game(min_val=1, max_val=100):
    secret = random.randint(min_val, max_val)
    attempts = 0
    print(f"I'm thinking of a number between {min_val} and {max_val}")
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempts!")
            return attempts

if __name__ == "__main__":
    play_game()
