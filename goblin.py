import random


class Goblin:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 15
        self.armor = 5

    def attack(self):
        """Return a random amount of damage around the attack power"""
        rand_num = random.randint(-5,5)
        return self.attack_power+rand_num

    def take_damage(self, damage):
        """Reduce health"""
        self.health -= max((damage - self.armor), 0)

    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0
