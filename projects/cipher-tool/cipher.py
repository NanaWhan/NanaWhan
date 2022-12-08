def caesar_encrypt(text, shift=3):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decrypt(text, key):
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    import sys
    text = input("Text: ")
    method = input("Method (caesar/vigenere): ")
    if method == "caesar":
        shift = int(input("Shift: "))
        print(f"Encrypted: {caesar_encrypt(text, shift)}")
    else:
        key = input("Key: ")
        print(f"Encrypted: {vigenere_encrypt(text, key)}")
