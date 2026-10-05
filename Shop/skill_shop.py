from Shop.upgrades import UPGRADES


def describe(upgrade):
    return f"+{upgrade['change']} {upgrade['stat_name']}"


def skill_shop(hero):
    print("Welcome to the skill shop!")
    print("Here you can buy upgrades for your hero.")

    while True:
        print("--------------------------------")
        print(f"You currently have {hero.prestige_points} prestige points.")
        for i, upgrade in enumerate(UPGRADES, start=1):
            print(f"{i}: {upgrade['name']}: {describe(upgrade)} | Cost: {upgrade['cost']} prestige point")
        print("0: Exit shop")
        
        choice = input("> ")   
        if choice == "0":
            break
        elif choice.isdigit():
            index = int(choice) - 1
            if index < 0 or index >= len(UPGRADES):
                print("Invalid choice. Please try again.")
                continue

            upgrade = UPGRADES[index]
            if hero.prestige_points >= upgrade['cost']:
                current_value = getattr(hero, upgrade['stat'])
                new_value = current_value + upgrade['change']
                setattr(hero, upgrade['stat'], new_value)
                hero.prestige_points = hero.prestige_points - upgrade['cost']
                print(f"You have purchased {upgrade['name']}! {describe(upgrade)}")
                print(f"Your {upgrade['stat_name']} has increased from {current_value} to {new_value}")
            else:
                print("You don't have enough prestige points to buy this skill.")
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for visiting the skill shop!")

