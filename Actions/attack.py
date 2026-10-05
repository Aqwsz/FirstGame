def attack(self, target):
    target.hitpoints = target.hitpoints - self.attack_power
    print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")