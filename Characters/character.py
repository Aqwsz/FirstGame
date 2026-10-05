from Actions.import_all_actions import attack, heal

class Character:
    def is_alive(self):
        return self.hitpoints > 0

    def total_hitpoints(self, prestige):
        return self.hitpoints * (prestige + 1)

    attack = attack
    heal = heal
    