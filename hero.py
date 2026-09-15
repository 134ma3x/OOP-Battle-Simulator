import random
from typing import Literal

class Hero:
    """Hero class with attack, take_damage, and is_alive"""
    def __init__(self, name, type:str=Literal["melee","mage"]):
        self.name = name
        self.type = type
        if type == "melee":
            self.health = 150
            self.attack_power = 20
            self.armor = 10
            self.max_mana = 1
            self.current_mana = 1
            self.magic_power = 0
            self.magic_armor = 0
        elif type == "mage":
            self.health = 100
            self.attack_power = 5
            self.armor = 0
            self.max_mana = 10
            self.current_mana = 10
            self.magic_power = 20
            self.magic_armor = 15


    def gambit(self):
        if random.randint(0,1):
            return 2*self.attack_power*((random.randint(-10,10)+100)/100)
        else:
            return 0

    def attack(self):
        """Return a random amount of melee damage around the attack power"""
        return self.attack_power*((random.randint(-10,10)+100)/100)

    def magic_attack(self):
        """Return a random amount of magic damage around the attack power"""
        if self.current_mana <= 0:
            return
        else:
            self.current_mana -= 1
        return self.magic_power*((random.randint(-15,15)+100)/100)

    def take_damage(self, damage):
        """Reduces health"""
        self.health -= max((damage - self.armor), 0)

    def is_alive(self):
        """Returns True if health is >0."""
        return self.health > 0