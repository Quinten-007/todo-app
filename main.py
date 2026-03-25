from todo_manager import add_todo, list_todos, mark_done

def menu():
    print("\nTodo List CLI")
    print("1. List todos")
    print("2. Add todo")
    print("3. Mark todo as done")
    print("4. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option: ")
        if choice == "1":
            list_todos()
        elif choice == "2":
            desc = input("Enter todo description: ")
            add_todo(desc)
        elif choice == "3":
            idx = int(input("Enter index to mark done: "))
            mark_done(idx)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()