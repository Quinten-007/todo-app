import json
from typing import List, Dict

TODO_FILE = "todos.json"

def load_todos() -> List[Dict]:
    try:
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_todos(todos: List[Dict]):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=4)