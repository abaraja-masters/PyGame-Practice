import csv
from character import Character

# Text Variables:
windowCaption = 'Edgy RPG'

# Color Variables:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)

# Dimension Variables:
ingame_battle_bottom_panel = 200
width, height = 800, 600 + ingame_battle_bottom_panel


# Image File Path Variables:
menuWallpaper = 'Pictures\edgy_wallpaper01.jpg'

dungeonBG = 'Pictures\dungeon_background01.jpg'
panelBG = 'Pictures\panel.png'

#warriorImg = 'Pictures\\heroes\\warrior\\fighter01.png'
#rogueImg = 'Pictures\\heroes\\rogue\\rogue.png'
#mageImg = 'Pictures\\heroes\\mage\\mage.png'

# Sound File Path Variables:
menuBGMusicFilePath = 'Sounds\DarkFantasySong.mp3'

# Load Characters and Enemies from csv file to a Dictionary
charDict = dict()
with open('Datasets/characterDS.csv', newline='') as csvFile:
    csvCharRecords = csv.DictReader(csvFile)
    for record in csvCharRecords:
        charDict[record["name"]] = Character(
                                              record["name"], 
                                              record["health"], 
                                              record["mana"], 
                                              record["attack_power"], 
                                              record["magic_power"], 
                                              record["defense_armor"], 
                                              record["defense_magic"],
                                              record["image_file_path"]
                                            )
