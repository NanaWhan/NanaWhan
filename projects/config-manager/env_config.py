import os
from config import Config

class EnvConfig(Config):
    def __init__(self, filepath="config.json", prefix="APP", defaults=None):
        self.prefix = prefix
        super().__init__(filepath, defaults)
    
    def get(self, key, default=None):
        env_key = f"{self.prefix}_{key.upper().replace('.', '_')}"
        env_val = os.environ.get(env_key)
        if env_val is not None:
            if env_val.lower() in ("true", "false"):
                return env_val.lower() == "true"
            try:
                return int(env_val)
            except ValueError:
                try:
                    return float(env_val)
                except ValueError:
                    return env_val
        return super().get(key, default)

    def validate(self, schema):
        errors = []
        for key, rules in schema.items():
            value = self.get(key)
            if rules.get("required") and value is None:
                errors.append(f"Missing required config: {key}")
            if "type" in rules and value is not None:
                if not isinstance(value, rules["type"]):
                    errors.append(f"Invalid type for {key}: expected {rules['type'].__name__}")
        return errors

if __name__ == "__main__":
    cfg = EnvConfig(prefix="MYAPP")
    cfg.set("server.port", 8080)
    cfg.set("server.debug", True)
    print(f"Port: {cfg.get('server.port')}")
