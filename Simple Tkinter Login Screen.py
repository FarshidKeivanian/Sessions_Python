import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Login Screen")
window.geometry("400x300")

# Create a label and entry for the username
username_label = tk.Label(window, text="Enter your username:")
username_label.pack(pady=10)

username_entry = tk.Entry(window)
username_entry.pack(pady=5)

# Create a label and entry for the password
password_label = tk.Label(window, text="Enter your password:")
password_label.pack(pady=10)

password_entry = tk.Entry(window, show="*")  # The 'show' option hides the input for privacy
password_entry.pack(pady=5)

# Create a submit button
submit_button = tk.Button(window, text="Submit")
submit_button.pack(pady=20)

# Start the event loop
window.mainloop()
