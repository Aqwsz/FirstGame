from Characters.character import Character

class Skeleton(Character):
    def __init__(self):
        self.name = "Skeleton"
        self.hitpoints = 30
        self.attack_power = 2
        self.defense = 0
        self.speed = 1
        self.heal_amount = 0
