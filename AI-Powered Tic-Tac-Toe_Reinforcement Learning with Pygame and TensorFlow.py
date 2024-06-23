# pip install pygame numpy tensorflow

import sys
import random
import numpy as np
import pygame
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Initialize Pygame
pygame.init()

# Set up the display for the game
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic-Tac-Toe')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Game variables
board = [0] * 9  # Represents a 3x3 grid
game_over = False
player_turn = True  # True if player's turn, False for AI

# Initialize font, adjusting size to fit better
font = pygame.font.Font(None, 28)

# Neural Network for the AI Player
model = Sequential()
model.add(Dense(64, input_dim=9, activation='relu'))  # Input layer for 9 board positions
model.add(Dense(64, activation='relu'))  # Hidden layer
model.add(Dense(9, activation='linear'))  # Output layer for each move's Q-value
model.compile(loss='mse', optimizer=Adam())

def draw_board():
    screen.fill(white)
    for i in range(1, 3):
        pygame.draw.line(screen, black, (0, 100 * i), (300, 100 * i), 3)
        pygame.draw.line(screen, black, (100 * i, 0), (100 * i, 300), 3)

    for index, value in enumerate(board):
        x = (index % 3) * 100 + 50
        y = (index // 3) * 100 + 50
        if value == 1:
            pygame.draw.line(screen, black, (x - 25, y - 25), (x + 25, y + 25), 2)
            pygame.draw.line(screen, black, (x + 25, y - 25), (x - 25, y + 25), 2)
        elif value == -1:
            pygame.draw.circle(screen, black, (x, y), 34, 2)

def check_win():
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] != 0:
            return 'Human' if board[a] == 1 else 'AI'
    if 0 not in board:
        return 'Draw'
    return None

def ai_move():
    """AI chooses the best move based on the neural network prediction."""
    state = np.array(board).reshape(1, -1)
    predictions = model.predict(state)[0]
    # Apply a mask to remove illegal moves (positions already taken)
    legal_moves = [i if x == 0 else -1e7 for i, x in enumerate(board)]
    move = np.argmax(np.array(predictions) + np.array(legal_moves))
    return move if board[move] == 0 else None

def display_message(message):
    message_screen = pygame.display.set_mode((300, 150))
    pygame.display.set_caption('Game Over')
    message_screen.fill(white)
    text = font.render(message, True, black)
    text_rect = text.get_rect(center=(150, 75))
    message_screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.display.quit()

# Main game loop
while not game_over:
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and player_turn:
            x, y = pygame.mouse.get_pos()
            index = (x // 100) + (y // 100) * 3
            if board[index] == 0:
                board[index] = 1
                result = check_win()
                if result is not None:
                    game_over = True
                player_turn = False

    if not player_turn and not game_over:
        index = ai_move()
        if index is not None:
            board[index] = -1
            result = check_win()
            if result is not None:
                game_over = True
        player_turn = True

    pygame.display.flip()

if game_over:
    result = check_win()
    message = "Congratulations! You've won the game!" if result == 'Human' \
        else "Your hard work is commendable, but you need to try more." if result == 'AI' \
        else "Game Over. It's a draw."
    display_message(message)
    pygame.quit()
    sys.exit()
