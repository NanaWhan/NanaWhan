COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "reset": "\033[0m",
}

def colorize(text, color):
    return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"

def success(text):
    return colorize(f"✓ {text}", "green")

def error(text):
    return colorize(f"✗ {text}", "red")

def warning(text):
    return colorize(f"⚠ {text}", "yellow")

def info(text):
    return colorize(f"ℹ {text}", "blue")

def header(text):
    return colorize(text, "bold")
