import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame")

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Render the game
    screen.fill((0, 0, 0))  # Fill the screen with black
    # Draw your game objects here

    pygame.display.flip()  # Update the screen

# Quit the game
pygame.quit()
