import random

class Hero:
    """Hero class with attack, take_damage, and is_alive"""
    def __init__(self, name):
        self.name = name
        self.health = 200
        self.attack_power = 20
        self.armor = 10

    def gambit(self):
        if random.randint(0,1):
            rand_num = random.randint(-5,5)
            return 2*(self.attack_power+rand_num)
        else:
            return 0

    def attack(self):
        """Return a random amount of damage around the attack power"""
        rand_num = random.randint(-5,5)
        return self.attack_power+rand_num

    def take_damage(self, damage):
        """Reduces health"""
        self.health -= max((damage - self.armor), 0)

    def is_alive(self):
        """Returns True if health is >0."""
        return self.health > 0