from Levels.level_1 import fight1
from Characters.Heroes.Hero import Hero

def main():
    hero = Hero()

    print("================================")
    print("       MY ADVENTURE GAME")
    print("================================")

    print()
    print("Your hero enters the dungeon...")

    survived = fight1(hero)

    if survived:
        print()
        print("You survived Fight 1!")
    else:
        print()
        print("Game Over")


if __name__ == "__main__":
    main()