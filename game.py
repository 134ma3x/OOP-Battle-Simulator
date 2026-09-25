import goblin
import boss
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
    elif enemy.is_alive():
        print(f"{enemy.name} won")
        return
    else:
        print(f"{hero.name} and {enemy.name} caused mutually assured destruction")

def main():
    global enemies, character
    """Open the arena and introduce its first opponent."""

    character = hero.Hero(input("Name your hero: "))

    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    enemies = []
    #for i in range(3):
    #    enemies.append(goblin.Goblin(name=f"Goblin {i+1}"))
    enemies.append(boss.Boss("The King"))

if __name__ == "__main__":
    main()
    for enemy in enemies:
        battle(character, enemy)