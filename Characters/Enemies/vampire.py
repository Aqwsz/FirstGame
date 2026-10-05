from Characters.character import Character

class Vampire(Character):
    def __init__(self):
        self.name = "Vampire"
        self.hitpoints = 25
        self.attack_power = 2
        self.defense = 0
        self.speed = 1
        self.heal_amount = 0
