import random
import string
import json

FIRST_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry", "Iris", "Jack"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Wilson", "Moore"]
DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "example.com"]

def random_name():
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

def random_email(name=None):
    if not name:
        name = random_name()
    username = name.lower().replace(" ", ".") + str(random.randint(1, 99))
    return f"{username}@{random.choice(DOMAINS)}"

def random_phone():
    return f"+1-{random.randint(200,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"

def random_user():
    name = random_name()
    return {
        "name": name,
        "email": random_email(name),
        "phone": random_phone(),
        "age": random.randint(18, 80),
        "active": random.choice([True, False])
    }

def generate_users(count=10):
    return [random_user() for _ in range(count)]

if __name__ == "__main__":
    import sys
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    users = generate_users(count)
    print(json.dumps(users, indent=2))
