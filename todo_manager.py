from storage import load_todos, save_todos
from typing import List, Dict

def add_todo(description: str):
    todos = load_todos()
    todos.append({"description": description, "done": False})
    save_todos(todos)

def list_todos():
    todos = load_todos()
    for idx, todo in enumerate(todos, 1):
        status = "✅" if todo["done"] else "❌"
        print(f"{idx}. {todo['description']} [{status}]")

def mark_done(index: int):
    todos = load_todos()
    if 0 < index <= len(todos):
        todos[index - 1]["done"] = True
        save_todos(todos)
    else:
        print("Invalid index.")