# File: rpg.py
# Copyright (C) 2023 The Unlicense
# This is the game initial driver, and is part of Edgy RPG.

import pygame, sys
from pygame.locals import *
from button import Button
from character import Character
from helperVariables import *
from eventHandler import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(windowCaption)
screenCenterX = screen.get_rect().centerx
screenCenterY = screen.get_rect().centery

# Set up Images
background_image = pygame.image.load(menuWallpaper)
background_image = pygame.transform.scale(background_image, (width, height))

dungeon_background = pygame.image.load(dungeonBG) #.convert_alpha()
dungeon_background = pygame.transform.scale(dungeon_background, (width, height - ingame_battle_bottom_panel))
panel_background = pygame.image.load(panelBG) #.convert_alpha()
panel_background = pygame.transform.scale(panel_background, (width, ingame_battle_bottom_panel))

fighter_image = pygame.image.load(charDict["Fighter"].get_imagefilepath())
fighter_image = pygame.transform.scale(fighter_image, (150, 150))

rogue_image = pygame.image.load(charDict["Rogue"].get_imagefilepath())
rogue_image = pygame.transform.scale(rogue_image, (100, 100))

mage_image = pygame.image.load(charDict["Mage"].get_imagefilepath())
mage_image = pygame.transform.scale(mage_image, (100, 100))

rat_image = pygame.image.load(charDict["Rat1"].get_imagefilepath())
rat_image = pygame.transform.scale(rat_image, (100, 100))

# Set up the text
basicFont = pygame.font.SysFont(None, 48)

textMainMenu = basicFont.render(windowCaption, True, WHITE, BLACK)
textRectMainMenu = textMainMenu.get_rect()
textRectMainMenu.centerx = screenCenterX
textRectMainMenu.centery = screenCenterY - 200

textBattleMenu = basicFont.render('Choose Your Character', True, WHITE, BLACK)
textRectBattleMenu = textBattleMenu.get_rect()
textRectBattleMenu.centerx = screenCenterX
textRectBattleMenu.centery = screenCenterY - 200

textCharacterSelection = basicFont.render('Your Character', True, WHITE, BLACK)
textRectCharacterSelection = textCharacterSelection.get_rect()
textRectCharacterSelection.centerx = screenCenterX
textRectCharacterSelection.centery = screenCenterY - 200

# Set up Buttons
button1 = Button(screenCenterX - 75, screenCenterY - 100, 150, 50, "Start Adventure")
button2 = Button(screenCenterX - 75, screenCenterY, 150, 50, "Options")
button3 = Button(screenCenterX - 75, screenCenterY + 100, 150, 50, "Quit Game")

buttonFighter = Button(screenCenterX - 275, screenCenterY, 150, 50, "Fighter")
buttonRogue = Button(screenCenterX - 75, screenCenterY, 150, 50, "Rogue")
buttonMage = Button(screenCenterX + 125, screenCenterY, 150, 50, "Mage")
buttonBack = Button(50, 50, 150, 50, "Back")

buttonPlay = Button(screenCenterX, screenCenterY + 200, 150, 50, "Play")

# Set up the background music
pygame.mixer.music.load(menuBGMusicFilePath)
pygame.mixer.music.play(-1, 22.5)

# Set up screen current_screen
current_screen = 1

# Set up character selection
playerCharacter = ''

# Game Loop
running = True
while running:

    clock.tick(fps)
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            quit()

        # Check for mouse click events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if current_screen == 1:
                    if button1.is_clicked(event.pos):
                        print("Start Game clicked!")
                        current_screen = 2
                    elif button2.is_clicked(event.pos):
                        print("Options clicked!")
                    elif button3.is_clicked(event.pos):
                        quit()
                if current_screen == 2:
                    if buttonBack.is_clicked(event.pos):
                        print("Back Button clicked!")
                        current_screen = 1
                    elif buttonFighter.is_clicked(event.pos):
                        playerCharacter = 'Fighter'
                        current_screen = 3
                    elif buttonRogue.is_clicked(event.pos):
                        playerCharacter = 'Rogue'
                        current_screen = 3
                    elif buttonMage.is_clicked(event.pos):
                        playerCharacter = 'Mage'
                        current_screen = 3
                if current_screen == 3:
                    if buttonBack.is_clicked(event.pos):
                        print("Back Button clicked!")
                        current_screen = 2
                    elif buttonPlay.is_clicked(event.pos):
                        print("Play Button Click!")
                        current_screen = 4
                    elif playerCharacter == 'Fighter':
                        player = charDict["Fighter"]
                    elif playerCharacter == 'Rogue':
                        player = charDict["Rogue"]
                    elif playerCharacter == 'Mage':
                        player = charDict["Mage"]

    screen.fill(BLACK)  # Clear the screen
    
    if current_screen == 1:  # Main Menu
        screen.blit(background_image, (0, 0))
        screen.blit(textMainMenu, textRectMainMenu)
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
    elif current_screen == 2:  # Player Character Selection
        screen.blit(background_image, (0, 0))
        screen.blit(textBattleMenu, textRectBattleMenu)
        buttonFighter.draw(screen)
        buttonRogue.draw(screen)
        buttonMage.draw(screen)
        buttonBack.draw(screen)
        screen.blit(fighter_image, (screenCenterX - 275, screenCenterY - 175))
        screen.blit(rogue_image, (screenCenterX - 75, screenCenterY - 150))
        screen.blit(mage_image, (screenCenterX + 125, screenCenterY - 150))
    elif current_screen == 3:  # Display Player Character Stats
        screen.blit(background_image, (0, 0))
        screen.blit(textCharacterSelection, textRectCharacterSelection)
        buttonBack.draw(screen)
        buttonPlay.draw(screen)
        # Render and Display character stats
        for i, line in enumerate(player.listStats()):
            text_surface = basicFont.render(line, True, WHITE)  # White
            screen.blit(text_surface, (screenCenterX - 300, screenCenterY - 100 + i * 30))
    elif current_screen == 4:  # Battle Screen
        screen.blit(dungeon_background, (0, 0))
        screen.blit(panel_background, (0, height - ingame_battle_bottom_panel))
        # Player Side
        player.draw(screen, 650, 460)
        # Enemy Side
        rat1 = charDict["Rat1"]
        rat2 = charDict["Rat1"]
        rat1.draw(screen, 100, 460)
        rat2.draw(screen, 300, 460)

    pygame.display.update()

pygame.quit()

