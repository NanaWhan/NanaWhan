import json
import os

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE) as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add_todo(text):
    todos = load_todos()
    todos.append({"text": text, "done": False})
    save_todos(todos)

def list_todos():
    todos = load_todos()
    for i, t in enumerate(todos):
        status = "x" if t["done"] else " "
        print(f"  [{status}] {i+1}. {t['text']}")

def complete_todo(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["done"] = True
        save_todos(todos)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        list_todos()
    elif sys.argv[1] == "add":
        add_todo(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "done":
        complete_todo(int(sys.argv[2]) - 1)

def delete_todo(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        save_todos(todos)
        print(f"Removed: {removed['text']}")

def clear_completed():
    todos = load_todos()
    todos = [t for t in todos if not t["done"]]
    save_todos(todos)
    print("Cleared completed todos")
