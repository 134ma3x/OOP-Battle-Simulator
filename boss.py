import random
import enemy

class Boss(enemy.Enemy):
    def __init__(self, name):
        super().__init__(name, 300, 25, 15)

    def attack(self):
        if random.randint(0,1):
            if random.randint(0,1):
                if random.randint(0,1):
                    return super().attack() * 2
                else:
                    return super().attack() * 1.5
            else:
                return super().attack()
        else:
            return super().attack()