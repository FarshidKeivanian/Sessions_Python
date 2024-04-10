# Importing necessary libraries
import sys

# Display welcome message and menu
print("-" * 30)
print("\tWelcome to Torrens Cafe")
print("-" * 30)
print("1. Small brekky $10")
print("2. Regular brekky $15")
print("3. Big brekky $20")
print("4. Egg ($0.99 each)")
print("5. Toast ($0.79 per slice)")
print("6. Coffee ($1.09 per cup)")
print("Enter 111 to finalize the payment.")
print("Enter 000 to quit the program.")
print("\n")

# Initialize the total cost variable
total = 0.0

# Loop until user decides to quit or finalize the payment
while True:
    try:
        item_choice = input("Choose your item (or 111 to finalize, 000 to quit): ")
        
        # Handling the exit code
        if item_choice == '000':
            print("Quitting")
            sys.exit(0)  # Exit the program

        # Finalize payment and break the loop
        elif item_choice == '111':
            print(f"Total: ${total:.2f}")
            break

        # Process item choices
        elif item_choice in ['1', '2', '3', '4', '5', '6']:
            quant = int(input("Quantity: "))

            # Calculate cost based on the choice
            if item_choice == '1':
                total += 10 * quant
            elif item_choice == '2':
                total += 15 * quant
            elif item_choice == '3':
                total += 20 * quant
            elif item_choice == '4':
                total += 0.99 * quant
            elif item_choice == '5':
                total += 0.79 * quant
            elif item_choice == '6':
                total += 1.09 * quant
        else:
            print("Enter a valid input again!")

    # Handle exceptions for non-integer quantities and invalid choices
    except ValueError:
        print("Enter a valid input again!")

