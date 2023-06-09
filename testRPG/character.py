import pygame

class Character:
    def __init__(self, className, health, mana, attack_power, magic_power, defense_armor, defense_magic, image_file_path):
        self.className = className
        self.health = health
        self.mana = mana
        self.attack_power = attack_power
        self.magic_power = magic_power
        self.defense_armor = defense_armor
        self.defense_magic = defense_magic
        self.image_file_path = image_file_path

    def get_imagefilepath(self):
        return self.image_file_path
    
    def draw(self, screen, x, y):
        self.image = pygame.image.load(self.image_file_path)
        self.image = pygame.transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        screen.blit(self.image, self.rect)

    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, other_character):
        damage = self.attack_power
        other_character.take_damage(damage)
        print(f"{self.name} attacks {other_character.name} for {damage} damage.")

    def display_status(self):
        print(f"{self.className} - Health: {self.health}, Mana: {self.mana}")
    
    def listStats(self):
        return [
            f'Class: {self.className}', 
            f'Health: {self.health}',
            f'Mana: {self.mana}',
            f'Attack Power: {self.attack_power}',
            f'Magic Power: {self.magic_power}',
            f'Defense Armor: {self.defense_armor}',
            f'Magic Shield: {self.defense_magic}'
        ]