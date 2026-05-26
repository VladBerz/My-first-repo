tasks = []

while True:
    print("\nTODO LIST")
    print("1. Show tasks")
    print("2. Add tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        
        if len(tasks) == 0:
            print("No tasks yet!")
        
        else :
            print("\nYour tasks:")

            for index, task in enumerate(tasks, start=1):
                print(index, "-", task)
    

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to delete!")
        
        else:
            for index, task in enumerate(tasks, start=1):
                print(index, "-", task)

            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print("Deleted:", removed_task)

            else:
                print("Invalid task number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option")    