def calculate():
    number1 = float(input("Enter first number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
    number2 = float(input("Enter second number: "))    
    if operation == "add":
        print("Result:", number1 + number2)
    elif operation == "subtract":
        print("Result:", number1 - number2)
    elif operation == "multiply":
        print("Result:", number1 * number2)
    elif operation == "divide":
        if number2 != 0:
            print("Result:", number1 / number2)
        else:
            print("Error: Division by zero.")
    else:
        print("Invalid operation.")
calculate()