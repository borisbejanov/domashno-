from .CharacterClass import CharacterClass
import random

class ClericClass(CharacterClass):
    def __init__(self, name, health, mana):
        super().__init__(name, health, mana)

        self.heal_turn = 0
        self.mana_turn = 0

        self.attack_turn = 0
        self.defense_turn = 0
        self.critical_turn = 0

        self.attack_duration = 0
        self.defense_duration = 0
        self.critical_duration = 0

        self.critical_chance = 0

    def use_greater_heal(self):
        if self.heal_turn == 0 and self.mana >= 100:
            self.mana -= 100

            heal = self.max_health * 0.35
            self.health += heal

            if self.health > self.max_health:
                self.health = self.max_health

            self.heal_turn = 6

    def use_mana_restore(self):
        if self.mana_turn == 0:
            restore = self.max_mana * 0.65
            self.mana += restore

            if self.mana > self.max_mana:
                self.mana = self.max_mana

            self.mana_turn = 4

    def use_attack_up(self):
        if self.attack_turn == 0 and self.mana >= 65:
            self.mana -= 65
            self.damage_multiplier = 1.40
            self.attack_duration = 3

    def use_defense_up(self):
        if self.defense_turn == 0:
            self.defense_multiplier = 0.72
            self.defense_duration = 3

    def use_critical_hit_enhance(self):
        if self.critical_turn == 0:
            self.critical_chance = 0.25
            self.critical_duration = 3

    def attack(self, target, damage=0):
        if damage:
            final_damage = damage
        else:
            final_damage = random.randint(1, 20)

        if random.random() <= self.critical_chance:
            final_damage *= 2

        target.take_damage(final_damage * self.damage_multiplier)

    def update_turn(self):
        super().update_turn()

        if self.heal_turn > 0:
            self.heal_turn -= 1

        if self.mana_turn > 0:
            self.mana_turn -= 1

        if self.attack_duration > 0:
            self.attack_duration -= 1

            if self.attack_duration == 0:
                self.damage_multiplier = 1.0
                self.attack_turn = 2

        elif self.attack_turn > 0:
            self.attack_turn -= 1

        if self.defense_duration > 0:
            self.defense_duration -= 1

            if self.defense_duration == 0:
                self.defense_multiplier = 1.0
                self.defense_turn = 2

        elif self.defense_turn > 0:
            self.defense_turn -= 1

        if self.critical_duration > 0:
            self.critical_duration -= 1

            if self.critical_duration == 0:
                self.critical_chance = 0
                self.critical_turn = 2

        elif self.critical_turn > 0:
            self.critical_turn -= 1