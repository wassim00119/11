def display_menu():
    print("\n=== To-Do List Menu ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed.")
    except (IndexError, ValueError):
        print("Invalid task number. Please try again.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nChoose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
