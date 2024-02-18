import random

def get_player_names():
    players = []
    while True:
        player_name = input("Enter player name (or type 'done' when all players are added): ")
        if player_name.lower() == 'done':
            break
        players.append(player_name)
    return players

def initialize_guess_counts(players):
    return {player: 0 for player in players}

def play_round(players, guess_counts):
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    guesses = {}
    
    while True:
        for player in players:
            guess = int(input(f"{player}, make your guess: "))
            guesses[player] = guess
            guess_counts[player] += 1
            
            if guess == number:
                print(f"Congratulations {player}! You guessed the number.")
                return player, guess_counts
        
            if guess < number:
                print("Too low.")
            else:
                print("Too high.")

def determine_winner(guess_counts):
    min_guesses = min(guess_counts.values())
    winners = [player for player, guesses in guess_counts.items() if guesses == min_guesses]
    
    if len(winners) == 1:
        return winners[0]
    else:
        return winners

def main():
    print("Welcome to the Multiplayer Guessing Game!")
    players = get_player_names()
    guess_counts = initialize_guess_counts(players)
    
    winner, guess_counts = play_round(players, guess_counts)
    if isinstance(winner, list):
        print(f"It's a tie between {' and '.join(winner)} with {guess_counts[winner[0]]} guesses each!")
    else:
        print(f"The winner is {winner} with {guess_counts[winner]} guesses.")
    
    print("Game Over. Thanks for playing!")

if __name__ == "__main__":
    main()
