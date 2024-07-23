import tkinter as tk
from tkinter import messagebox
import json  # Import json module for handling persistent storage

# Function to save tasks to a file
def save_tasks():
    try:
        with open('tasks.json', 'w') as file:
            json.dump(ToDoList, file)

# Function to load tasks from a file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Load tasks from file at the start of the application
ToDoList = load_tasks()

# Function to update the tasks display
def UpdateDisplay():
    listbox_tasks.delete(0, tk.END)
    for task in ToDoList:
        listbox_tasks.insert(tk.END, task)

# Function to add a task
def AddTask():
    task = entry_task.get()
    if task != "":
        ToDoList.append(task)
        save_tasks()  # Save tasks after adding a new one
        UpdateDisplay()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")
    entry_task.delete(0, tk.END)

# Function to delete a task
def DeleteTask():
    try:
        task_index = listbox_tasks.curselection()[0]
        del ToDoList[task_index]
        save_tasks()  # Save tasks after deleting
        UpdateDisplay()
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Create UI components
frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add task", width=48, command=AddTask)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete selected task", width=48, command=DeleteTask)
button_delete_task.pack()

button_exit = tk.Button(root, text="Exit", width=48, command=root.quit)
button_exit.pack()

# Start the main event loop
root.mainloop()
