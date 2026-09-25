import goblin
import hero


ARENA_NAME = "The Greatest Arena to Exist"

def battle(hero:hero.Hero, enemy:goblin.Goblin):
    """battle between players/npcs"""
    while hero.is_alive() and enemy.is_alive():
        enemy.take_damage(hero.attack())
        if enemy.is_alive():
            hero.take_damage(enemy.attack())
        print(f"{hero.name} has {hero.health} health")
        print(f"{enemy.name} has {enemy.health} health")

    if hero.is_alive():
        print(f"{hero.name} won")
        return
    if enemy.is_alive():
        print(f"{enemy.name} won")
        return

def main():
    """Open the arena and introduce its first opponent."""

    character = hero.Hero(input("Name your hero: "))

    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblins = []
    for i in range(3):
        goblins.append(goblin.Goblin(name=i))

    goblin.take_damage(character.gambit())
    print(f"Is the goblin still alive? {goblin.is_alive()} with {goblin.health}hp")


if __name__ == "__main__":
    main()
    for gobby in goblins:
        battle(character, gobby)