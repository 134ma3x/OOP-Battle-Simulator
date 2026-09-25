import random


class Enemy:
    """A base class for every enemy in the arena."""

    def __init__(self, name, health, attack_power, armor):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.armor = armor

    def attack(self):
        """Return a random amount of damage around the attack power"""
        rand_num = random.randint(-5,5)
        return self.attack_power+rand_num

    def take_damage(self, damage):
        """Reduce health"""
        self.health -= max((damage - self.armor), 0)

    def is_alive(self):
        return self.health > 0