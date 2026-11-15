import random
from .CharacterClass import CharacterClass

class ChampionClass(CharacterClass):
    def __init__(self, name, health, mana, stamina=220):
        super().__init__(name, health, mana, stamina)

        self.berserk_turn = 0
        self.berserk_duration = 0

        self.blood_turn = 0

    def use_berserk(self):
        if self.berserk_turn == 0 and self.mana >= 40 and self.stamina >= 30:
            self.mana -= 40
            self.stamina -= 30

            self.health -= self.max_health * 0.10

            self.damage_multiplier = 1.70
            self.berserk_duration = 2

            self.berserk_turn = 6

    def use_blood_attack(self, target):
        if self.blood_turn == 0 and self.mana >= 20 and self.stamina >= 25:
            self.mana -= 20
            self.stamina -= 25

            damage = target.health * 0.15
            target.take_damage(damage)

            self.health = min(self.max_health, self.health + damage)
            self.blood_turn = 2

    def use_piercing_stab(self, target):
        target.take_damage(random.randint(50, 80))

        target.poison_damage = 5
        target.poison_turns = 5

    def use_leap_strike(self, target):
        target.take_damage(random.randint(70, 90))

    def update_turn(self):
        super().update_turn()

        if self.berserk_duration > 0:
            self.berserk_duration -= 1

            if self.berserk_duration == 0:
                self.damage_multiplier = 1.0

        if self.berserk_turn > 0:
            self.berserk_turn -= 1

        if self.blood_turn > 0:
            self.blood_turn -= 1