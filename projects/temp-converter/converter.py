def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

if __name__ == "__main__":
    print("Temperature Converter")
    temp = float(input("Enter temperature: "))
    unit = input("From unit (C/F/K): ").upper()
    
    if unit == "C":
        print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F = {celsius_to_kelvin(temp):.2f}K")
    elif unit == "F":
        c = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {c:.2f}°C = {celsius_to_kelvin(c):.2f}K")
    elif unit == "K":
        c = kelvin_to_celsius(temp)
        print(f"{temp}K = {c:.2f}°C = {celsius_to_fahrenheit(c):.2f}°F")
