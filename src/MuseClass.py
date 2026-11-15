from .CharacterClass import CharacterClass

class MuseClass(CharacterClass):
    def __init__(self, name, health, mana):
        super().__init__(name, health, mana)

    def use_spell(self, target):
        if self.mana >= 15:
            self.mana -= 15

        self.attack(target)

    def restore_mana(self):
        if self.mana != 0:
            self.mana *= 0.10
