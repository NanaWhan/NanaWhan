import random

STANDARD = {"rock": ["scissors"], "scissors": ["paper"], "paper": ["rock"]}
EXTENDED = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"],
}

def play_round(choice, mode="standard"):
    rules = STANDARD if mode == "standard" else EXTENDED
    options = list(rules.keys())
    computer = random.choice(options)
    if choice == computer:
        return "tie", computer
    elif computer in rules[choice]:
        return "win", computer
    else:
        return "lose", computer

def play_game(rounds=5, mode="standard"):
    score = {"wins": 0, "losses": 0, "ties": 0}
    rules = STANDARD if mode == "standard" else EXTENDED
    options = list(rules.keys())
    
    for i in range(rounds):
        choice = input(f"Round {i+1} ({'/'.join(options)}): ").lower()
        if choice not in options:
            print("Invalid!")
            continue
        result, comp = play_round(choice, mode)
        score["wins" if result == "win" else "losses" if result == "lose" else "ties"] += 1
        print(f"  Computer: {comp} -> {result.upper()}")
    
    print(f"\n{score['wins']}W - {score['losses']}L - {score['ties']}T")

if __name__ == "__main__":
    import sys
    mode = "extended" if "--extended" in sys.argv else "standard"
    play_game(mode=mode)
