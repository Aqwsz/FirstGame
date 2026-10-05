from Characters.character import Character

class Ogre(Character):
    def __init__(self):
        self.name = "Ogre"
        self.hitpoints = 35
        self.attack_power = 3
        self.defense = 0
        self.speed = 1
        self.heal_amount = 0
