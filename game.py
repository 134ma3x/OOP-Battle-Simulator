from goblin import Goblin
import hero


ARENA_NAME = "The Greatest Arena to Exist"


def main():
    """Open the arena and introduce its first opponent."""

    character = hero.Hero(input("Name your hero: "))

    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Bribble")
    new_goblin = Goblin("Scribble")

    goblin.take_damage(character.gambit())
    print(f"Is the goblin still alive? {goblin.is_alive()} with {goblin.health}hp")


if __name__ == "__main__":
    main()