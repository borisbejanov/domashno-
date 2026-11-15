import random

# Родителският клас.
class CharacterClass:
    def __init__(self, name, health, mana, stamina=0):
        self.name = name

        self.health = health
        self.max_health = health

        self.mana = mana
        self.max_mana = mana

        self.stamina = stamina
        self.max_stamina = stamina

        self.turns_skipped = 0

        self.damage_multiplier = 1.0
        self.defense_multiplier = 1.0

        self.poison_damage = 0
        self.poison_turns = 0

    def take_damage(self, damage):
        damage = damage * self.defense_multiplier
        self.health = max(0.0, self.health - damage)

    def heal(self):
        self.health += random.randint(1, 20)

        if self.health > self.max_health:
            self.health = self.max_health

    def attack(self, target, damage: float | int = 0):
        if damage:
            target.take_damage(damage * self.damage_multiplier)
        else:
            damage = random.randint(1, 20)
            target.take_damage(damage * self.damage_multiplier)

    def is_alive(self):
        return self.health > 0

    def update_turn(self):
        if self.poison_turns > 0:
            self.health = max(0, self.health - self.poison_damage)
            self.poison_turns -= 1

    def restore_energypoints(self, hp, mp, sp):
        self.health = min(self.max_health, self.health + hp)
        self.mana = min(self.max_mana, self.mana + mp)
        self.stamina = min(self.max_stamina, self.stamina + sp)