from src.CharacterClass import CharacterClass
from src.SoldierClass import SoldierClass
from src.MuseClass import MuseClass

def main():
    john = SoldierClass('John', 100, 100)
    alex = MuseClass('Alex', 100, 100)

    round_number = 1

    while john.is_alive() and alex.is_alive():
        print('Round ' + str(round_number))

        if round_number % 2 == 0:
            john.heal()
            alex.heal()

        # Всеки 4 рунда се възстановява маната
        if round_number % 4 == 0 and isinstance(alex, MuseClass):
            alex.restore_mana

        if isinstance(john, SoldierClass):
            # Атакуваме героя alex, но намаляваме щетите които ще му нанесем
            damage_reduction = john.use_shield()

            john.attack(alex, damage_reduction)

        if isinstance(alex, MuseClass):
            # Атакуваме героя alex, но намаляваме щетите които ще му нанесем
            alex.use_spell(john)

        if alex.is_alive():
            alex.attack(john)

        round_number += 1


    print('Winner is')

    if john.is_alive():
        print('John')
    elif alex.is_alive():
        print('Alex')

if __name__ == "__main__":
    main()