from Characters.character import Character

class Bat(Character):
    def __init__(self):
        self.name = "Bat"
        self.hitpoints = 50
        self.attack_power = 3
        self.defense = 0
        self.speed = 1
        self.heal_amount = 0
