

import sys

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added.')

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f'{i + 1}. {task["task"]} - {status}')

def mark_task_completed(task_number):
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print(f'Task "{tasks[task_number]["task"]}" marked as completed.')
    else:
        print("Invalid task number.")

def print_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to mark as completed: ")) - 1
                mark_task_completed(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
