import json

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("\nYour tasks:")
        for index, task, in enumerate(tasks, start=1):
            print(index, "-", task)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks to delete!")
        return
    
    show_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print("Deleted:", removed_task)
        else:
            print("Invalid task number")

    except ValueError:
        print("Please enter a valid number")

def main():
    tasks = load_tasks()

    while True:
        print("\nTODO LIST")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            show_tasks(tasks)
        
        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

main()