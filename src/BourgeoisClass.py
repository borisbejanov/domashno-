import random
from .CharacterClass import CharacterClass

class BourgeoisClass(CharacterClass):
    def __init__(self, name, health, mana, stamina=170):
        super().__init__(name, health, mana, stamina)

        self.overcharge_turn = 0
        self.warrior_turn = 0
        self.warrior_duration = 0

        self.warrior = None
        self.warrior_damage = 0

        self.rest_turns = 0

    def use_gun_smash(self, target):
        target.take_damage(random.randint(50, 70))

        if random.randint(1, 100) <= 15:
            target.turns_skipped = 1

    def use_overcharge(self, target):
        if self.overcharge_turn == 0 and self.mana >= 60 and self.stamina >= 30:
            self.mana -= 60
            self.stamina -= 30

            self.overcharge_turn = 6
            self.rest_turns = 1

    def use_employ_warrior(self):
        if self.warrior_turn == 0 and self.mana >= 80:
            self.mana -= 80

            self.warrior = CharacterClass(
                "Warrior",
                self.max_health / 2,
                0,
                0
            )

            self.warrior_damage = random.randint(30, 40)

            self.warrior_duration = 4
            self.warrior_turn = 4

    def use_aim_point(self, target):
        target.take_damage(random.randint(50, 80))

    def update_turn(self):
        super().update_turn()

        if self.overcharge_turn > 0:
            self.overcharge_turn -= 1

        if self.warrior_duration > 0:
            self.warrior_duration -= 1

            if self.warrior_duration == 0:
                self.warrior = None

        if self.warrior_turn > 0:
            self.warrior_turn -= 1

        if self.rest_turns > 0:
            self.rest_turns -= 1