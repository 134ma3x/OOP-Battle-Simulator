import goblin
import hero


ARENA_NAME = "The Greatest Arena to Exist"

def battle(hero:hero.Hero, enemy:goblin.Goblin):
    while hero.is_alive() and enemy.is_alive():
        if hero.type == "melee":
            enemy.take_damage(hero.attack())
        elif hero.type == "mage":
            enemy.take_damage(hero.magic_attack())
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
    global character, goblin1
    character = hero.Hero(name=input("Name your hero: "),type="melee")

    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin1 = goblin.Goblin("Bribble")

if __name__ == "__main__":
    main()
    while character.is_alive():
        battle(character, goblin1)