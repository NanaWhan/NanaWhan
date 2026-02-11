import random
import string

def generate_password(length=16, use_upper=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()-_=+"
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Password length (default 16): ") or 16)
    count = int(input("How many passwords? ") or 1)
    for i in range(count):
        print(generate_password(length))
