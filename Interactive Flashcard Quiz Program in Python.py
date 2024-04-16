import random

def load_flashcards(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        flashcards = [line.strip().split(' - ') for line in lines]
    return flashcards

def display_flashcard(flashcards):
    card = random.choice(flashcards)
    print(f"Question: {card[0]}")
    input("Press Enter to see the answer...")
    print(f"Answer: {card[1]}")
    if input("Press 'y' to continue or any other key to stop: ").lower() != 'y':
        return False
    return True

def main():
    filename = "flashcards.txt"  # Assume the file contains lines formatted as "Question - Answer"
    flashcards = load_flashcards(filename)
    while display_flashcard(flashcards):
        pass

if __name__ == "__main__":
    main()
