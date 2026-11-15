import random
# Използваме "namespace" за да добавим нашият клас.
# "." показва, че файла се намира на същото място където е текущият файл.
# Ако е объркващо може да използвате "from src.CharacterClass import CharacterClass"

from .CharacterClass import CharacterClass

class SoldierClass(CharacterClass):
    def __init__(self, name, health, mana):
        super().__init__(name, health, mana)

    # Щитът ще намали стоиността на щетите които ще поеме героят.
    def use_shield(self):
        return random.randint(1, 20) - 0.2