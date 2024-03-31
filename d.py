
# Path: e.py
# I want to create a simple game using Python and Pygame. The game should have the following features:
# - A player character that can move left and right using the arrow keys.   
# - A background image that scrolls to the left to simulate movement.
# - Randomly generated obstacles that the player must avoid.
# - A score that increases as the player successfully avoids obstacles.
# - Game over screen when the player collides with an obstacle.
# - Restart the game when the player presses the space bar after a game over.
# - Sound effects for player movement, obstacle collision, and score increase.
# - A simple menu screen with a start button to begin the game.
# - A quit button to exit the game.
# - The game should have a clean and simple design.
# - The game should be well-documented and easy to understand.
# - The code should be organized into functions and classes where appropriate.
# - The game should run smoothly and without errors.
# - The game should be implemented using Pygame.
# - The game should be fun and engaging to play.
# - The game should be challenging but not frustrating.

import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

# ı dont have any images so ı will use colors for now 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up clock
clock = pygame.time.Clock()

# Set up fonts
font = pygame.font.Font(None, 36)


# Set up game variables
player_x = WIDTH // 2
player_y = HEIGHT - 50
player_width = 50
player_height = 50
player_speed = 20

obstacle_width = 50
obstacle_height = 50
obstacle_speed = 15
obstacle_quantity = 5
obstacle_increase_interval = 1000  # milliseconds
last_obstacle_increase_time = pygame.time.get_ticks()

def increase_obstacle_quantity():
    global obstacle_quantity
    obstacle_quantity += 1

def increase_obstacle_speed():
    global obstacle_speed
    obstacle_speed += 1

def increase_obstacle_frequency():
    global obstacle_frequency
    obstacle_frequency -= 1



obstacle_list = []
score = 0




# ı dont need for sounds

# Set up game states
START = 0
PLAYING = 1
GAME_OVER = 2
QUIT = 3
state = START

# Set up game loop
run = True

while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if state == START:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = PLAYING
        elif state == PLAYING:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x -= player_speed
                if event.key == pygame.K_RIGHT:
                    player_x += player_speed
        elif state == GAME_OVER:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = PLAYING
                player_x = WIDTH // 2
                player_y = HEIGHT - 50
                obstacle_list = []
                score = 0
        elif state == QUIT:
            run = False

    # Update game
    if state == PLAYING:
        # Move player
        if player_x < 0:
            player_x = 0
        if player_x + player_width > WIDTH:
            player_x = WIDTH - player_width

        # Add obstacles
        current_time = pygame.time.get_ticks()
        if current_time - last_obstacle_increase_time > obstacle_increase_interval:
            last_obstacle_increase_time = current_time
            for _ in range(obstacle_quantity):
                obstacle_x = random.randint(0, WIDTH - obstacle_width)
                obstacle_y = -obstacle_height
                obstacle_list.append([obstacle_x, obstacle_y])

        # Move obstacles
        for obstacle in obstacle_list:
            obstacle[1] += obstacle_speed

        # Check for collisions
        for obstacle in obstacle_list:
            if (player_x < obstacle[0] + obstacle_width and
                player_x + player_width > obstacle[0] and
                player_y < obstacle[1] + obstacle_height and
                player_y + player_height > obstacle[1]):
                state = GAME_OVER

        # Remove obstacles that have gone off screen
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle[1] < HEIGHT]

        # Increase score
        score += 1

    # Draw everything
    WIN.fill(WHITE)

    if state == START:
        text = font.render("Press SPACE to start", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        WIN.blit(text, text_rect)
    elif state == PLAYING:
        pygame.draw.rect(WIN, GREEN, (player_x, player_y, player_width, player_height))
        for obstacle in obstacle_list:
            pygame.draw.rect(WIN, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))
        text = font.render(f"Score: {score}", True, BLACK)
        WIN.blit(text, (10, 10))
    elif state == GAME_OVER:
        text = font.render("Game Over! Press SPACE to play again", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        WIN.blit(text, text_rect)
    elif state == QUIT:
        text = font.render("Press Q to quit", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        WIN.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()







 