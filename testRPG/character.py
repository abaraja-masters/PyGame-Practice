import pygame

class Character:
    def __init__(self, name, health, mana, attack_power, magic_power, defense_armor, defense_magic):
        self.name = name
        self.health = health
        self.mana = mana
        self.attack_power = attack_power
        self.magic_power = magic_power
        self.defense_armor = defense_armor
        self.defense_magic = defense_magic

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, other_character):
        damage = self.attack_power
        other_character.take_damage(damage)
        print(f"{self.name} attacks {other_character.name} for {damage} damage.")

    def display_status(self):
        print(f"{self.name} - Health: {self.health}, Attack Power: {self.attack_power}")