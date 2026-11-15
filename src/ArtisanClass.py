import random
from .CharacterClass import CharacterClass

class ArtisanClass(CharacterClass):
    def __init__(self, name, health, mana, stamina=150):
        super().__init__(name, health, mana, stamina)

        self.evasion_turn = 0
        self.evasion = False

    def use_charge_shot(self, target):
        if self.stamina >= 35:
            self.stamina -= 35

            seconds = random.choices(
                [20, 30, 40, 50, 60, 70, 80],
                weights=[82, 8, 4, 2, 1, 0.5, 0.5]
            )[0]

            damage = 40 + (seconds - 20) * (160 / 60)

            target.take_damage(damage)

    def use_tripple_shot(self, target):
        if self.stamina >= 45:
            self.stamina -= 45

            damage = random.randint(60, 90)

            target.take_damage(damage)
            target.take_damage(damage * 0.85)
            target.take_damage(damage * 0.85 * 0.85)

    def use_evasion(self):
        if self.evasion_turn == 0:
            self.evasion = True
            self.evasion_turn = 2

    def update_turn(self):
        super().update_turn()

        if self.evasion_turn > 0:
            self.evasion_turn -= 1

            if self.evasion_turn == 0:
                self.evasion = False