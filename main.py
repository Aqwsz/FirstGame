from Levels.level_1 import fight1
from Levels.level_2 import fight2
from Characters.Heroes.hero import Hero

def main():
    hero = Hero()

    print("================================")
    print("       MY ADVENTURE GAME")
    print("================================")

    print()
    print("Your hero enters the dungeon...")

    if not fight1(hero):
        print()
        print("Game Over")
        return

    print()
    print("You survived Fight 1!")
    print()

    if not fight2(hero):
        print()
        print("Game Over")
        return

    print()
    print("You survived Fight 2!")


if __name__ == "__main__":
    main()