def heal(self):
    self.hitpoints = self.hitpoints + self.heal_amount
    print(f"{self.name} heals for {self.heal_amount} hitpoints.")
