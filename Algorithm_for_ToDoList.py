# Initialize an empty list to store tasks
ToDoList = []

# Function to add a task
def AddTask(task):
    ToDoList.append(task)
    print("Task added.")

# Function to view tasks
def ViewTasks():
    if ToDoList:
        for index, task in enumerate(ToDoList, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to delete a task
def DeleteTask(task_index):
    try:
        del ToDoList[task_index - 1]  # Adjusting index as list index starts from 0
        print("Task deleted.")
    except IndexError:
        print("Invalid task index. Please try again.")

# Main loop
while True:
    print("\nTo-Do List Application")
    print("1. Add a new task")
    print("2. View current tasks")
    print("3. Delete a task")
    print("4. Exit")

    option = input("Enter your choice (1-4): ")

    if option == '1':
        task = input("Enter the task: ")
        AddTask(task)
    elif option == '2':
        ViewTasks()
    elif option == '3':
        task_index = int(input("Enter the task index to delete: "))
        DeleteTask(task_index)
    elif option == '4':
        print("Exiting application.")
        break
    else:
        print("Invalid option. Please try again.")
