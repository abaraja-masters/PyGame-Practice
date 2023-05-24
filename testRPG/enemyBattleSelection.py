import pygame
from pygame.locals import *
from button import Button

buttonBack = Button(50, 50, 150, 50, "Back")

def enemyBattleScreen(screen):
    buttonBack.draw(screen)
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            quit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if buttonBack.is_clicked(event.pos):
                    print("Back Button clicked!")
                    current_screen = 3
                    return
