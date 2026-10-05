from Characters.Character import Character

class Hero(Character):
    def __init__(self):
        self.name = "Hero"
        self.hitpoints = 10
        self.attack_power = 5
        self.defense = 0
        self.speed = 1
        self.heal_amount = 5
