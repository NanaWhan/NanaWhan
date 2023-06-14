import random
from datetime import datetime, timedelta

def random_date(start_year=2020, end_year=2023):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = (end - start).days
    return (start + timedelta(days=random.randint(0, delta))).strftime("%Y-%m-%d")

def random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def random_product():
    adjectives = ["Premium", "Basic", "Pro", "Ultra", "Mini", "Eco"]
    items = ["Widget", "Gadget", "Tool", "Kit", "Pack", "Module"]
    return {
        "name": f"{random.choice(adjectives)} {random.choice(items)}",
        "price": round(random.uniform(9.99, 299.99), 2),
        "sku": f"SKU-{random.randint(10000, 99999)}",
        "in_stock": random.choice([True, True, True, False]),
    }

def random_address():
    streets = ["Main St", "Oak Ave", "Elm Dr", "Park Ln", "Cedar Blvd"]
    cities = ["Springfield", "Portland", "Austin", "Denver", "Seattle"]
    return {
        "street": f"{random.randint(100, 9999)} {random.choice(streets)}",
        "city": random.choice(cities),
        "zip": f"{random.randint(10000, 99999)}",
    }
