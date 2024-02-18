import random

def get_hint(number, guess):
    if number % 2 == 0 and guess % 2 != 0:
        return "Hint: The number is even."
    elif number % 2 != 0 and guess % 2 == 0:
        return "Hint: The number is odd."
    elif number % 3 == 0 and guess % 3 != 0:
        return "Hint: The number is divisible by 3."
    elif number % 5 == 0 and guess % 5 != 0:
        return "Hint: The number is divisible by 5."
    else:
        return "No hint for this guess."

def choose_difficulty():
    difficulty = input("Choose difficulty (easy/medium/hard): ")
    if difficulty.lower() == 'easy':
        return random.randint(1, 50), 10  # Easier range, more guesses
    elif difficulty.lower() == 'medium':
        return random.randint(1, 100), 7  # Medium range, medium guesses
    else:  # hard
        return random.randint(1, 1000), 5  # Harder range, fewer guesses

def play_game():
    number, max_guesses = choose_difficulty()
    guesses = 0
    
    print("Welcome to the Enhanced Number Guessing Game!")
    print(f"I'm thinking of a number in your chosen range.")

    while guesses < max_guesses:
        guess = int(input(f"Make a guess ({max_guesses - guesses} guesses left): "))
        guesses += 1
        
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print("Congratulations! You guessed the number.")
            break
        
        print(get_hint(number, guess))
        
        if guesses == max_guesses:
            print(f"Sorry, you've run out of guesses. The number was {number}.")
            break

if __name__ == "__main__":
    play_game()