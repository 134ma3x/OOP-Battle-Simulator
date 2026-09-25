import random
import enemy

class Goblin(enemy.Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, 100, 15, 5)
    