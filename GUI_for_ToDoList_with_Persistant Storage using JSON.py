import json

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(ToDoList, file)

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# At the start of your application
ToDoList = load_tasks()

# And whenever you add or delete tasks, call save_tasks() to update the JSON file
