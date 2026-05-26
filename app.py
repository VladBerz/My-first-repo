tasks = []

while True:
    print("\nTODO LIST")
    print("1. Show tasks")
    print("2. Add tasks")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print(tasks)

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")    