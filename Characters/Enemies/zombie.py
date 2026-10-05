from Characters.character import Character

class Zombie(Character):
    def __init__(self):
        self.name = "Zombie"
        self.hitpoints = 20
        self.attack_power = 2
        self.defense = 0
        self.speed = 1
        self.heal_amount = 0
