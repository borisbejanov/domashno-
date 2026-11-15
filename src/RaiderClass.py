import random
from .CharacterClass import CharacterClass

class RaiderClass(CharacterClass):
    def __init__(self, name, health, mana, stamina=180):
        super().__init__(name, health, mana, stamina)

        self.blood_turn = 0
        self.camouflage_turns = 0
        self.next_attack_boost = False

    def use_double_slash(self, target):
        if self.stamina >= 30:
            self.stamina -= 30

            damage = random.randint(40, 50)

            target.take_damage(damage)
            target.take_damage(damage * 1.15)

    def use_camouflage(self):
        if self.mana >= 20 and self.stamina >= 25:
            self.mana -= 20
            self.stamina -= 25

            chance = random.randint(1, 100)

            if chance <= 30:
                self.camouflage_turns = 4
            elif chance <= 70:
                self.camouflage_turns = 3
            else:
                self.camouflage_turns = 2

    def use_screw_attack(self, target):
        target.take_damage(random.randint(70, 90))
        self.next_attack_boost = True

    def use_posion_knife(self, target):
        target.take_damage(random.randint(40, 80))

        target.poison_damage = 8
        target.poison_turns = 6

    def use_mana_blood(self, target):
        if self.blood_turn == 0:
            damage = target.health * 0.15
            target.take_damage(damage)

            self.mana = min(self.max_mana, self.mana + damage * (10 / 15))
            self.health = min(self.max_health, self.health + damage * (5 / 15))

            self.blood_turn = 2

    def update_turn(self):
        super().update_turn()

        if self.blood_turn > 0:
            self.blood_turn -= 1

        if self.camouflage_turns > 0:
            self.camouflage_turns -= 1