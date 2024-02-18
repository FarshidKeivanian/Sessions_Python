import tkinter as tk

def on_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def on_clear():
    global expression
    expression = ""
    input_text.set("")

def on_calculate():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression using the eval function
        input_text.set(result)
        expression = ""
    except Exception as e:
        input_text.set("Error")
        expression = ""

# Setting up the main GUI window
root = tk.Tk()
root.title("Tkinter Calculator")

expression = ""
input_text = tk.StringVar()

# Creating the input field
input_frame = tk.Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Creating the buttons frame
btns_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

# Row for digits 7-9 and addition
for i, num in enumerate(['7', '8', '9', '+']):
    tk.Button(btns_frame, text=num, fg="black", width=10, height=3, bd=0, bg="#fff", command=lambda num=num: on_click(num)).grid(row=1, column=i, padx=1, pady=1)

# Row for digits 4-6 and subtraction
for i, num in enumerate(['4', '5', '6', '-']):
    tk.Button(btns_frame, text=num, fg="black", width=10, height=3, bd=0, bg="#fff", command=lambda num=num: on_click(num)).grid(row=2, column=i, padx=1, pady=1)

# Row for digits 1-3 and multiplication
for i, num in enumerate(['1', '2', '3', '*']):
    tk.Button(btns_frame, text=num, fg="black", width=10, height=3, bd=0, bg="#fff", command=lambda num=num: on_click(num)).grid(row=3, column=i, padx=1, pady=1)

# Row for digit 0, clear, equals, and division
tk.Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", command=lambda: on_click(0)).grid(row=4, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="C", fg="black", width=10, height=3, bd=0, bg="#fff", command=on_clear).grid(row=4, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#fff", command=on_calculate).grid(row=4, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", command=lambda: on_click("/")).grid(row=4, column=3, padx=1, pady=1)

# Event loop to run the application
root.mainloop()
