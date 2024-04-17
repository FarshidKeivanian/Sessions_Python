    # Exercise 2: Nested while Loop with Input Validation
    # Created on Wed Mar 30 10:56:29 2022
    # @author: SHEERAZ MEMON

    # Initial choice for the loop
    choice = "Y"
    # Tuple of valid input choices
    valid = ("Y", "y", "n", "N")
    # Tuple of choices that imply affirmation
    yes_list = ("Y", "y", "yes", "Yes", "YES")

    # Main loop to repeat BMI calculations
    while choice in yes_list:
        # Get the weight from the user, with input validation
        weight = float(input("How much do you weigh? "))
        # Get the height from the user, with input validation
        height = float(input("How tall are you in inches? "))
        
        # Calculate BMI using the 703 factor for imperial units
        bmi = 703 * (weight / (height * height))
        
        # Print the calculated BMI, formatted to two decimal places
        print("Your BMI is: %.2f" % bmi)
        
        # Ask the user if they want to perform another calculation
        choice = input("Another BMI calculation (Y/N)? ")
        
        # Validate the input
        while choice not in valid:
            # Prompt the user again for a valid response
            choice = input("Invalid choice. Enter a Y or N? ")