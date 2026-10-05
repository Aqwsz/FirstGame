from Actions.import_all_actions import attack, heal
from math import ceil

class Character:
    def is_alive(self):
        return self.hitpoints > 0


    # Scaling per prestige
    def total_hitpoints(self, prestige):
        return self.hitpoints * (prestige + 1)

    def total_attack_power(self, prestige):
        return ceil(self.attack_power * (prestige/2 + 1))
        

    # Applying prestige to enemies
    def scale_prestige(self, prestige):
        self.hitpoints = self.total_hitpoints(prestige)
        self.attack_power = self.total_attack_power(prestige)


    attack = attack
    heal = heal
    