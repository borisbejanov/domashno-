import random
from .CharacterClass import CharacterClass

class DealerClass(CharacterClass):
    def __init__(self, name, health, mana):
        super().__init__(name, health, mana)

    def use_gun(self, target):
        damage = target.health * 0.55
        self.attack(target, damage)

        if random.randint(1, 5) == 1:
            target.turns_skipped = 2

    def update_turn(self):
        super().update_turn()