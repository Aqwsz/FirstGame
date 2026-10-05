from Actions.import_all_actions import attack, heal

class Character:
    def is_alive(self):
        return self.hitpoints > 0

    attack = attack
    heal = heal
    