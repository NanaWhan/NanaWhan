import sys

class CLI:
    def __init__(self, name, version="1.0.0"):
        self.name = name
        self.version = version
        self.commands = {}
    
    def command(self, name, help_text=""):
        def decorator(func):
            self.commands[name] = {"func": func, "help": help_text}
            return func
        return decorator
    
    def parse_args(self, args):
        flags = {}
        positional = []
        i = 0
        while i < len(args):
            if args[i].startswith("--"):
                key = args[i][2:]
                if i + 1 < len(args) and not args[i+1].startswith("--"):
                    flags[key] = args[i+1]
                    i += 2
                else:
                    flags[key] = True
                    i += 1
            else:
                positional.append(args[i])
                i += 1
        return positional, flags
    
    def run(self, args=None):
        args = args or sys.argv[1:]
        if not args or args[0] == "help":
            self.show_help()
            return
        if args[0] == "--version":
            print(f"{self.name} v{self.version}")
            return
        cmd_name = args[0]
        if cmd_name in self.commands:
            positional, flags = self.parse_args(args[1:])
            self.commands[cmd_name]["func"](positional, flags)
        else:
            print(f"Unknown command: {cmd_name}")
    
    def show_help(self):
        print(f"{self.name} v{self.version}\n\nCommands:")
        for name, info in self.commands.items():
            print(f"  {name:15} {info['help']}")

if __name__ == "__main__":
    app = CLI("demo", "0.1.0")
    
    @app.command("greet", "Say hello")
    def greet(args, flags):
        name = args[0] if args else "World"
        print(f"Hello, {name}!")
    
    app.run()
