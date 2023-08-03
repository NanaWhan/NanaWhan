import json
import os
from pathlib import Path

class Config:
    def __init__(self, filepath="config.json", defaults=None):
        self.filepath = Path(filepath)
        self.defaults = defaults or {}
        self.data = {}
        self.load()
    
    def load(self):
        if self.filepath.exists():
            with open(self.filepath) as f:
                self.data = json.load(f)
        else:
            self.data = dict(self.defaults)
    
    def save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=2)
    
    def get(self, key, default=None):
        keys = key.split(".")
        value = self.data
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default or self.defaults.get(key)
        return value
    
    def set(self, key, value):
        keys = key.split(".")
        data = self.data
        for k in keys[:-1]:
            data = data.setdefault(k, {})
        data[keys[-1]] = value
        self.save()
    
    def delete(self, key):
        keys = key.split(".")
        data = self.data
        for k in keys[:-1]:
            if k in data:
                data = data[k]
            else:
                return
        data.pop(keys[-1], None)
        self.save()
    
    def all(self):
        return dict(self.data)

if __name__ == "__main__":
    cfg = Config(defaults={"app.name": "MyApp", "app.debug": False})
    cfg.set("app.name", "TestApp")
    cfg.set("database.host", "localhost")
    print(json.dumps(cfg.all(), indent=2))
