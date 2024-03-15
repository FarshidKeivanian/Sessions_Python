# Game Introduction
print("Welcome to our text-based adventure game!")
print("You are standing in the middle of a forest. There are two paths ahead of you: one to the left and the other to the right.")

# Getting user choice
choice = input("Do you want to go left or right? (left/right) ")

# Conditional logic to follow user choice
if choice == "left":
    print("You went left and arrived at an old house. The door is open.")
    # Getting user's second choice
    choice2 = input("Do you want to enter the house? (yes/no) ")
    if choice2 == "yes":
        print("You entered the house and found a treasure! You won!")
    else:
        print("You decided not to enter the house. Suddenly, a storm began and you got stuck outside. Game over.")
elif choice == "right":
    print("You went right and encountered a bear!")
    # Getting user's second choice
    choice2 = input("Do you want to fight the bear? (yes/no) ")
    if choice2 == "yes":
        print("Unfortunately, the bear was too strong and you lost the fight. Game over.")
    else:
        print("You decided to run away and managed to escape safely. But your adventure is not over yet!")
else:
    print("Invalid choice. Please enter only 'left' or 'right'.")

# End of the game
print("Thank you for trying our game!")
