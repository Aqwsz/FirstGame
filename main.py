from Levels.levels import LEVELS
from Levels.fight import fight
from Characters.Heroes.hero import Hero
from Shop.skill_shop import skill_shop


def main():
    hero = Hero()

    print("================================")
    print("       MY ADVENTURE GAME")
    print("================================")

    print()
    print("Your hero enters the dungeon...")

    while hero.prestige < 2:
        for level in LEVELS:
            number = level["level"]
            print()
            if hero.prestige > 0:
                print(f"=== PRESTIGE {hero.prestige} - FIGHT {number} ===")
            else:
                print(f"=== FIGHT {number} ===")

            for group in level["enemies"]:
                for _ in range(group["count"]):
                    enemy = group["type"]()
                    enemy.scale_prestige(hero.prestige)
                    survive = fight(hero, enemy)

                    if not survive:
                        print()
                        print("Game Over")
                        return

            print()
            print(f"You survived Fight {number}!")

        print()
        hero.prestige = hero.prestige + 1
        hero.prestige_points = hero.prestige_points + hero.prestige
        print(f"Your prestige is now {hero.prestige}!")
        print(f"You gained {hero.prestige} prestige points!")
        print(f"You have {hero.prestige_points} prestige points!")
        print("--------------------------------")

        skill_shop(hero)

    print(f"You beat prestige {hero.prestige-1}! You win!")

if __name__ == "__main__":
    main()
