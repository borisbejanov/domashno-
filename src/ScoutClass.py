import random
from .CharacterClass import CharacterClass

class ScoutClass(CharacterClass):
    def __init__(self, name, health, mana, stamina=150):
        super().__init__(name, health, mana, stamina)

        self.speed_shot_turn = 0

    def use_tripple_shot(self, target):
        if self.stamina >= 45:
            self.stamina -= 45

            damage = random.randint(50, 80)

            target.take_damage(damage)
            target.take_damage(damage * 0.85)
            target.take_damage(damage * 0.85 * 0.85)

    def use_eagle_shot(self, target):
        damage = random.randint(50, 90)
        target.take_damage(damage)

        if random.randint(1, 100) <= 35:
            target.turns_skipped = 1

    def use_speed_shot(self):
        if self.speed_shot_turn == 0:
            self.speed_shot_turn = 6

    def use_poison_arrow(self, target):
        if self.mana >= 35 and self.stamina >= 25:
            self.mana -= 35
            self.stamina -= 25

            target.take_damage(random.randint(40, 80))

            target.poison_damage = 5
            target.poison_turns = 6

    def update_turn(self):
        super().update_turn()

        if self.speed_shot_turn > 0:
            self.speed_shot_turn -= 1