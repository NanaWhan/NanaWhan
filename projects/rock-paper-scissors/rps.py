import random

CHOICES = ["rock", "paper", "scissors"]
WINS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

def play_round(player_choice):
    computer = random.choice(CHOICES)
    if player_choice == computer:
        return "tie", computer
    elif WINS[player_choice] == computer:
        return "win", computer
    else:
        return "lose", computer

def play_game(rounds=5):
    score = {"player": 0, "computer": 0, "ties": 0}
    for i in range(rounds):
        choice = input(f"Round {i+1}: rock/paper/scissors? ").lower()
        if choice not in CHOICES:
            print("Invalid choice!")
            continue
        result, comp = play_round(choice)
        print(f"  Computer chose: {comp} -> You {result}!")
        if result == "win":
            score["player"] += 1
        elif result == "lose":
            score["computer"] += 1
        else:
            score["ties"] += 1
    print(f"\nFinal: You {score['player']} - {score['computer']} Computer ({score['ties']} ties)")

if __name__ == "__main__":
    play_game()
