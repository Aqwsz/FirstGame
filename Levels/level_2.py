from Characters.Enemies.zombie import Zombie

def fight2(hero):
    print("=== FIGHT 2 ===")
    print("A Zombie appears!")

    zombie = Zombie()

    while hero.hitpoints > 0 and zombie.is_alive():

        print()
        print(f"Hero HP: {hero.hitpoints}")
        print(f"Zombie HP: {zombie.hitpoints}")

        print()
        print("1. Attack")
        print("2. Heal")

        choice = input("> ")

        if choice == "1":
            hero.attack(zombie)

        elif choice == "2":
            hero.heal()

        else:
            print("Invalid choice.")
            continue

        if zombie.is_alive():
            zombie.attack(hero)


    if hero.hitpoints <= 0:
        print("You died!")
        return False

    if not zombie.is_alive():
        print("You defeated the zombie!")
        return True