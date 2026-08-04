tasks = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("\nNo tasks found!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            remove = int(input("Enter task number to remove: "))

            if 1 <= remove <= len(tasks):
                deleted = tasks.pop(remove - 1)
                print(f'"{deleted}" removed.')
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Try again.")