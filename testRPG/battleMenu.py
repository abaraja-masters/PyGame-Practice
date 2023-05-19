import pygame, sys
from pygame.locals import *
from button import Button

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)

# Set up display
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Edgy RPG')
screenCenterX = screen.get_rect().centerx
screenCenterY = screen.get_rect().centery

# Set up Images
background_image = pygame.image.load("Pictures\edgy_wallpaper01.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

