def main():
    tasks = []

    while True:
        print("\n To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            task = input("Enter the task to do: ").strip()
            if task:
                tasks.append(task)
                print(f"The task '{task}' has been added.")
            else:
                print("Task cannot be empty.")

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter the number of the task to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"The task '{removed}' was successfully deleted.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print(" No tasks to delete.")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


def display_tasks(tasks):
    """This function displays the current tasks."""

    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\n Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


# Run the program
main()
