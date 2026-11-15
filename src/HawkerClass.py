from .CharacterClass import CharacterClass

class HawkerClass(CharacterClass):
    def __init__(self, name, health, mana):
        super().__init__(name, health, mana)

        self.bow_turn = 0

    def use_stealth(self):
        if self.mana >= 20:
            self.mana -= 20
            print(self.name, "uses Stealth!")

        else:
            print("Not enough mana!")

    def use_bow(self, target):
        damage = target.health * 0.35
        self.attack(target, damage)

        self.bow_turn += 1

        if self.bow_turn == 3:
            target.turns_skipped = 1
            self.bow_turn = 0

    def update_turn(self):
        super().update_turn()