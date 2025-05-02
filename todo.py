# Empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index] += " (Completed)"
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted.")
    else:
        print("Invalid task number.")

# Main function to run the program
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
