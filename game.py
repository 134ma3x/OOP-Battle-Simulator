from goblin import Goblin


ARENA_NAME = "The Greatest Arena to Exist"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Bribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    new_goblin = Goblin("Scribble")

    print(f"{new_goblin.name} enters the arena with {new_goblin.health} health.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()