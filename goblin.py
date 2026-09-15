import random

class Goblin:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 15
        self.armor = 5

    def attack(self):
        """Return a random amount of melee damage around the attack power"""
        return self.attack_power*((random.randint(-10,10)+100)/100)

    def take_damage(self, damage):
        """Reduce health"""
        self.health -= max((damage - self.armor), 0)

    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0
