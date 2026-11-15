import random
from .CharacterClass import CharacterClass

class KnightClass(CharacterClass):
    def __init__(self, name, health, mana, stamina=250):
        super().__init__(name, health, mana, stamina)

        self.defense_turn = 0
        self.defense_duration = 0

        self.reflect_percent = 0

    def use_enhance_defence(self):
        if self.defense_turn == 0 and self.mana >= 30:
            self.mana -= 30

            self.defense_multiplier = 0.30
            self.defense_duration = 3
            self.defense_turn = 6

            self.turns_skipped += 1

    def use_shield_reflect(self, target):
        chance = random.randint(1, 100)

        if chance <= 80:
            self.reflect_percent = 0.05
        elif chance <= 95:
            self.reflect_percent = 0.20
        else:
            self.reflect_percent = 0.70

    def use_impact_wave(self, target):
        if self.stamina >= 45:
            self.stamina -= 45
            target.take_damage(random.randint(80, 100))

    def use_shield_slam(self, target):
        if self.stamina >= 30:
            self.stamina -= 30

            target.take_damage(random.randint(70, 90))

            if random.randint(1, 100) <= 8:
                target.turns_skipped = 1

    def use_one_hand_attack(self, target):
        target.take_damage(random.randint(40, 70))

    def update_turn(self):
        super().update_turn()

        if self.defense_duration > 0:
            self.defense_duration -= 1

            if self.defense_duration == 0:
                self.defense_multiplier = 1.0

        elif self.defense_turn > 0:
            self.defense_turn -= 1