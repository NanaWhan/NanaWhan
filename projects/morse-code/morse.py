MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

REVERSE_MORSE = {v: k for k, v in MORSE.items()}

def to_morse(text):
    return ' '.join(MORSE.get(c, '') for c in text.upper())

def from_morse(morse):
    return ''.join(REVERSE_MORSE.get(code, '') for code in morse.split(' '))

if __name__ == "__main__":
    import sys
    if "--decode" in sys.argv:
        text = input("Morse code: ")
        print(f"Decoded: {from_morse(text)}")
    else:
        text = input("Text: ")
        print(f"Morse: {to_morse(text)}")
