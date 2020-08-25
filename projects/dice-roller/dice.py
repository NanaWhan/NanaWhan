import random
import re

def roll(notation="1d6"):
    match = re.match(r'(\d+)d(\d+)([+-]\d+)?', notation)
    if not match:
        raise ValueError(f"Invalid dice notation: {notation}")
    
    num_dice = int(match.group(1))
    sides = int(match.group(2))
    modifier = int(match.group(3) or 0)
    
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    total = sum(rolls) + modifier
    
    return {"rolls": rolls, "modifier": modifier, "total": total}

def roll_multiple(notation, times=1):
    return [roll(notation) for _ in range(times)]

if __name__ == "__main__":
    import sys
    dice = sys.argv[1] if len(sys.argv) > 1 else "1d6"
    result = roll(dice)
    print(f"Rolling {dice}: {result['rolls']} = {result['total']}")
