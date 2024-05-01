#pip install pygame
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
BACKGROUND_COLOR = (0, 0, 0)  # black
SNAKE_COLOR = (0, 255, 0)  # green
FOOD_COLOR = (255, 0, 0)  # red
BLOCK_SIZE = 20

# Setup the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

snake = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]]

def place_food():
    return [random.randrange(1, (SCREEN_WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
            random.randrange(1, (SCREEN_HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]

food_pos = place_food()





clock = pygame.time.Clock()
direction = 'RIGHT'
change_to = direction

def change_direction(new_dir):
    global direction
    dirs = {'RIGHT': 'LEFT', 'LEFT': 'RIGHT', 'UP': 'DOWN', 'DOWN': 'UP'}
    if new_dir != dirs[direction]:
        direction = new_dir

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    
    change_direction(change_to)

    if direction == 'UP':
        snake[0][1] -= BLOCK_SIZE
    elif direction == 'DOWN':
        snake[0][1] += BLOCK_SIZE
    elif direction == 'LEFT':
        snake[0][0] -= BLOCK_SIZE
    elif direction == 'RIGHT':
        snake[0][0] += BLOCK_SIZE

    # Snake body growing mechanism
    snake.insert(0, list(snake[0]))
    if snake[0] == food_pos:
        food_pos = place_food()
    else:
        snake.pop()

    # Game over conditions
    if snake[0][0] < 0 or snake[0][0] > SCREEN_WIDTH - BLOCK_SIZE:
        break
    if snake[0][1] < 0 or snake[0][1] > SCREEN_HEIGHT - BLOCK_SIZE:
        break

    # Fill the screen with background color
    screen.fill(BACKGROUND_COLOR)
    # Draw snake
    for pos in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    # Draw food
    pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.update()
    clock.tick(10)
