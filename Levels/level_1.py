from Characters.Enemies.spider import Spider

def fight1(hero):
    print("=== FIGHT 1 ===")
    print("A spider appears!")

    spider = Spider()

    while hero.hitpoints > 0 and spider.is_alive():

        print()
        print(f"Hero HP: {hero.hitpoints}")
        print(f"Spider HP: {spider.hitpoints}")

        print()
        print("1. Attack")
        print("2. Heal")

        choice = input("> ")

        if choice == "1":
            hero.attack(spider)

        elif choice == "2":
            hero.heal()

        else:
            print("Invalid choice.")
            continue

        if spider.is_alive():
            spider.attack(hero)


    if hero.hitpoints <= 0:
        print("You died!")
        return False

    if not spider.is_alive():
        print("You defeated the spider!")
        return True