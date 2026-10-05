from Characters.character import Character

class Dinosaur(Character):
    def __init__(self):
        self.name = "Dinosaur"
        self.hitpoints = 80
        self.attack_power = 4
        self.defense = 0
        self.speed = 1
        self.heal_amount = 0
