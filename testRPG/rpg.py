import pygame, sys
from pygame.locals import *
from button import Button
from character import Character
from helperVariables import *

pygame.init()

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(windowCaption)
screenCenterX = screen.get_rect().centerx
screenCenterY = screen.get_rect().centery

# Set up Images
background_image = pygame.image.load(menuWallpaper)
background_image = pygame.transform.scale(background_image, (width, height))

fighter_image = pygame.image.load(warriorImg)
fighter_image = pygame.transform.scale(fighter_image, (150, 150))

rogue_image = pygame.image.load(rogueImg)
rogue_image = pygame.transform.scale(rogue_image, (100, 100))

mage_image = pygame.image.load(mageImg)
mage_image = pygame.transform.scale(mage_image, (100, 100))

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
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

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
                        print("Quit Game clicked!")
                        pygame.quit()
                        sys.exit()
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
                    elif playerCharacter == 'Fighter':
                        player = Character('Fighter', 100, 0, 20, 0, 10, 0)
                    elif playerCharacter == 'Rogue':
                        player = Character('Rogue', 80, 20, 25, 10, 5, 50)
                    elif playerCharacter == 'Mage':
                        player = Character('Mage', 60, 50, 5, 25, 0, 10)

    screen.fill(BLACK)  # Clear the screen
    screen.blit(background_image, (0, 0))
    
    if current_screen == 1:
        screen.blit(textMainMenu, textRectMainMenu)
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
    elif current_screen == 2:
        screen.blit(textBattleMenu, textRectBattleMenu)
        buttonFighter.draw(screen)
        buttonRogue.draw(screen)
        buttonMage.draw(screen)
        buttonBack.draw(screen)
        screen.blit(fighter_image, (screenCenterX - 275, screenCenterY - 175))
        screen.blit(rogue_image, (screenCenterX - 75, screenCenterY - 150))
        screen.blit(mage_image, (screenCenterX + 125, screenCenterY - 150))
    elif current_screen == 3:
        screen.blit(textCharacterSelection, textRectCharacterSelection)
        buttonBack.draw(screen)
        # Render and Display character stats
        for i, line in enumerate(player.listStats()):
            text_surface = basicFont.render(line, True, WHITE)  # White
            screen.blit(text_surface, (screenCenterX - 300, screenCenterY - 100 + i * 30))

    pygame.display.update()

pygame.quit()

