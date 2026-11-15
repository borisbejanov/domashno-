import random
from .CharacterClass import CharacterClass

class MageClass(CharacterClass):
    def __init__(self, name, health, mana):
        super().__init__(name, health, mana)

        self.quick_cast_turn = 0

        self.fire_turn = 0
        self.fire_target = None

    def use_fireball(self, target):
        if self.mana >= 70:
            self.mana -= 70

            damage = random.randint(50, 80)
            target.take_damage(damage)

            self.fire_turn = 3
            self.fire_target = target

    def use_ice_ball(self, target):
        if self.mana >= 55:
            self.mana -= 55

            damage = random.randint(30, 50)
            target.take_damage(damage)

            if random.randint(1, 100) <= 15:
                target.turns_skipped = 1

    def use_lightning_ball(self, target):
        if self.mana >= 85:
            self.mana -= 85

            damage = random.randint(60, 70)
            target.take_damage(damage)

            if random.randint(1, 100) <= 5:
                target.turns_skipped = 1

    def use_quick_cast(self):
        if self.quick_cast_turn == 0 and self.mana >= 60:
            self.mana -= 60
            self.quick_cast_turn = 6

    def update_turn(self):
        super().update_turn()

        if self.quick_cast_turn > 0:
            self.quick_cast_turn -= 1

        if self.fire_turn > 0:
            if self.fire_target is not None and self.fire_target.is_alive():
                self.fire_target.take_damage(5)

            self.fire_turn -= 1

        if self.fire_turn == 0:
            self.fire_target = None