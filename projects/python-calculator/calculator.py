def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Choose operation (1-4): ")
    a = float(input("First number: "))
    b = float(input("Second number: "))
    ops = {"1": add, "2": subtract, "3": multiply, "4": divide}
    if choice in ops:
        print(f"Result: {ops[choice](a, b)}")

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
