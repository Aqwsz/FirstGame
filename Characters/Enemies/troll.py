from Characters.character import Character

class Troll(Character):
    def __init__(self):
        self.name = "Troll"
        self.hitpoints = 40
        self.attack_power = 3
        self.defense = 0
        self.speed = 1
        self.heal_amount = 0
