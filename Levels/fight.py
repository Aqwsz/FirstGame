def fight(hero, enemy):
    article = "An" if enemy.name[0] in "AEIOU" else "A"
    print(f"{article} {enemy.name} appears!")

    while hero.is_alive() and enemy.is_alive():

        print()
        print(f"{hero.name} HP: {hero.hitpoints}")
        print(f"{enemy.name} HP: {enemy.hitpoints}")

        print()
        print("1. Attack")
        print("2. Heal")

        choice = input("> ")

        if choice == "1":
            hero.attack(enemy)

        elif choice == "2":
            hero.heal()

        else:
            print("Invalid choice.")
            continue

        if enemy.is_alive():
            enemy.attack(hero)

    if not hero.is_alive():
        print("You died!")
        return False

    print(f"You defeated the {enemy.name.lower()}!")
    return True
