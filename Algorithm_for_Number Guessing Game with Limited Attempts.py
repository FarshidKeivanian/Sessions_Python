import random

# Generate a random number between 50 and 100
random_number = random.randint(50, 100)

# Initialize the count of guesses
count = 0

# Start a loop that runs as long as count is less than 5
while count < 5:
    # Prompt the user to enter their guess
    guess = int(input("Enter your guess: "))

    # Increment the count of guesses
    count += 1

    # Check if the user's guess matches the random number
    if guess == random_number:
        print("\nYour guess is correct! You've won!\n")
        break
    # Check if the user's guess is less than the random number
    elif guess < random_number:
        print("Your guess is lower than the correct answer.")
    # Check if the user's guess is greater than the random number
    elif guess > random_number:
        print("Your guess is higher than the correct answer.")

    # Inform the user of the remaining number of guesses
    if count == 5:
        print("\nYou have run out of guesses! The correct number was", random_number, ". Try again :)")
