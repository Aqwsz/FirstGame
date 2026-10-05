from Levels.level_1 import fight1
from Levels.level_2 import fight2
from Levels.level_3 import fight3
from Levels.level_4 import fight4
from Levels.level_5 import fight5
from Levels.level_6 import fight6
from Levels.level_7 import fight7
from Levels.level_8 import fight8
from Levels.level_9 import fight9
from Levels.level_10 import fight10
from Characters.Heroes.hero import Hero

LEVELS = [fight1, fight2, fight3, fight4, fight5, fight6, fight7, fight8, fight9, fight10]


def main():
    hero = Hero()

    print("================================")
    print("       MY ADVENTURE GAME")
    print("================================")

    print()
    print("Your hero enters the dungeon...")

    for number, level in enumerate(LEVELS, start=1):
        print()
        print(f"=== FIGHT {number} ===")

        if not level(hero):
            print()
            print("Game Over")
            return

        print()
        print(f"You survived Fight {number}!")

    print()
    print("You beat all the levels! You win!")


if __name__ == "__main__":
    main()
